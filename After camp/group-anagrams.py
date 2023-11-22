class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup = defaultdict(list)

        for word in strs:
            anagramGroup["".join(sorted(word))].append(word)

        return list(anagramGroup.values())