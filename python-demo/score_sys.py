import os
#保存数据的文件路径
FILE_NAME="student.txt"

#存储所有学生数据
students_data={}

#程序启动：读取文件加载历史数据
def load_data():
   global students_data
   #判断文件是否存在
   if not os.path.exists(FILE_NAME):
       return
   #读取文件:
   with open(FILE_NAME,"r",encoding="utf-8")as f:
       lines=f.readlines()
       for line in lines:
           line=line.strip()
           if line=="":
               continue
           name,score=line.split(",")
           students_data[name]=float(score);#可以兼容小数分数存储读取
               

#程序启动：保存数据到文件
def save_data():
    with open(FILE_NAME,"w",encoding="utf-8")as f:
        for name,score in students_data.items():
            f.write(f"{name},{score}\n")
    

#录入学生函数
def add_students():
    try:
        while True:
            name=input("请输入学生的姓名：")
            if name in students_data:
                print("该学生已存在")
                return

            score=float(input("请输入学生的成绩："))
            if 0<=score<=100:
                students_data[name]=score

                print("录入成功！")
                return
            else:
                print("请输入0~100的分数，本次输入无效，请重新输入：")
    except ValueError:
        print("分数必须是数字")


#查询学生函数
def search_student():
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
        new_score=float(input("请输入新的分数："))
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
        del students_data[name]
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


#班级成绩统计：
def stat_score():
    if len(students_data)==0:
        print("暂无任何学生成绩，无法统计！")
        return
    score_list=list(students_data.values())
    avg=sum(score_list)/len(score_list)
    max_s=max(score_list)
    min_s=min(score_list)
    print("=====班级成绩统计=====")
    print(f"学生总人数：{len(score_list)}")
    print(f"平均分：{avg:.2f}")
    print(f"最高分：{max_s}")
    print(f"最低分：{min_s}")


#程序主菜单
def main():

    #启动加载文件数据：
    load_data()

    print("======学生成绩管理系统======")
    while True:
        print("输入1录入信息 2查询成绩 3修改信息 4删除学生 5查看所有信息 6成绩统计 0退出程序\n")
        choose=int(input("请选择您的需求："))
        if choose==1:
            add_students()
        elif choose==2:
            search_student()
        elif choose==3:
            modify_score()
        elif choose==4:
            del_student()
        elif choose==5:
            show_all()
        elif choose==6:
            stat_score()
        elif choose == 0:
            #退出前保存数据
            save_data()
            print("数据已保存，程序退出！！")
            break
        else:
            print("该输入无效，请重新输入：")

#启动程序
if __name__=="__main__":
    main()
