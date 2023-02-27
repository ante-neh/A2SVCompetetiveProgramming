class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        canonicalPath = []
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if canonicalPath:
                    canonicalPath.pop()
                    
            else:
                canonicalPath.append(p)
                
        return "/" + "/".join(canonicalPath)
