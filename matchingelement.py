def matching(arr):
    tot=len(arr)
    for i in range(tot):
        for j in range((i+1),tot,1):
            if(arr[i]==arr[j]):
                print(arr[i],'at',i, 'and', arr[j],'at',j,'are same')

matching([1,2,3,4,5,1,2,6,7])