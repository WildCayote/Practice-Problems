from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = defaultdict(lambda: 0)
        result = []
        for num in nums:
            res[num] += 1

        for num in res:
            result.append((num, res[num]))

        result.sort(
            key = lambda x: x[1],
            reverse=True
        )
    
        return [i[0] for i in result[:k]]


if __name__ == '__main__':
    answer = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    answer_1 = answer.topKFrequent(nums, k)
    print(f"Result for test case 1: {answer_1}")

    nums = [1]
    k = 1
    answer_2 = answer.topKFrequent(nums, k)
    print(f"Result for test case 1: {answer_2}")
