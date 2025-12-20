class Solution(object):
    def calPoints(self, operations):
        final = []

        for op in operations:
            if op.isdigit():
                final.append(int(op))

            elif op == "+":
                final.append(final[-1] + final[-2])

            elif op == "D":
                final.append(final[-1] * 2)

            elif op == "C":
                final.pop()

        return sum(final)

i=Solution()
ops = ["5","2","C","D","+"]
print(i.calPoints(ops))

                
