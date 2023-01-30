class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ch = skill[0] + skill[-1]
        res = 0
        i = 0
        j = len(skill)-1
        while(i < j):
            if (skill[i] + skill[j] != ch):
                return -1
            res += (skill[i] * skill[j])
            i+=1
            j-=1
        return res