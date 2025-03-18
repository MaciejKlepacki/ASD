def removeDuplicates(nums):
        counter=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i]!=None: nums[i+1] = None
            else: counter +=1
        return nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))