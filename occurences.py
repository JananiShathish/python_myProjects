# def occurances(occ):
#     occ=occ.upper()
#     print(occ)
#     count=0
#     charat='A'
#     for i in occ:
#         if (i == charat):
#             count+=1
#     print(count)        



# occurances('Janani')    


def occurancesEach(occ):
    occDict={}
    occ=occ.upper()
    for i in occ:
        if(i not in occDict):
            occDict[i]=1
        else:
            c=occDict[i]
            occDict[i]=c+1
    print(occDict)
occurancesEach('jananiShathish Jalana Pattabiraman')    