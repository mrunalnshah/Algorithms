"""
Problem Number: 3
Link: https://projecteuler.net/problem=3

Author: Mrunal Nirajkumar Shah
Date  : 30th January, 2026
"""

class Solve():
    @staticmethod
    def find_largest_prime_factor(n=600851475143):
        largest_prime = 1
        
        i = 2 # if n=1, its infinite loop as n / 1 = n
        while n > 1:
            while n % i == 0:
                largest_prime = i

                n = int(n / i)
            i += 1
        return largest_prime


def main():
    solve = Solve()

    result = solve.find_largest_prime_factor()
    print(result)


if __name__ == "__main__":
    main()