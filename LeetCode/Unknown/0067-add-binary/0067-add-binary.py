class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binA = int(a, 2)
        binB = int(b, 2)

        total = binA + binB
        return bin(total)[2:]