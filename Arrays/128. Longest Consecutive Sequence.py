class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == '__main__':
    answer = Solution()

    nums = [100,4,200,1,3,2]
    answer_1 = answer.longestConsecutive(nums)
    print(f"Result for test case 1: {answer_1}")

    nums = [0,3,7,2,5,8,4,6,0,1]
    answer_2 = answer.longestConsecutive(nums)
    print(f"Result for test case 2: {answer_2}")
