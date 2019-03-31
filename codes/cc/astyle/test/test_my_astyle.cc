/*
 * Copyright (C) dirlt
 */

#include <string>
#include "astyle/my_astyle.h"

static const char* nasty_code = "int main(){\nprintf(\"hello,world\");\nreturn 0;\n}\n";

int main() {
  std::string s = astyle::my_astyle(nasty_code);
  printf("--------------------\n%s\n--------------------\n", s.c_str());
  return 0;
}
