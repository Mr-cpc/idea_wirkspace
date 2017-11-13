def maxproofthre(nums:list) -> int:
    mx,md,mi = max(nums[:3]),max()
    for num in nums:
