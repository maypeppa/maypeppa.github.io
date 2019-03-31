#ifndef SEMANT_H_
#define SEMANT_H_

#include <assert.h>
#include <iostream>
#include "cool-tree.h"
#include "stringtab.h"
#include "symtab.h"
#include "list.h"
#include <vector>

#define TRUE 1
#define FALSE 0

// This is a structure that may be used to contain the semantic
// information such as the inheritance graph.  You may use it or not as
// you like: it is only here to provide a container for the supplied
// methods.

typedef SymbolTable<Symbol, attr_class> AttrClassTable;
typedef SymbolTable<Symbol, method_class> MethodClassTable;

class ClassTable {
  public:
  int semant_errors;
  void install_basic_classes();
  ostream& error_stream;
    Classes builtin_classes;
    Classes my_classes;
    Classes check_classes;
    AttrClassTable* vtab;
    MethodClassTable * mtab;
    ClassClass cc;
public:
  ClassTable(Classes);
    int errors() { return semant_errors; }
    ClassClass find_class_by_symbol(Symbol sym);
    void check_inheritance_graph();
    void check_inheritance_graph(Class_ c);
    void check_class_semantic(Class_ c);
    void check_class_semantic();
    void check_class_pre_semantic();
    void check_class_pre_semantic(Class_ c);
    ostream& semant_error();
    ostream& semant_error(tree_node* t);
    ostream& semant_error(Symbol filename, tree_node *t);
    int is_type_compatible(Symbol sub, Symbol s);
    MethodClass find_method(ClassClass c, Symbol s);
    Symbol type_lub(Symbol a, Symbol b);
};


#endif
