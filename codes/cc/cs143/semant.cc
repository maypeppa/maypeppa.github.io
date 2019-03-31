

#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include "semant.h"
#include "utilities.h"
#include <vector>


extern int semant_debug;
extern char *curr_filename;

//////////////////////////////////////////////////////////////////////
//
// Symbols
//
// For convenience, a large number of symbols are predefined here.
// These symbols include the primitive type and method names, as well
// as fixed names used by the runtime system.
//
//////////////////////////////////////////////////////////////////////
static Symbol
    arg,
    arg2,
    Bool,
    concat,
    cool_abort,
    copy,
    Int,
    in_int,
    in_string,
    IO,
    length,
    Main,
    main_meth,
    No_class,
    No_type,
    Object,
    out_int,
    out_string,
    prim_slot,
    self,
    SELF_TYPE,
    Str,
    str_field,
    substr,
    type_name,
    val;
//
// Initializing the predefined symbols.
//
static void initialize_constants(void)
{
    arg         = idtable.add_string("arg");
    arg2        = idtable.add_string("arg2");
    Bool        = idtable.add_string("Bool");
    concat      = idtable.add_string("concat");
    cool_abort  = idtable.add_string("abort");
    copy        = idtable.add_string("copy");
    Int         = idtable.add_string("Int");
    in_int      = idtable.add_string("in_int");
    in_string   = idtable.add_string("in_string");
    IO          = idtable.add_string("IO");
    length      = idtable.add_string("length");
    Main        = idtable.add_string("Main");
    main_meth   = idtable.add_string("main");
    //   _no_class is a symbol that can't be the name of any
    //   user-defined class.
    No_class    = idtable.add_string("_no_class");
    No_type     = idtable.add_string("_no_type");
    Object      = idtable.add_string("Object");
    out_int     = idtable.add_string("out_int");
    out_string  = idtable.add_string("out_string");
    prim_slot   = idtable.add_string("_prim_slot");
    self        = idtable.add_string("self");
    SELF_TYPE   = idtable.add_string("SELF_TYPE");
    Str         = idtable.add_string("String");
    str_field   = idtable.add_string("_str_field");
    substr      = idtable.add_string("substr");
    type_name   = idtable.add_string("type_name");
    val         = idtable.add_string("_val");
}



ClassTable::ClassTable(Classes classes) : semant_errors(0) , error_stream(cerr) {

    /* Fill this in */
    install_basic_classes();


    int n = classes->len();
    std::vector<Symbol> seen;
    int main_class_found = 0;
    for (int i = 0; i < n; i++) {
        ClassClass c = static_cast<ClassClass>(classes->nth(i));
        if (c->name == SELF_TYPE) {
            semant_error(c->filename, c) << "Redefinition of basic class SELF_TYPE" << endl;
        }
        for(int j = 0; j < builtin_classes->len(); j++) {
            ClassClass c2 = static_cast<ClassClass>(builtin_classes->nth(j));
            if (c->name == c2->name) {
                semant_error(c->filename, c) << "Conflict with builtin classes " << c2->name << endl;
            }
        }
        for(size_t j = 0; j < seen.size(); j ++) {
            if(c->name == seen[j]) {
                semant_error(c->filename, c) << "Redefinition of class " << c->name << endl;
            }
        }
        seen.push_back(c->name);
        if (c->name == Main) {
            main_class_found = 1;
        }
    }
    if (!main_class_found) {
        semant_error() << "Class Main is not defined." << endl;
    }

    my_classes = append_Classes(builtin_classes, classes);
    check_classes = classes;
    // cerr << "builtin_classes len = " << builtin_classes->len() << endl;
    // cerr << "classes len = " << classes->len()  << endl;
    // cerr << "my_classes len = " << my_classes->len()  << endl;
    vtab = new AttrClassTable();
    mtab = new MethodClassTable();
}

