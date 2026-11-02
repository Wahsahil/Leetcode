import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        words = re.findall(r'[a-z]+', paragraph.lower())

        banned = set(banned)

        freq = {}

        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)