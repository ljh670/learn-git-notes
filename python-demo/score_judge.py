score=int(input("请输入您的分数："))

if score<0:
    print("分数不合法，程序结束")
elif score>=90:
    print("等级：优秀")
elif score>=80:
    print("等级：良好")
elif score>=60:
    print("等级：及格")
else:
    print("等级：不及格")