void ClassTable::install_basic_classes() {

    // The tree package uses these globals to annotate the classes built below.
   // curr_lineno  = 0;
    Symbol filename = stringtable.add_string("<basic class>");

    // The following demonstrates how to create dummy parse trees to
    // refer to basic Cool classes.  There's no need for method
    // bodies -- these are already built into the runtime system.

    // IMPORTANT: The results of the following expressions are
    // stored in local variables.  You will want to do something
    // with those variables at the end of this method to make this
    // code meaningful.

    //
    // The Object class has no parent class. Its methods are
    //        abort() : Object    aborts the program
    //        type_name() : Str   returns a string representation of class name
    //        copy() : SELF_TYPE  returns a copy of the object
    //
    // There is no need for method bodies in the basic classes---these
    // are already built in to the runtime system.

    Class_ Object_class =
	class_(Object,
	       No_class,
	       append_Features(
			       append_Features(
					       single_Features(method(cool_abort, nil_Formals(), Object, no_expr())),
					       single_Features(method(type_name, nil_Formals(), Str, no_expr()))),
			       single_Features(method(copy, nil_Formals(), SELF_TYPE, no_expr()))),
	       filename);

    //
    // The IO class inherits from Object. Its methods are
    //        out_string(Str) : SELF_TYPE       writes a string to the output
    //        out_int(Int) : SELF_TYPE            "    an int    "  "     "
    //        in_string() : Str                 reads a string from the input
    //        in_int() : Int                      "   an int     "  "     "
    //
    Class_ IO_class =
	class_(IO,
	       Object,
	       append_Features(
			       append_Features(
					       append_Features(
							       single_Features(method(out_string, single_Formals(formal(arg, Str)),
										      SELF_TYPE, no_expr())),
							       single_Features(method(out_int, single_Formals(formal(arg, Int)),
										      SELF_TYPE, no_expr()))),
					       single_Features(method(in_string, nil_Formals(), Str, no_expr()))),
			       single_Features(method(in_int, nil_Formals(), Int, no_expr()))),
	       filename);

    //
    // The Int class has no methods and only a single attribute, the
    // "val" for the integer.
    //
    Class_ Int_class =
	class_(Int,
	       Object,
	       single_Features(attr(val, prim_slot, no_expr())),
	       filename);

    //
    // Bool also has only the "val" slot.
    //
    Class_ Bool_class =
	class_(Bool, Object, single_Features(attr(val, prim_slot, no_expr())),filename);

    //
    // The class Str has a number of slots and operations:
    //       val                                  the length of the string
    //       str_field                            the string itself
    //       length() : Int                       returns length of the string
    //       concat(arg: Str) : Str               performs string concatenation
    //       substr(arg: Int, arg2: Int): Str     substring selection
    //
    Class_ Str_class =
	class_(Str,
	       Object,
	       append_Features(
			       append_Features(
					       append_Features(
							       append_Features(
									       single_Features(attr(val, Int, no_expr())),
									       single_Features(attr(str_field, prim_slot, no_expr()))),
							       single_Features(method(length, nil_Formals(), Int, no_expr()))),
					       single_Features(method(concat,
								      single_Formals(formal(arg, Str)),
								      Str,
								      no_expr()))),
			       single_Features(method(substr,
						      append_Formals(single_Formals(formal(arg, Int)),
								     single_Formals(formal(arg2, Int))),
						      Str,
						      no_expr()))),
	       filename);


    builtin_classes = append_Classes(
        single_Classes(Object_class),
        append_Classes(
            single_Classes(IO_class),
            append_Classes(
                single_Classes(Int_class),
                append_Classes(
                    single_Classes(Bool_class),
                    single_Classes(Str_class)))));
}

////////////////////////////////////////////////////////////////////
//
// semant_error is an overloaded function for reporting errors
// during semantic analysis.  There are three versions:
//
//    ostream& ClassTable::semant_error()
//
//    ostream& ClassTable::semant_error(Class_ c)
//       print line number and filename for `c'
//
//    ostream& ClassTable::semant_error(Symbol filename, tree_node *t)
//       print a line number and filename
//
///////////////////////////////////////////////////////////////////

ostream& ClassTable::semant_error(tree_node* t)
{
    return semant_error(cc->get_filename(),t);
}

ostream& ClassTable::semant_error(Symbol filename, tree_node *t)
{
    error_stream << filename << ":" << t->get_line_number() << ": ";
    return semant_error();
}

ostream& ClassTable::semant_error()
{
    semant_errors++;
    return error_stream;
}



/*   This is the entry point to the semantic checker.

     Your checker should do the following two things:

     1) Check that the program is semantically correct
     2) Decorate the abstract syntax tree with type information
        by setting the `type' field in each Expression node.
        (see `tree.h')

     You are free to first do 1), make sure you catch all semantic
     errors. Part 2) can be done in a second stage, when you want
     to build mycoolc.
 */
