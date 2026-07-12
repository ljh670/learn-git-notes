import random
answer=random.randint(1,100)
count=0
max_time=7
print("欢迎来到猜字游戏！数字范围1~100，在7次以内猜中数字获胜哦！！")

while count<max_time:
    try:
        num=int(input("请输入您猜的数字："))
        count+=1
        if num<1 or num>100:
            print("请输入1~100之间的数字！")
            continue
        if num<answer:
            print("猜小了")
        elif num>answer:
            print("猜大了")
        else:
            print(f"恭喜您，猜中啦！您总共猜了{count}次")
            break
    except ValueError:
        print("只能输入整数哦~")
else:
    print(f"很遗憾机会用完了，正确答案是{answer}")



