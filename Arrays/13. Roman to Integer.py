class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        final = 0
        value_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'V': 5,
            'X': 10,
            'I': 1
        }
        for i in range(len(s)):
            if i+1 < len(s) and value_map[s[i]] < value_map[s[i+1]]:
                final -= value_map[s[i]]
            else:
                final += value_map[s[i]]

        return final



if __name__ == "__main__":
    answer = Solution()

    s = "III"
    answer_1 = answer.romanToInt(s)
    print(f"Result for test case 1: {answer_1}")

    s = "LVIII"
    answer_2 = answer.romanToInt(s)
    print(f"Result for test case 2: {answer_2}")
    
    s = "MCMXCIV"
    answer_3 = answer.romanToInt(s)
    print(f"Result for test case 2: {answer_3}")
