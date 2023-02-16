class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        NN = len(trainers)
        N = len(players)
        res = 0
        l = N-1
        r = NN-1
        while l >= 0 and r >= 0:
            # print(l, r)
            if players[l] > trainers[r]:
                l -= 1
            else:
                res += 1
                l -= 1
                r -= 1
        # print(res)
        return res
