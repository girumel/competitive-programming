class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            tmp = x
            inv = []
            while tmp != 0:
                inv.append(str(tmp % 10))
                tmp //= 10
            if x == int(''.join(inv)):
                return True
            else:
                return False
        