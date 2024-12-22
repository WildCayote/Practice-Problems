class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] = 1
        
        return False


if __name__ == '__main__':
    answer = Solution()

    case_1 = [1,2,3,1]
    answer_1 = answer.containsDuplicate(nums=case_1)
    print(f"Result for test case 1: {answer_1}")

    case_2 = [1,2,3,4]
    answer_2 = answer.containsDuplicate(nums=case_2)
    print(f"Result for test case 2: {answer_2}")

    case_3 = [1,1,1,3,3,4,3,2,4,2]
    answer_3 = answer.containsDuplicate(nums=case_3)
    print(f"Result for test case 3: {answer_3}")