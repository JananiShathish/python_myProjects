class Solution:
    def pivotIndex(self, nums) -> int:
        sumleft=[]
        sumRight=[]
        total=len(nums)
        for i in range(total):
            if i==0:
                sumleft.append(0)
                # print(sumleft)
                
            else:   
                sumleft.append(sum(nums[0:i]))
                # print(sumleft)
            # sum_right=sum(nums[(i+1):(total)])
            sumRight.append(sum(nums[(i+1):(total)]))
            # print(sumleft)
            # print(sumRight)
           
            if(sumleft[i] == sumRight[i]):
                return i
        return -1
s=Solution()
print(output)
