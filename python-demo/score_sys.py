#存储所有学生数据
students_data={}

#录入学生函数
def add_students():
    try:
        while True:
            name=input("请输入学生的姓名：")
            if name in students_data:
                print("该学生已存在")
                return

            score=int(input("请输入学生的成绩："))
            if 0<=score<=100:
                students_data[name]=score

                print("录入成功！")
                return
            else:
                print("请输入0~100的分数，本次输入无效，请重新输入：")
    except ValueError:
        print("分数必须是数字")


#查询学生函数
def search_studentd():
    name=input("请输入要查询学生的名字：")
    if name in students_data:
        print(f"{name}的成绩是{students_data[name]}分")
    else:
        print("该数据不存在，请重新输入")
        return


#程序主菜单
def main():

    print("======学生成绩管理系统======")
    while True:
        print("输入1录入信息 2查询成绩 3退出程序\n")
        choose=int(input("请选择您的需求："))
        if choose==1:
            add_students()
        elif choose==2:
            search_studentd()
        elif choose==3:
            print("程序退出！")
            return
        else:
            print("该输入无效，请重新输入：")

#启动程序
if __name__=="__main__":
    main()
