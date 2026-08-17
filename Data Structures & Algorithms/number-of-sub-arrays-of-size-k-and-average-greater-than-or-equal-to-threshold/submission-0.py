class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        i = 0
        keep = k

        while k - 1 < len(arr):
            total = sum(arr[i:k])
            print(total)
            print(float(total / keep))

            if float(total / keep) >= threshold:
                count+=1
            i+=1
            k+=1

        return count