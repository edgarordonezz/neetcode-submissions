class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # count zero
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
        product = 1
        # compute product
        for num in nums:
            if num != 0:
                product *= num
        # build result
        result = []
        if zeroCount > 1:
            return [0] * len(nums)
        for num in nums:
            if zeroCount == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // num)
        return result
        

                
