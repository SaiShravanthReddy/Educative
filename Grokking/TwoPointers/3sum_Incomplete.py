def three_sum(nums):
    nums = sorted(nums)
    print(nums)

    ans = []
    
    index = 0
    
    while index < len(nums):
        if nums[0] > 0:
            return [[]]
        
        # skip duplicate numbers
        if index > 0 and nums[index] == nums[index-1]:
            print("duplicates")
            index += 1
            continue
        
        
        # select a current element and then set low and high pointer
        low = index + 1
        high = len(nums) - 1
        
    
        while low < high:
            print(nums[index], nums[low], nums[high])
            
            if nums[index] + nums[low] + nums[high] == 0:
                print("equal")
                ans.append([nums[index], nums[low], nums[high]])
                break
            elif nums[index] + nums[low] + nums[high] < 0:
                print("lesser")
                low += 1
                continue
            else: 
                print("greater")
                high -= 1
                continue
        
        index += 1
            
        
    return ans
   

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))    