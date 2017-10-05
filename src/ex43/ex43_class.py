from sys import exit
from random import randint
class Game(object):
    def __init__(self, start):
        self.results=["老哥，你死了 ","俺们会悼念你的！",
                      "卧槽，怪物把你吃了",
                      "老铁，下次再来吧！"]

        self.start=start

    def play(self):
        next=self.start

        while True:
            print("\n--------")

            room=getattr(self,next)
            next=room()

    def death(self):
        print(self.results[randint(0,len(self.results)-1)])
        exit(1)

    def central_corridor(self):
        print("你的探险小队在森林中收到了袭击，其他的队员都与你失散了。")
        print("你醒来后发现你在一个墓穴中，只有前方有个通道。")
        print("你来到了中央通道，迎面走来一个三眼怪物。现在你的身上只有一把枪和一柄匕首。")
        print("现在，你需要想想你该做什么...")
        action=input("> 1. 开枪射击 2.用匕首跟怪物拼了 3.问怪物点问题. \n 请输入数字")

        if action== "1":
            print("你开了枪，射到了怪物的脑袋上，但是子弹穿不透怪物的皮肤。")
            print("怪物很生气，向你跑了过来")
            return 'death'
        elif action=="2":
            print("这个部分一会儿再写....")
            return 'death'
        else:
            return 'success'
    def success(self):
        print("you win!")
        print("\n")