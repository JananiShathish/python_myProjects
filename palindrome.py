def palindrome(st):
    st1=''.join((reversed(st)))
    print(st1)
    if(st == st1):
        print("Its a palindrome")
    else:
        print('Not a palindrome')    

palindrome('sir')    