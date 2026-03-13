# def add():
#     a=int(input("Enter number: "))
#     b=int(input("Enter number: "))
#     res=a+b
#     print(res)
# if __name__ == '__main__':
#    add()

#Fuction with Parameter with No return Value
# def add(x,y):
#     res=a+b
#     print(res)
# if __name__ == '__main__':
#    a=int(input("Enter number: "))
#    b=int(input("Enter number: "))
#    add(a,b)

   #Fuction with Parameter with Return Value

def add(x,y):
    res=x+y
    return res
if __name__ == '__main__':
   a=int(input("Enter number: "))
   b=int(input("Enter number: "))
   res=add(a,b)
   print(res)


def add(x,y):
    res1=x+y
    res2=x*y
    res3=x-y
    return res1,res2,res3
if __name__ == '__main__':
   a=int(input("Enter number: "))
   b=int(input("Enter number: "))
   res=add(a,b)
   print(res)


