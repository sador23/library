x=[x for x in range(0,10) if x%2==0]
print(x)




def pyramid(number):
    number=int(number/2)
    for i in range(-number,number):
        print(" "*abs(i)+"a")


pyramid(10)