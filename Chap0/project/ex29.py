# -*- coding: utf-8 -*-
people = 50
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

#if对下一行代码是个关卡
#下一行需要4个空格缩进，规矩
#不缩进会报错

if people == dogs and people < cats:
    print("People are dogs, and they less than cats.")
