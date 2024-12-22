class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        final = ''
        dif = len(word1) - len(word2)
        # word 2 is longer
        if dif < 0:
            for i in range(len(word1)):
                final += word1[i] + word2[i]
            final += word2[i+1:]

        # word 1 is longer
        elif dif > 0:
           for i in range(len(word2)):
               final += word1[i] + word2[i]
           final += word1[i+1:]

        else:
            for i in range(len(word1)):
                final += word1[i] + word2[i]

        return final

if __name__ == '__main__':
    answer = Solution()

    word_1 = "abc"
    word_2 = "pqr"
    answer_1 = answer.mergeAlternately(word_1, word_2)
    print(f"Result for test case 1: {answer_1}")

    word_1 = "ab"
    word_2 = "pqrs"
    answer_2 = answer.mergeAlternately(word_1, word_2)
    print(f"Result for test case 2: {answer_2}")

    word_1 = "abcd"
    word_2 = "pq"
    answer_3 = answer.mergeAlternately(word_1, word_2)
    print(f"Result for test case 3: {answer_3}")