void program_class::semant()
{
    initialize_constants();

    /* ClassTable constructor may do some semantic analysis */
    ClassTable *classtable = new ClassTable(classes);
    if (classtable->errors()) {
	cerr << "Compilation halted due to static semantic errors." << endl;
	exit(1);
    }

    /* some semantic analysis code may go here */

    // 1. check inheritance graph
    classtable->check_inheritance_graph();

    if (classtable->errors()) {
	cerr << "Compilation halted due to static semantic errors." << endl;
	exit(1);
    }

    // 2. check class pre semantic
    classtable->check_class_pre_semantic();

    if (classtable->errors()) {
	cerr << "Compilation halted due to static semantic errors." << endl;
	exit(1);
    }

    // 3. check types and semantics.
    classtable->check_class_semantic();

    if (classtable->errors()) {
	cerr << "Compilation halted due to static semantic errors." << endl;
	exit(1);
    }
}

ClassClass ClassTable::find_class_by_symbol(Symbol sym) {
    if (sym == prim_slot) sym = Object;
    if (sym == SELF_TYPE) {
        return cc;
    }
    int n = my_classes->len();
    for (int i = 0; i < n; i ++) {
        Class_ c = my_classes->nth(i);
        ClassClass c2 = static_cast<ClassClass>(c);
        if (c2 -> name == sym) {
            return c2;
        }
    }
    return NULL;
}


void ClassTable::check_inheritance_graph(Class_ c) {
    ClassClass c2 = static_cast<ClassClass>(c);
    if (c2->parent == Str || c2->parent == Int || c2->parent == Bool) {
        semant_error(c2->filename, c2) << "Can not inherit from basic class" << endl;
    }

    std::vector<Symbol> seen;
    while(c2->parent != No_class) {
        Symbol name = c2->name;
        int found = 0;
        for(std::vector<Symbol>::const_iterator it = seen.begin();
            it != seen.end(); ++ it) {
            if (*it == name) {
                found = 1;
                break;
            }
        }
        if (found) {
            semant_error(c2->filename, c2) << "Detect cycle in inheritance graph."
                                           << endl;
            break;
        }
        seen.push_back(c2->name);
        Symbol parent = c2->parent;
        c = find_class_by_symbol(parent);
        if (!c) {
            semant_error(c2->filename, c2) << "Parent class not found. " << endl;
            break;
        }
        c2 = static_cast<ClassClass>(c);
    }
    // no cycle.
}


void ClassTable::check_inheritance_graph() {
    int n = check_classes -> len();
    for (int i = 0; i < n; i ++) {
        Class_ c = check_classes->nth(i);
        check_inheritance_graph(c);
    }
}

void ClassTable::check_class_semantic() {
    int n = check_classes -> len();
    for (int i = 0; i < n; i ++) {
        Class_ c = check_classes->nth(i);
        check_class_semantic(c);
    }
}

void ClassTable::check_class_semantic(Class_ c) {
    c->semant(this);
}

void ClassTable::check_class_pre_semantic() {
    int n = my_classes -> len();
    for (int i = 0; i < n; i ++) {
        Class_ c = my_classes->nth(i);
        check_class_pre_semantic(c);
    }
}

void ClassTable::check_class_pre_semantic(Class_ c) {
    c->pre_semant(this);
}

void class__class::pre_semant(ClassTable* ct) {
    ct->cc = this;

    // 1. check attr & method name duplicated or not
    // 2. collect all attrs & methods
    int n = features->len();
    for (int i=0; i < n; i++) {
        Feature f = features->nth(i);
        if (f->ftype == FT_ATTR) {
            AttrClass x = static_cast<AttrClass>(f);

            // if duplicated.
            AttrClass s = find_attr(x->name);
            if (s) {
                ct->semant_error(filename, x) << "Duplicate attr name: "
                                              << x->name << endl;
                continue;
            }

            if(x->name == self) {
                ct->semant_error(filename, x) << "Attr name == self"
                                              << endl;
                continue;
            }

            x->pre_semant(ct);
            attrs.push_back(x);

        } else if(f->ftype == FT_METHOD) {
            MethodClass x = static_cast<MethodClass>(f);

            // if duplicated.
            MethodClass s = find_method(x->name);
            if (s) {
                ct->semant_error(filename, x) << "Duplicate method name: " << x->name << endl;
                continue;
            }

            if (x->name == self) {
                ct->semant_error(filename, x) << "Method name == self" << endl;
            }

            x->pre_semant(ct);
            methods.push_back(x);
        }
    }
    // cerr << "attrs size = " << attrs.size() << ", methods size = " << methods.size() << ", name " << name << endl;
}

