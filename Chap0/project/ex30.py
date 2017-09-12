# -*- coding: utf-8 -*-
people = 40
cars = 40
buses = 60

#如果cars大于people,执行第一个print,如果小于执行第二个print，如果1，2个条件不满足，那么执行最后一个print
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take a buses")
else:
    print("We still can't dicede")

#只有两大类条件，一个类是people大于buses，另一类是“除第一个条件以外的任何”
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
