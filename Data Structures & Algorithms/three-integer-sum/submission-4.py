class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        real_list = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if a == nums[i- 1] and i > 0:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]

                if total > 0:
                    r-=1

                elif total < 0:
                    l +=1

                else:
                    real_list.append((a, nums[l], nums[r]))
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

                

        return list(real_list)

