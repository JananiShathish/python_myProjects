def noVowels(sent):
    vowel=['a','e','i','o','u']
    sent=sent.lower()
    vowelcount=0
    concount=0
    for i in sent:
        if i in vowel:
            vowelcount=vowelcount+1
        else:
            if i !=' ':
                concount=concount+1    
    print('vowelCount:',vowelcount,'constcount: ',concount)        

noVowels('I like to be a good human')    