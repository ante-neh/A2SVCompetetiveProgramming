class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for c in path:
            if c == '..' and stack:
                stack.pop()
            
            elif c != '.' and c != '' and c != '..':
                stack.append(c)

        stack = "/".join(stack)

        return "/" + stack