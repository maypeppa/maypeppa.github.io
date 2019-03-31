# http://astyle.sourceforge.net/astyle.html
# please consider changing to clang-format.

# 一些不要使用的选项
# --indent-cases // case后面内容多一次缩进,但是会让case部分{}存在问题.
# --indent-namespaces // 会让namespace下面内容多一个层缩进.
# --indent-classes // 虽然能够让public:,private:产生所缩进,但是造成函数出现两次缩进.
# --break-blocks // 在{}之后断开一行.看上去很好,但是不太合适.
# --delete-empty-lines // 删除函数内不必要空行.看上去很好,但是不太合适.

# 一些可以使用的选项
# --suffix=none // 不进行任何备份.
# --style=java // 基本风格使用java style.
# --brackets=attach // 括号附着在函数和条件表达式之后.
# --indent-switches // switch里面case进行缩进.
# --indent-labels // label进行缩进.
# --indent-preprocessor // 预处理换行使用缩进.
# --indent-col1-comments // 注释进行缩进.
# --add-brackets // 条件表达语句都加上{}
# --convert-tabs // 转换tab成为空格
# --lineend=linux // 换行转换成为\n
# --align-pointer=type // *和&都偏向类型.
# --pad-oper // 在运算符附近加上空格

astyle --suffix=none --style=java --indent=spaces=4 --brackets=attach \
    --indent-switches --indent-labels --indent-preprocessor --indent-col1-comments \
    --convert-tabs --verbose --lineend=linux --align-pointer=type --pad-oper $@
