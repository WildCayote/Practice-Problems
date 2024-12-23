from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values() )
    
if __name__ == '__main__':
    answer = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    answer_1 = answer.groupAnagrams(strs)
    print(f"Result for test case 1: {answer_1}")

    strs = [""]
    answer_2 = answer.groupAnagrams(strs)
    print(f"Result for test case 1: {answer_2}")

    strs = ["a"]
    answer_3 = answer.groupAnagrams(strs)
    print(f"Result for test case 1: {answer_3}")
