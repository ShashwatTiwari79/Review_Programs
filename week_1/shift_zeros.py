def shiftZeros(nums):
    """
    Description: Function to shift all zeros occuring in the list to the end
    parameters : nums list
    return : modified list where all zeros are shifted to the last
    """
    total_zeros = 0
    nums_lst_nos = []
    for i in range(len(nums)):
        if nums[i] == 0:
            total_zeros += 1
        else:
            nums_lst_nos.append(nums[i])
    for _ in range(total_zeros):
        nums_lst_nos.append(0)
    return nums_lst_nos
    

nums = list(map(int,input("Input: ").split(','))) 
new_lst_nums = shiftZeros(nums)
print(f"Output:-{new_lst_nums}")

        
