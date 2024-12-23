class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product = 1
        zero_idx = []
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i]: product *= nums[i]
            elif len(zero_idx) < 1: 
                zero_idx.append(i)
            else: return result

        if len(zero_idx):
            for i in zero_idx:
                result[i] = product
        else:
            for i in range(len(nums)):
                result[i] = int(product / nums[i])
        

        return result
            

if __name__ == '__main__':
    answer = Solution()

    nums = [0,0,0]
    answer_1 = answer.productExceptSelf(nums)
    print(f"Result for test case 1: {answer_1}")

    nums = [-1,1,0,-3,3]
    answer_2 = answer.productExceptSelf(nums)
    print(f"Result for test case 1: {answer_2}")