void class__class::semant(ClassTable* ct) {
    // cerr << "class__class::semant" << endl;

    ct->cc = this;

    // what's the inheritance graph.
    std::vector<ClassClass> chain;
    ClassClass c = ct->find_class_by_symbol(name);
    for(;;) {
        chain.push_back(c);
        if (c->parent == No_class) break;
        c = ct->find_class_by_symbol(c->parent);
    }
    // cerr << "chain size " << chain.size() << endl;


    // create scope.
    size_t chain_size = chain.size();
    for(int i = chain_size - 1 ; i >=0; i--) {
        ct->vtab->enterscope();
        ct->mtab->enterscope();
        ClassClass c = chain[i];
        // cerr << "Type " << c->name << ", attrs = " << c->attrs.size()
        // << ", methods = " << c->methods.size() << endl;
        for(size_t j = 0; j < c->attrs.size(); j ++){
            AttrClass v =c->attrs[j];
            // cerr << "adding v name " << v->name << ", type " << v->type_decl << ", v" << v << endl;

            if (i == 0) {
                AttrClass v2 = ct->vtab->lookup(v->name);
                if(v2) {
                    ct->semant_error(v) << "Attr redefined" << endl;
                }
            }
            ct->vtab->addid(v->name, v);
        }
        for(size_t j = 0; j < c->methods.size(); j++) {
            MethodClass m = c->methods[j];

            if (i == 0) {
                MethodClass m2 = ct->mtab->lookup(m->name);
                if (m2) {
                    if (m2->formals->len() != m ->formals->len()) {
                        ct->semant_error(m) << "Different numbber of paramaters" << endl;
                    } else {
                        for (int z = 0; z < m->formals->len(); z ++) {
                            FormalClass f0 = static_cast<FormalClass>(m->formals->nth(z));
                            FormalClass f1 = static_cast<FormalClass>(m2->formals->nth(z));
                            if (f0->type_decl != f1->type_decl) {
                                ct->semant_error(f0) << "Redefined Method type mismatches" << endl;
                            }
                        }
                    }
                }
            }

            ct->mtab->addid(m->name, m);
        }
    }

    // add "self"
    Feature f = attr(self, SELF_TYPE, no_expr());
    AttrClass v = static_cast<AttrClass>(f);
    ct->vtab->addid(self, v);

    int n = features->len();
    for (int i = 0; i < n; i++) {
        Feature f = features->nth(i);
        f->semant(ct);
    }

    // destroy scope.
    for (size_t i = 0; i < chain_size; i ++) {
        ct->vtab->exitscope();
        ct->mtab->exitscope();
    }
}

AttrClass class__class::find_attr(Symbol s) {
    for(size_t i = 0; i < attrs.size(); i ++) {
        AttrClass attr = attrs[i];
        if (attr->name == s) {
            return attr;
        }
    }
    return NULL;
}

MethodClass class__class::find_method(Symbol s) {
    for(size_t i = 0; i < methods.size(); i ++) {
        MethodClass method = methods[i];
        if (method->name == s) {
            return method;
        }
    }
    return NULL;
}

MethodClass ClassTable::find_method(ClassClass c, Symbol s) {
    MethodClass m = NULL;
    for(;;) {
        m = c->find_method(s);
        if (m) break;
        if(c->parent == No_class) break;
        c = find_class_by_symbol(c->parent);
    }
    return m;
}

void method_class::pre_semant(ClassTable* ct) {
    ClassClass c = ct->find_class_by_symbol(return_type);
    if (!c) {
        ct->semant_error(this) << "Method " << name << " return type " << return_type << " not found" << endl;
        return_type = Object;
    }
    int n = formals->len();
    std::vector<Symbol> seen;
    for (int i = 0; i < n; i++) {
        formal_class* f = static_cast<formal_class*>(formals->nth(i));
        if (f->name == self) {
            ct->semant_error(this) << "Formal name can not be self" << endl;
        }
        if (f->type_decl == SELF_TYPE) {
            ct->semant_error(this) << "Formal type can not be SELF_TYPE" << endl;
            f->type_decl = Object;
        }
        c = ct->find_class_by_symbol(f->type_decl);
        if (!c) {
            ct->semant_error(this) << "Method " << name << " arg " << f->name << " type " << f->type_decl << " not found" << endl;
            f->type_decl = Object;
        }
        for(size_t j = 0 ; j < seen.size(); j++) {
            if (seen[j] == f->name) {
                ct->semant_error(this) << "Method " << name << " arg " << f->name << " duplicated" << endl;
                break;
            }
        }
        seen.push_back(f->name);
    }
}

