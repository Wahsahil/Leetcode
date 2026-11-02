class Solution(object):
    def expressiveWords(self, s, words):

        def check(word):
            i = j = 0

            while i < len(s) and j < len(word):

                if s[i] != word[j]:
                    return False

                char = s[i]

                count1 = 0
                while i < len(s) and s[i] == char:
                    count1 += 1
                    i += 1

                count2 = 0
                while j < len(word) and word[j] == char:
                    count2 += 1
                    j += 1

                if count1 < count2:
                    return False

                if count1 != count2 and count1 < 3:
                    return False

            return i == len(s) and j == len(word)

        ans = 0

        for word in words:
            if check(word):
                ans += 1

        return ans