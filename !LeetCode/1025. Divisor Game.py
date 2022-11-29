class Solution:
    # Whoever gets 1 will lose because there is not number 0 < x < 1.
    # Thus the goal is to force your opponent to get 1, adn the only way to do that
    # is to yourself get 2 and choose 1 as divisor.
    # Since no odd number is divisible by 2, odd numbers only have odd divisors.
    # If you get an even number and choose 1, the opponent will get an odd number.
    # Since the opponent can only choose an odd number to subtract, you will then always
    # get an even number, at which point you can choose 1 again to repeat.
    # Consequently, whoever gets an even number will win by always choosing 1.
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0