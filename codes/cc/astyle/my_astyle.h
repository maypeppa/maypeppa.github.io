/*
 * Copyright (C) dirlt
 */

#ifndef __CC_ASTYLE_MYASTYLE_H__
#define __CC_ASTYLE_MYASTYLE_H__

#include <string>
#include <cstdlib>
#include <cstdio>
#include <cerrno>

#define SERRNO (strerror(errno))
#define SERRNO2(n) (strerror(n))
#define DEBUG(fmt, ...) fprintf(stderr, "[DEBUG]"fmt"\n",  ##__VA_ARGS__)
#define NOTICE(fmt, ...) fprintf(stderr, "[NOTICE]"fmt"\n",  ##__VA_ARGS__)
#define TRACE(fmt, ...) fprintf(stderr, "[TRACE]"fmt"\n",  ##__VA_ARGS__)
#define WARNING(fmt, ...) fprintf(stderr, "[WARNING]"fmt"\n", ##__VA_ARGS__)
#define FATAL(fmt, ...) fprintf(stderr, "[FATAL]"fmt"\n", ##__VA_ARGS__)

namespace astyle {

extern const char* kDefaultOptions;
const std::string my_astyle(const char* src,
                            const char* options = kDefaultOptions);

} // namespace astyle

#endif // __CC_ASTYLE_MYASTYLE_H__
