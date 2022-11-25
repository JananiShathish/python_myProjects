def anagram(str1,str2):
    if (len(str1) != len(str2)):
        print('not a anagram')
    else:
        if (sorted(str1)==sorted(str2)):
            print('Anagram')
        else:
            print('Not a Anagram')    

anagram('care','rate')    