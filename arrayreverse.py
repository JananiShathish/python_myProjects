# def reve(nums):
#     s=nums[::-1]
#     print(s)    
# reve([1,2,3,4,5,6])    

def rev(nums):
    for i in range(int(len(nums)/2)):
        a=nums[i]
        nums[i]=nums[len(nums)-(i+1)]
        nums[len(nums)-(i+1)]=a
        print('nums',nums)
    print(nums)    
rev([1,2,3,4,5,6,7,8])    