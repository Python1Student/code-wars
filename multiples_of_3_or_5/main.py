def solution(nums):
    return sum([num for num in range(1, nums) if num % 3 == 0 or num % 5 == 0]) if nums > 0 else 0
