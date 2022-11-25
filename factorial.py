# def factorial(n):
#     c=1
#     for i in range(1,n+1):
#         print(i)
#         b=i*c
#         c=b
#     print(c)
# factorial(5)


#Recursive fnuction for finding Factorial
def factorial(n):
    if(n<=1):
        return n
    else:
        return( n* factorial(n-1)   )
a=factorial(5)         
print(a)