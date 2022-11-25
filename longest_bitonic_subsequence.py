def LongestBitonicSequence(nums):
        print(type(nums))
        t=len(nums)
        mid=int(t/2)
        # maz= max(nums)
        maz=nums[mid]


        incArray=[]
        increasingArray=nums[0:mid]
        print(increasingArray)
        decreasingArray=nums[mid:len(nums)]
        print(decreasingArray)
        k=0

        for i in increasingArray:
            # print("iiii",i, type(i))
            if(k<=i):
                incArray.append(i)
                k=i
        for j in decreasingArray:
            if(maz>=j):
                incArray.append(j)
                maz=j
        print(incArray)
        # for i,j in zip(increasingArray,decreasingArray):
        #     if(k<=i ):
        #         incArray.append(i)
        #         k=i
        #     if(maz>=j):
        #         incArray.append(j)
        #         maz=j             

        print(len(incArray))

LongestBitonicSequence([1,11,2,10,4,5,2,1])