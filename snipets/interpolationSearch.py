def search( nums, target):

    low = 0
    high =len(nums)-1

    while low <= high and target >= nums[low] and target <= nums[high]: 
        if low == high: 
            if nums[low] == target: 
                return low; 
            return -1; 

        pos = int(low + (((float(high - low)/( nums[high] - nums[low])) * (target - nums[low])))) 
    
        if nums[pos] == target: 
            return pos 
        if nums[pos] < target: 
            low = pos + 1; 
        else: 
            high = pos - 1; 
    
    return -1