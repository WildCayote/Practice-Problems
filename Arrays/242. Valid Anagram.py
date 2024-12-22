class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        

        if len(s) != len(t): return False

        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in hashmap: return False
            else:
                if hashmap[t[i]] == 0: return False
                hashmap[t[i]] -= 1
                
        return True


if __name__ == '__main__':
    answer = Solution()

    s = "anagram"
    t = "nagaram"
    answer_1 = answer.isAnagram(s, t)
    print(f"Result for test case 1: {answer_1}")

    s = "rat"
    t = "car"
    answer_2 = answer.isAnagram(s, t)
    print(f"Result for test case 2: {answer_2}")