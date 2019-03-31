/* -*- c -*-
 *  The scanner definition for COOL.
 */

/*
 *  Stuff enclosed in %{ %} in the first section is copied verbatim to the
 *  output, so headers and global definitions are placed here to be visible
 * to the code in the file.  Don't remove anything that was here initially
 */
%{
#include <cool-parse.h>
#include <stringtab.h>
#include <utilities.h>

/* The compiler assumes these identifiers. */
#define yylval cool_yylval
#define yylex  cool_yylex

/* Max size of string constants */
#define MAX_STR_CONST 1025
#define YY_NO_UNPUT   /* keep g++ happy */

extern FILE *fin; /* we read from this file */

/* define YY_INPUT so we read from the FILE fin:
 * This change makes it possible to use this scanner in
 * the Cool compiler.
 */
#undef YY_INPUT
#define YY_INPUT(buf,result,max_size) \
	if ( (result = fread( (char*)buf, sizeof(char), max_size, fin)) < 0) \
		YY_FATAL_ERROR( "read() in flex scanner failed");

char string_buf[MAX_STR_CONST]; /* to assemble string constants */
char *string_buf_ptr;

extern int curr_lineno;
extern int verbose_flag;

extern YYSTYPE cool_yylval;

const char* string_tolower(const char* s) {
    char* s2 = strdup(s);
    for(int i = 0; s[i]; i++){
      s2[i] = tolower(s[i]);
    }
    return s2;
}

const char* keywords[] = {
  "class", "else", "fi", "if", "in", "inherits",
  "let", "isvoid", "loop", "pool", "then", "while",
  "case", "esac", "new", "of", "not", NULL
};

int keyword_tokens[] = {
  CLASS, ELSE, FI, IF, IN, INHERITS,
  LET, ISVOID, LOOP, POOL, THEN, WHILE,
  CASE, ESAC, NEW, OF, NOT, 0
};

/*
 *  Add Your own definitions here
 */

%}

/*
 * Define names for regular expressions here.
 */

ASSIGN          <-
DARROW          =>
LE              <=
DIGIT [0-9]
LETTER [a-zA-Z_]
LETTER2 [a-zA-Z]
WS [ \n\f\r\t\v]
LINE_COMMENT --
BEGIN_COMMENT \(\*
END_COMMENT \*\)

%%

{WS}+ {
    for(int i = 0; yytext[i]; i++) {
        if (yytext[i] == '\n') {
            curr_lineno += 1;
        }
    }
}

 /*
  *  Nested comments
  */

{LINE_COMMENT} {
    // printf("+++++ discard line comment\n");
    int c = 0;
    while((c = yyinput()) != EOF) {
        if (c == '\n') break;
    }
    curr_lineno += 1;
}

{BEGIN_COMMENT} {
  int c = 0;
  int nest = 1;
  // printf("+++++ discard block comment\n");
  while((c = yyinput()) != EOF) {
   if(c == '*') {
      int c2 = yyinput();
      if (c2 == ')') {
          nest -= 1;
          if (nest == 0) {
              // BEGIN(INITIAL);
              break;
          }
      } else {
         unput(c2);
      }
   } else if (c == '(') {
      int c2 = yyinput();
      if (c2 == '*') {
          nest += 1;
      } else {
          unput(c2);
      }
   } else {
       // putchar(c);
       if (c == '\n') {
           curr_lineno += 1;
       }
   }
  }

  if (c == EOF) {
      // unexpected EOF.
      cool_yylval.error_msg = "EOF in comment";
      return ERROR;
  }
}

{END_COMMENT} {
    cool_yylval.error_msg = "Unmatched *)";
    return ERROR;
}

 /*
  *  The multiple-character operators.
  */

{ASSIGN}                { return (ASSIGN); }
{DARROW}		{ return (DARROW); }
{LE}                    { return (LE); }

 /*
  * Keywords are case-insensitive except for the values true and false,
  * which must begin with a lower-case letter.
  */

{DIGIT}+ {
    Symbol s = stringtable.add_string(yytext);
    cool_yylval.symbol = s;
    return INT_CONST;
}

{LETTER2}({LETTER}|{DIGIT})* {
  const char* s = yytext;
  const char* s2 = string_tolower(s);
  int token = 0;

  if (s[0] == '_' and s[1] == '\0') {
      REJECT;
  }

  for(int i = 0; keywords[i]; i++) {
     if (strcmp(s2, keywords[i]) == 0) {
       token = keyword_tokens[i];
       break;
     }
  }

  if (!token) {
      if (strcmp(s2, "true") == 0 && s[0] == 't') {
          token = BOOL_CONST;
          cool_yylval.boolean = 1;
      } else if (strcmp(s2, "false") == 0 && s[0] == 'f') {
          token = BOOL_CONST;
          cool_yylval.boolean = 0;
      }
  }

  if (!token) {
      if (isupper(s[0])) {
          token = TYPEID;
      } else {
          token = OBJECTID;
      }
      Symbol sym = stringtable.add_string(yytext);
      cool_yylval.symbol = sym;

  }
  free((void*)s2);
  return token;
}

 /*
  *  String constants (C syntax)
  *  Escape sequence \c is accepted for all characters c. Except for
  *  \n \t \b \f, the result is c.
  *
  */

\" {
    int c = 0;
    int p = 0;
    int overflow = 0;
    int null_char = 0;
    int newline_char = 0;
    while((c = yyinput()) != EOF) {
        if (c == '\\') {
            int c2 = yyinput();
            if (c2 != EOF) {
                // escape this character.
                if (c2 == 'b') c2 = '\b';
                else if (c2 == 't') c2 = '\t';
                else if (c2 == 'n') c2 = '\n';
                else if (c2 == 'f') c2 = '\f';
                else if (c2 == '\0') {
                    null_char = 1;
                }
                string_buf[p] = (char) c2;
                p += 1;
                if (p == MAX_STR_CONST) {
                    // mark it, but keep going.
                    overflow = 1;
                    p -= 1;
                }
            } else {
                unput(c2);
            }
        } else if (c == '\0') {
            // skip this character.
            null_char = 1;
        } else if (c == '\n' || c == '"') {
            break;
        }else {
            string_buf[p] = (char) c;
            p += 1;
            if (p == MAX_STR_CONST) {
                overflow = 1;
                p -= 1;
            }
        }
    }

    if (c == EOF) {
        cool_yylval.error_msg = "EOF in string constant";
        return ERROR;
    }

    if (c == '\n') {
        curr_lineno += 1;
        cool_yylval.error_msg = "Unterminated string constant";
        return ERROR;
    }

    if (null_char) {
        cool_yylval.error_msg = "String contains null character";
        return ERROR;
    }

    if (overflow) {
        cool_yylval.error_msg = "String constant too long";
        return ERROR;
    }

    string_buf[p] = '\0';
    Symbol s = stringtable.add_string(string_buf);
    cool_yylval.symbol = s;
    return STR_CONST;
}

[{}@+\-*/<=();:\.~,] { return yytext[0]; }

. {
    /* unknown character */
    cool_yylval.error_msg = yytext;
    return ERROR;
}

%%
