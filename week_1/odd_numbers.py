def sum_even_numbers(nums):
    """
    Description: function to check even numbers at odd indices
    Parameters: nums list
    Return: Sum of even numbers that are present at odd indices
    """
    sum = 0
    for i in range(len(nums)):
        if i%2!=0:
            if nums[i]%2==0:
                sum += nums[i]
    return sum
lst_nums = list(map(int,input().split(',')))
calc_sum = sum_even_numbers(lst_nums)
print(calc_sum)
            