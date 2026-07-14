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

#今日新增1：修改学生成绩
def modify_score():
    name=input("请输入要修改成绩学生的名字：")
    if name not in students_data:
        print("未查询到该学生信息！")
        return
    try:
        new_score=int(input("请输入新的分数："))
        if 0<=new_score<=100:
            students_data[name]=new_score
            print("分数修改完成！")
            return
        else:
            print("请输入0~100之间的分数！")
    except ValueError:
        print("分数必须是整数")


#今日新增2：删除学生
def del_student():
    name=input("请输入要删除学生的姓名：")
    if name in students_data:
        del_student()
        print("该学生信息已删除！")
    else:
        print("未查询到该学生的信息")



#今日新增3：展示全部学生
def show_all():
    if len(students_data)==0:
        print("暂无任何学生信息")
        return
    else:
        print("=====全部学生信息=====")
        for name,score in students_data.items():
            print(f"姓名：{name}，成绩：{score}")


#程序主菜单
def main():

    print("======学生成绩管理系统======")
    while True:
        print("输入1录入信息 2查询成绩 3退出程序 4修改信息 5删除学生 6查看所有信息\n")
        choose=int(input("请选择您的需求："))
        if choose==1:
            add_students()
        elif choose==2:
            search_studentd()
        elif choose==3:
            print("程序退出！")
            return
        elif choose==4:
            modify_score()
        elif choose==5:
            del_student()
        elif choose==6:
            show_all()
        else:
            print("该输入无效，请重新输入：")

#启动程序
if __name__=="__main__":
    main()
