def insertion_sort(arr1):
    for i in range(1,len(arr1)):
        j=i
        while (j>0 and arr1[j-1]>arr1[j]):
            arr1[j],arr1[j-1]=arr1[j-1],arr1[j]
            print('in while loop',arr1)
            j-=1
        print('in for loop',arr1)    
    print('outside final',arr1)
insertion_sort([2,1,7,6,4,12,9,8])    