# 简易两数计算器 Python入门小项目
# 功能：输入两个数字，实现加减乘除
if __name__ == "__main__":
    print("=====极简计算器=====")
    # 输入数字，input接收字符串，转浮点型
    num1 = float(input("请输入第一个数字："))
    op = input("请输入运算符(+ - * /)：")
    num2 = float(input("请输入第二个数字："))

    # 判断运算，和C语言if-else逻辑一致
    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        # 避免除0报错
        if num2 == 0:
            print("错误：除数不能为0")
            exit()
        res = num1 / num2
    else:
        print("运算符输入错误")
        exit()
    # 输出结果
    print(f"计算结果：{num1} {op} {num2} = {res}")