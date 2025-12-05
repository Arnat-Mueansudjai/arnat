def hammingWeight(self, n):
        L = ""
        while n > 0:
            L += str(n % 2)
            n //= 2
        L = (L[::-1])
        Sum = 0
        for i in range(len(L)):
            Sum += int(L[i])
        return Sum 
