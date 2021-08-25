class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1[:-1]
        num2 = num2[:-1]
        num1s = num1.split('+')
        num2s = num2.split('+')

        first = int(num1s[0])*int(num2s[0])
        second = (int(num2s[0]) * int(num1s[1]))+(int(num1s[0])*int(num2s[1]))
        third = int(num1s[1])*int(num2s[1])*-1

        return f'{first+third}+{second}i'