void formal_class::semant(ClassTable* ct) {
}

void method_class::semant(ClassTable* ct) {
    // note: formal and attr has same layout.
    ct->vtab->enterscope();
    int n = formals->len();
    for(int i = 0; i < n; i++) {
        formal_class* f = static_cast<formal_class*>(formals->nth(i));
        AttrClass v = (AttrClass)f;
        ct->vtab->addid(f->name, v);
    }
    expr->semant(ct);
    ct->vtab->exitscope();
    if(!ct->is_type_compatible(expr->get_type(), return_type)) {
        ct->semant_error(this) << "Type mismatches. Return type " << return_type
                               << ", expr type " << expr->get_type() << endl;
    }
}

void attr_class::pre_semant(ClassTable* ct) {
    ClassClass c = ct->find_class_by_symbol(type_decl);
    if(!c) {
        ct->semant_error(this) << "Attr " << name << " type decl " << type_decl
                               << " not found" << endl;
        type_decl = Object; // assign default type.
    }
}

void attr_class::semant(ClassTable* ct) {
    init->semant(ct);
    if (!ct->is_type_compatible(init->get_type(), type_decl)) {
        ct->semant_error(this) << "Type mismatches. Declare type " << type_decl
                               << ", expr type " << init->get_type() << endl;
    }
}

int ClassTable::is_type_compatible(Symbol sub, Symbol s) {
    if (sub == No_type) return 1; // no_expr
    if (sub == SELF_TYPE) {
        if (s == SELF_TYPE) return 1;
        else sub = cc->name;
    }
    if (sub == s) return 1; // symbols are the same.
    ClassClass c = find_class_by_symbol(sub);
    while(c->parent != No_class) {
        c = find_class_by_symbol(c->parent);
        if (c->name == s) return 1;
    }
    return 0;
}

void branch_class::semant(ClassTable* ct) {
    ClassClass c = ct->find_class_by_symbol(type_decl);
    if (!c) {
        ct->semant_error(this) << "Type not found " << type_decl << endl;
        type_decl = Object;
    }
    ct->vtab->enterscope();
    Feature f = attr(name, type_decl, no_expr());
    AttrClass v = static_cast<AttrClass>(f);
    ct->vtab->addid(name, v);
    expr->semant(ct);
    ct->vtab->exitscope();
}

void assign_class::semant(ClassTable* ct) {
    if (name == self) {
        ct->semant_error(this) << "Can not asisgn to self" << endl;
    }
    AttrClass v = (ct->vtab->lookup(name));
    if (!v) {
        ct->semant_error(this) << "Variable " << name << " not found" << endl;
        set_type(Object);
    } else {
        // cerr << "type = " << v << endl;
        set_type(v -> type_decl);
    }
    Symbol my_type = get_type();
    expr->semant(ct);
    if (!ct->is_type_compatible(expr->get_type(), my_type)) {
        ct->semant_error(this) << "Type mismatches. Variable name " << name << ", type " << my_type
                               << ", expr type " << expr->get_type() << endl;
    }
}

void static_dispatch_class::semant(ClassTable* ct) {
    expr->semant(ct);

    ClassClass c = ct->find_class_by_symbol(type_name);
    if (!c) {
        ct->semant_error(this) << "Type " << type_name << "not found" << endl;
    }

    if (!ct->is_type_compatible(expr->get_type(), type_name)) {
        ct->semant_error(this) << "Type cast error, from " << expr->get_type()
                               <<", to " << type_name << endl;
    }

    MethodClass m = NULL;
    if (c) {
        m = ct->find_method(c, name);
        if(!m) {
            ct->semant_error(this) << "Method " << name << " not found in type "
                                   << type_name << endl;
        }
    }

    if (m) {
        Symbol ret_type = m->return_type;
        if(ret_type == SELF_TYPE) {
            if (expr->get_type() == Str ||
                expr->get_type() == Int ||
                expr->get_type() == Bool) {
                ret_type = expr->get_type();
            } else {
                ret_type = expr->get_type();
            }
        }
        set_type(ret_type);
        int n = actual->len();
        int n2 = m->formals->len();
        if (n != n2) {
            ct->semant_error(this) << "Number of arguments " << n << " mismatches "
                                   << " of formals " << n2 << endl;
        } else {
            for(int i = 0; i < n; i ++) {
                Expression e = actual->nth(i);
                e->semant(ct);
            }
            for(int i = 0; i < n; i ++) {
                FormalClass f = static_cast<FormalClass>(m->formals->nth(i));
                Expression e = actual->nth(i);
                if(!ct->is_type_compatible(e->get_type(), f->type_decl)) {
                    ct->semant_error(this) << "Type mismatches, param type "
                                           << f->type_decl << ", arg type "
                                           << e->get_type() << endl;
                }
            }
        }
    } else {
        set_type(Object);
    }
}

