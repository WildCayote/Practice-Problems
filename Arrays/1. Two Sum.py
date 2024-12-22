class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compliment = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in compliment:
                return [i, compliment[remainder][0]]
            else:
                if nums[i] in compliment: compliment[nums[i]].append(i)
                else: compliment[nums[i]] = [i]
        
        return []

if __name__ == '__main__':
    answer = Solution()

    nums = [2,7,11,15]
    answer_1 = answer.twoSum(nums, 9)
    print(f"Result for test case 1: {answer_1}")

    nums = [3,2,4]
    answer_2 = answer.twoSum(nums, 6)
    print(f"Result for test case 2: {answer_2}")

    nums = [3,3]
    answer_3 = answer.twoSum(nums, 6)
    print(f"Result for test case 3: {answer_3}")
