class Solution(object):
    def restoreIpAddresses(self, s):

        result = []

        def backtrack(index, path):

            if len(path) == 4:

                if index == len(s):
                    result.append(".".join(path))

                return

            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

                if len(part) > 1 and part[0] == '0':
                    break

                if int(part) > 255:
                    break

                path.append(part)

                backtrack(index + length, path)

                path.pop()
        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result