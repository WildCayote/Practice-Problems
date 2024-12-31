class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


if __name__ == '__main__':
    answer = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    answer_1 = answer.trap(height)
    print(f"Result for test case 1: {answer_1}")

    height = [4,2,0,3,2,5]
    answer_2 = answer.trap(height)
    print(f"Result for test case 1: {answer_2}")
