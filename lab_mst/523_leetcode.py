class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        mp={0:-1}
        total=0
        for i in range(n):
            total+=nums[i]
            rem=total%k
            if rem in mp:
                if i-mp[rem]>=2:
                    return True
            else:
                mp[rem]=i
        return False
            