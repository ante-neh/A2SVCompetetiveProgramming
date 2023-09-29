class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(version1.split('.')), list(version2.split('.'))
        p1, p2 = 0, 0

        while p1 < len(v1) and p2 < len(v2):
            if int(v1[p1]) > int(v2[p2]):
                return 1
            elif int(v1[p1]) < int(v2[p2]):
                return -1

            else:
                p1 += 1
                p2 += 1

        while p1 < len(v1):
            if int(v1[p1]) > 0:
                return 1
            p1 += 1

        while p2 < len(v2):
            if int(v2[p2]) > 0:
                return -1
            p2 += 1

        return 0