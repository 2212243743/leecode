from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            j = target-nums[i]
            try:
                index = nums.index(j,i+1)
            except:
                continue
            return [i,index]
if __name__ == '__main__':
    su = Solution()
    print(su.twoSum([2,7,11,15],9))
