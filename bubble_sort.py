def bubbleSort(arr1):
    for j in range(len(arr1)):
        for i in range(len(arr1)-1):
     
            print(arr1)
            if (arr1[i]>arr1[i+1]):
                a=arr1[i]
                arr1[i]=arr1[i+1]
                arr1[i+1]=a
        print(arr1)         
    print(arr1) 
bubbleSort([3,2,7,6,4,9,12])    