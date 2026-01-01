lst = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
        return result

x = Solution()
print(x.twoSum(lst,target))