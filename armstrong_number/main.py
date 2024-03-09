def narcissistic(value):
    nums = list(str(value))
    return sum([int(num) ** len(nums) for num in nums]) == value  # Code away


print(narcissistic(1652))
