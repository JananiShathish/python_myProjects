def reverseString(sen):
    print(sen)
    str_len=len(sen)
    print(str_len)
    # sen=''.join(reversed(sen))
    # print(sen)st
    st=''
    print(type(st))
    for i in sen:
        st=i+st
    print(st)    


reverseString('Iam a Good Girl')    