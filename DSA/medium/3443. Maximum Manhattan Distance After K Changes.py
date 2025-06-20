class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = u = v = 0
        deltas = {'N': (1, -1), 'S': (-1, 1), 'E': (1, 1), 'W': (-1, -1)}
    
        for i, char in enumerate(s):
            du, dv = deltas[char]
            u += du
            v += dv
            l = i + 1
        
            u_dec = (l - u) // 2
            res = max(res, u + 2 * min(k, u_dec), -(u - 2 * min(k, l - u_dec)))
        
            v_dec = (l - v) // 2
            res = max(res, v + 2 * min(k, v_dec), -(v - 2 * min(k, l - v_dec)))
        
        return res
