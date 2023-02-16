class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill.sort()
        l = 0
        r = N - 1
        prev = 0
        res = []
        sums = 0
        # print(sum(skill)// (N//2))
        while l < r:
            if not prev:
                prev = skill[l] + skill[r]
                s = skill[l] * skill[r]
                sums += s
                res.append([skill[l], skill[r]])
                l += 1
                r -= 1
            else:
                s = skill[l] + skill[r]
                if s != prev:
                    break
                else:
                    f = skill[l] * skill[r]
                    sums += f
                    res.append([skill[l], skill[r]])
                    l += 1
                    r -= 1
            # print(res, sums)
