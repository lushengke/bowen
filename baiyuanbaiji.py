# ！/usr/bin/python
# -*-coding:utf-8-*-

# 用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
for x in range(101):
    for y in range(101):
        for z in range(101):
            if 2*x + y + 0.5*z == 100 and x+y+z == 100:
                print(x,y,z)