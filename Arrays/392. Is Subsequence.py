class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hashmap = {}
        for i in range(len(t)):
            if t[i] in hashmap: hashmap[t[i]].append(i)
            else: hashmap[t[i]] = [i]
        
        prev_idx = -1
        for i in range(len(s)):
            if s[i] in hashmap and len(hashmap[s[i]]):
                index_found = False
                for j in range(len(hashmap[s[i]])):
                    least_idx = hashmap[s[i]][j]
                    if prev_idx < least_idx:
                        prev_idx = hashmap[s[i]].pop(j)
                        index_found = True
                        break
                if not index_found : return False
            else: return False

        return True   


if __name__ == '__main__':
    answer = Solution()

    s = "abc"
    t = "ahbgdc"
    answer_1 = answer.isSubsequence(s, t)
    print(f"Result for test case 1: {answer_1}")

    s = "axc"
    t = "ahbgdc"
    answer_2 = answer.isSubsequence(s, t)
    print(f"Result for test case 2: {answer_2}")
