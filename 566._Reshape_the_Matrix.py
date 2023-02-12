class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if (r * c ) != (row * col):
            return mat
        res = [[0]*c for _ in range(r)]
        print(res)
        r1 = c1 = 0
        for rr in range(row):
            for cc in range(col):
                res[r1][c1] = mat[rr][cc]
                c1 += 1
                if c1 == c:
                    c1 = 0
                    r1 += 1
                # c1 += 1
        # print(res)
        return res
