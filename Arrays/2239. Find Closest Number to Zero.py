class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        closest = float('inf')

        for i in range(len(nums)):
            distance = abs(nums[i])
            # Check if this number is closer or has the same distance but is positive
            if distance < closest or (distance == closest and nums[i] > result):
                closest = distance
                result = nums[i]
        
        return result
 
    

if __name__ == '__main__':
    answer = Solution()
    
    case_1 = [-4,-2,1,4,8]
    answer_1 = answer.findClosestNumber(nums=case_1)
    print(f"Result for test case 1: {answer_1}")

    case_2 = [2,-1,1]
    answer_2 = answer.findClosestNumber(nums=case_2)
    print(f"Result for test case 2: {answer_2}")

    case_3 = [2,1,1,-1,100000]
    answer_3 = answer.findClosestNumber(nums=case_3)
    print(f"Result for test case 3: {answer_3}")

    case_4 = [-100000,-100000]
    answer_4 = answer.findClosestNumber(nums=case_4)
    print(f"Result for test case 4: {answer_4}")

    case_5 = [61488,18221,-1321,90249,-62158,55128,-93476,53905,57644,24630,89599,-95795,-14891,-60298,17690,99022,-24006,-89156,80135,-46303,18812,59924,32024,82924,-47519,-77086,1763,68618,53629,-56957,95485,99630,-7977,31164,94481,-80239,-57749,-3319,-58231,-94841,-19292,33200,-31446,-3528,2229,74241,-19992,-91852,-28073,31453,-74484,35491,38870,-9499,39838,87369,21123,-38616,-89277,-14541,-81586,-18569,-58242,-71216,10816,15086,-10519,51080,53257,-4912,-37142,-16723,-69795,54937,-24920,68970,-10010,-81717,36203,-67939,73877,-58258,-57183,36637,91518,-8492,-57476,50523,62462,73152,-9511,-66761,28333,-87163,5187]
    answer_5 = answer.findClosestNumber(nums=case_5)
    print(f"Result for test case 5: {answer_5}")