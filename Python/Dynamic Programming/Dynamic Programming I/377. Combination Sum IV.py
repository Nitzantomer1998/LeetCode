def combination_sum_4(nums: list[int], target: int) -> int:
    
    count = [0] * (target + 1)

    count[0] = 1

    for i in range(1, target + 1):

        for j in nums:

            if j <= i:
                count[i] += count[i - j]

    return count[target]