void dispatch_class::semant(ClassTable* ct) {
    expr->semant(ct);

    ClassClass c = ct->find_class_by_symbol(expr->get_type());
    if (!c) {
        ct->semant_error(this) << "Type " << type_name << "not found" << endl;
    }

    MethodClass m = NULL;
    if (c) {
        m = ct->find_method(c, name);
        if(!m) {
            ct->semant_error(this) << "Method " << name << " not found in type "
                                   << c->name << endl;
        }
    }

    int n = actual->len();
    for(int i = 0; i < n; i ++) {
        Expression e = actual->nth(i);
        e->semant(ct);
    }

    if (m) {
        Symbol ret_type = m->return_type;
        if(ret_type == SELF_TYPE) {
            if (expr->get_type() == Str ||
                expr->get_type() == Int ||
                expr->get_type() == Bool) {
                ret_type = expr->get_type();
            } else {
                ret_type = expr->get_type();
            }
        }
        set_type(ret_type);
        int n = actual->len();
        int n2 = m->formals->len();
        if (n != n2) {
            ct->semant_error(this) << "Number of arguments " << n << " mismatches "
                                   << " of formals " << n2 << endl;
        } else {
            for(int i = 0; i < n; i ++) {
                FormalClass f = static_cast<FormalClass>(m->formals->nth(i));
                Expression e = actual->nth(i);
                if(!ct->is_type_compatible(e->get_type(), f->type_decl)) {
                    ct->semant_error(this) << "Type mismatches, param type "
                                           << f->type_decl << ", arg type "
                                           << e->get_type() << endl;
                }
            }
        }
    } else {
        set_type(Object);
    }
}

void cond_class::semant(ClassTable* ct) {
    pred->semant(ct);
    if(pred->get_type() != Bool) {
        ct->semant_error(this) << "Predicate wrong type " << pred->get_type()
                               << endl;
    }
    then_exp->semant(ct);
    else_exp->semant(ct);
    Symbol s = ct->type_lub(then_exp->get_type(), else_exp->get_type());
    set_type(s);
}

void loop_class::semant(ClassTable* ct) {
    pred->semant(ct);
    if(pred->get_type() != Bool) {
        ct->semant_error(this) << "Predicate wrong type " << pred->get_type()
                               << endl;
    }
    body->semant(ct);
    set_type(Object);
}

void typcase_class::semant(ClassTable* ct) {
    expr->semant(ct);
    int n = cases->len();
    Symbol ret_type = NULL;
    std::vector<Symbol> seen;
    for(int i = 0; i < n; i++) {
        Case c = cases->nth(i);
        c->semant(ct);
        BranchClass c2 = static_cast<BranchClass>(c);
        // if(!ct->is_type_compatible(c2->type_decl, expr->get_type())) {
        //     ct->semant_error(this) << "Type mismatches. branch# " << i << " type "
        //                            << c2->type_decl << ", expr type "
        //                            << expr->get_type() << endl;
        // }
        for(size_t j = 0; j < seen.size(); j ++) {
            if (seen[j] == c2->type_decl) {
                ct->semant_error(this) << "Duplicated branch " << c2->type_decl << endl;
            }
        }
        seen.push_back(c2->type_decl);
        if(ret_type) {
            ret_type = ct->type_lub(ret_type, c2->expr->get_type());
        } else {
            ret_type = c2->expr->get_type();
        }
    }
    set_type(ret_type);
}

void block_class::semant(ClassTable* ct) {
    ct->vtab->enterscope();
    Symbol ret_type = NULL;
    int n = body->len();
    for(int i = 0; i < n; i++) {
        Expression e = body->nth(i);
        e->semant(ct);
        ret_type = e->get_type();
    }
    ct->vtab->exitscope();
    set_type(ret_type);
}

void let_class::semant(ClassTable* ct) {
    if (identifier == self) {
        ct->semant_error(this) << "Let identifier == self" << endl;
    }
    ClassClass c = ct->find_class_by_symbol(type_decl);
    Symbol s = type_decl;
    if (!c) {
        ct->semant_error(this) << "Type " << type_decl << " not found" << endl;
        s = Object;
    }
    init->semant(ct);
    // cerr << "init->get_type() = " << init->get_type() << ", s = " << s << endl;
    if (!ct->is_type_compatible(init->get_type(), s)) {
        ct->semant_error(this) << "Type mismatches" << endl;
    }
    Feature f = attr(identifier, type_decl, init);
    AttrClass attr = static_cast<AttrClass>(f);
    ct->vtab->enterscope();
    ct->vtab->addid(identifier, attr);
    body->semant(ct);
    ct->vtab->exitscope();
    set_type(body->get_type());
}

#define MUST_INT(e) do {                                    \
        if(e->get_type() != Int) {                          \
            ct->semant_error(this) << "Type is not int" << endl; \
        }                                                   \
    } while(0)

#define OP_CLASS_SEMANT(op, ret)                \
    void op::semant(ClassTable* ct) {           \
    e1->semant(ct);                             \
    e2->semant(ct);                             \
    MUST_INT(e1);                               \
    MUST_INT(e2);                               \
    set_type(ret);                              \
    }

OP_CLASS_SEMANT(plus_class, Int)
OP_CLASS_SEMANT(sub_class, Int)
OP_CLASS_SEMANT(mul_class, Int)
OP_CLASS_SEMANT(divide_class, Int)
OP_CLASS_SEMANT(lt_class, Bool)
OP_CLASS_SEMANT(leq_class, Bool)

void neg_class::semant(ClassTable* ct) {
    e1->semant(ct);
    MUST_INT(e1);
    set_type(Int);
}

void eq_class::semant(ClassTable* ct) {
    e1->semant(ct);
    e2->semant(ct);
    Symbol t1 = e1->get_type();
    Symbol t2 = e2->get_type();
    if (t1 == Int || t1 == Bool || t1 == Str || \
        t2 == Int || t2 == Bool || t2 == Str)  {
        if(t1 != t2) {
            ct->semant_error(this) << "Type mismatches: " << t1 << ", " << t2 << endl;
        }
    }
    set_type(Bool);
}

void comp_class::semant(ClassTable* ct) {
    e1->semant(ct);
    if(e1->get_type() != Bool) {
        ct->semant_error(this) << "Type not bool" << endl;
    }
    set_type(Bool);
}

void int_const_class::semant(ClassTable* ct) {
    set_type(Int);
}

void bool_const_class::semant(ClassTable* ct) {
    set_type(Bool);
}

void string_const_class::semant(ClassTable* ct) {
    set_type(Str);
}

void new__class::semant(ClassTable* ct) {
    ClassClass c = ct->find_class_by_symbol(type_name);
    if(c) {
        set_type(type_name);
    } else {
        ct->semant_error(this) << "Type not found " << type_name << endl;
        set_type(Object);
    }
}

void isvoid_class::semant(ClassTable* ct) {
    e1->semant(ct);
    set_type(Bool);
}

void no_expr_class::semant(ClassTable* ct) {
    set_type(No_type);
}

void object_class::semant(ClassTable* ct)  {
    AttrClass v = ct->vtab->lookup(name);
    if (v) {
        set_type(v->type_decl);
    } else {
        ct->semant_error(this) << "Object not found. " << name << endl;
        set_type(Object);
    }
}


Symbol ClassTable::type_lub(Symbol a, Symbol b) {
    ClassClass x = find_class_by_symbol(a);
    ClassClass y = find_class_by_symbol(b);
    if(!x || !y) return Object;
    while(y->parent != No_class) {
        ClassClass tmp = x;
        while(tmp->parent != No_class) {
            if(tmp->name == y->name) {
                // cerr << "Type lub(" << a << ", " << b << ") = " << tmp->name << endl;
                return tmp->name;
            }
            tmp = find_class_by_symbol(tmp->parent);
        }
        y = find_class_by_symbol(y->parent);
    }
    return Object;
}
