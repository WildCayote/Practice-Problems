class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        store = {}
        final = []
        largest = -1
        temp = []
        for i in range(len(nums)):
            num = nums[i]
            if largest == -1:
                temp = [num]
            elif num - 1 == temp[-1]:
                temp.append(num)
                # look for successors in the store
                next = num + 1
                while next in store:
                    temp.append(next)
                    next += 1
            else:
                # look for predecessors in the store
                temp = [num]
                prev = num - 1
                while prev in store:
                    temp.append(prev)
                    prev -= 1
                temp = temp[-1::-1]

                # look for successors in the store
                next = num + 1
                while next in store:
                    temp.append(next)
                    next += 1

            if largest <= len(temp): 
                largest = len(temp)
                final = temp
            store[num] = 1

        return len(final)


if __name__ == '__main__':
    answer = Solution()

    nums = [100,4,200,1,3,2]
    answer_1 = answer.longestConsecutive(nums)
    print(f"Result for test case 1: {answer_1}")

    nums = [0,3,7,2,5,8,4,6,0,1]
    answer_2 = answer.longestConsecutive(nums)
    print(f"Result for test case 2: {answer_2}")
