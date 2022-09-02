from typing import List

class Solution:
    # It's fizzbuzz =)
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            fizz = i % 3 == 0
            buzz = i % 5 == 0
            if fizz and buzz:
                res.append("FizzBuzz")
            elif fizz: 
                res.append("Fizz")
            elif buzz:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

sol = Solution()
print(sol.fizzBuzz(15))