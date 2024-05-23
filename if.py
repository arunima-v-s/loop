# if condition
a=-1
if a>0:
    print("true")


# if-else condition

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")


# elif condition

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("both are equal")
# else:
#     print("b is greater than a")



# a=int(input("enter your age"))
# if a>=25:
#     print("you can vote and able to candidate")
# elif a>=18:
#     print("you can vote and not able to candidate")
# else:
#     print("no vote")



# a=int(input("enter mark"))
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("fail")


# elif condition-logical operators

# a=int(input("enter mark"))
# if a>90 and a<=100:
#     print("A")
# elif a>80 and a<=90:
#     print("B")
# elif a>70 and a<=60:
#     print("C")
# elif a>60 and a<=50:
#     print("D")
# else:
#     print("fail")


# a=int(input("enter year"))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("a is a leap year")
# else:
#     print("a is not a leap year")


# a=int(input("enter a number"))
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")



# for-loop

# a=[1,2,3,4,5,6]
# print(a)
# for i in a:
#     print(i)

# for i in range(1,11,2):
#     print(i)


# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2==1:
#         print(i)


# a=int(input("enter a number"))
# b=int(input("enter the limit"))
# for i in range(1,b):
#     c=i*a
#     print(f"{a}*{i}={c}")


# d=int(input("enter the limit"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,d):
#     c=a+b
#     a=b
#     b=c
#     print(c)



# x=input("enter data")
# d=0
# a=0
# for i in x:
#     if i.isdigit():
#        d=d+1
#     elif i.isalpha():
#         a=a+1
#     else:
#         pass
# print(a)
# print(d)


n=int(input("enter limit"))
factorial=1
if n<0:
    print("no factorial")
elif n==0 or n==1:
    print("factorial is 1")
else:
    for i in range(2,n+1):
        factorial=factorial*i
    print(factorial)