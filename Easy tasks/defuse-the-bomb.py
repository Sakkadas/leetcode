class Solution:
    def decrypt(self, code, k):
        i = 0
        res, dig = [], []
        if k == 0:
            for i in range(len(code)):
                code[i] = 0
            return code
        elif k > 0:
            while len(code) > i:
                for j in range(k):
                    dig.append((code[((j + 1) + i) % len(code)]))
                res.append(sum(dig))
                dig.clear()
                i += 1
            return res
        elif k < 0:
            while len(code) > i:
                for j in range(abs(k)):
                    dig.append((code[((j - abs(k)) + i) % len(code)]))
                res.append(sum(dig))
                dig.clear()
                i += 1
            return res
