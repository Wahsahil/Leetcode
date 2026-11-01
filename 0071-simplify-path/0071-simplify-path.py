class Solution(object):
    def simplifyPath(self, path):
        stack = []

        words = path.split('/')

        for i in words:

            if i == '' or i == '.':
                continue

            elif i == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(i)

        return '/' + '/'.join(stack)