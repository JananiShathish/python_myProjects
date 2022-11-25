def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))    


        
terms=int(input("Enter the no of terms"))
if terms<=0:
    print("Enter valid terms")
else:
    for i in range(terms):
        print(fib(i))
    # print(fibbi)

        


  