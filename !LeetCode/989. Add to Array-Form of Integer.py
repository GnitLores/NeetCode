from typing import List


class Solution:
    # Handling the addition manually is more complicated but much more efficient.
    # Reversing the list makes it much easier to work with as we can iterate forward
    # and append the final carry.
    # Use modulo and integer division method to get digits of k and add them to
    # to digits of number.
    # Go through all digits except the most significant and carry if over 9.
    # Check if last digit carries as well, and if so append extra digit.
    # Reverse list again and return.
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0
        while k > 0:
            digit = k % 10
            k //= 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            i += 1
        
        for i in range(len(num) - 1):
            if num[i] > 9:
                num[i] -= 10
                num[i + 1] += 1
        
        if num[-1] > 9:
            num[-1] -= 10
            num.append(1)
        num.reverse()
        return num

    # Convert to integer so we don't have to handle addition ourselves.
    # Sum powers to convert list to integer representation, add k to integer,
    # and then use modulo and integer division method to convert back into
    # list of numbers.
    # This is simple but unfortunately also slow and only barely passes leetcode.
    def addToArrayFormSimple(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        val = 0
        for i, n in enumerate(num):
            val += n * (10 ** i)
        val += k

        res = []
        while val > 0:
            digit = val % 10
            val //= 10
            res.append(digit)
        res.reverse()
        return res

sol = Solution()
print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
print(sol.addToArrayForm(num = [2,7,4], k = 181))
print(sol.addToArrayForm(num = [2,1,5], k = 806))
print("")
print(sol.addToArrayFormSimple(num = [1,2,0,0], k = 34))
print(sol.addToArrayFormSimple(num = [2,7,4], k = 181))
print(sol.addToArrayFormSimple(num = [2,1,5], k = 806))