class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        camelCaseMatching = []
        def isSubsequence(pat, query):
            p1, p2 = 0, 0 
            count = 0
            for c in query:
                if c.isupper():
                    count += 1

            while p1 < len(pat) and p2 < len(query):
                if pat[p1] == query[p2]:
                    if query[p2].isupper():
                        count -= 1
                        
                    p1 += 1

                p2 += 1

            return count == 0 and p1 == len(pat)


        for query in queries:
            if isSubsequence(pattern, query):
                camelCaseMatching.append(True)
            
            else:
                camelCaseMatching.append(False)

        return camelCaseMatching



            