
def function_while(n, m):
    i = 0
    numbers = []
    while i < n:
        print("The top i is: %d" % i)
        numbers.append(i)
        print("The numbers is:", numbers)
        i += m
        print("The bottom i is: %d" % i)
    for num in numbers:
            print(num)

function_while(5,2)

numbers2 = []
for i in range(0,6):
    print("At the top i is: %d" % i)
    numbers2.append(i)
    print("Numbers now:", numbers2)
