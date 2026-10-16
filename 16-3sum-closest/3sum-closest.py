class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        Closest = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low,high = i+1,n-1 
            while low < high:
                Curr_sum = nums[i] + nums[low] + nums[high]
                if abs(Curr_sum - target)< abs(Closest - target):
                    Closest = Curr_sum
                if Curr_sum == target:
                    return Curr_sum
                elif Curr_sum<target:
                    low +=1
                else:
                    high -=1
        return Closest