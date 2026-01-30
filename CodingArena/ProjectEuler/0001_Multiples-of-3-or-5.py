"""
Problem Number: 1
Link: https://projecteuler.net/problem=1

Author: Mrunal Nirajkumar Shah
Date  : 30th January, 2026
"""

class Solve:
    @staticmethod
    def sum_multiples_35(n=1000):
        sum = 0

        # Add multiples of 3
        for i in range(3, n, 3):
            sum += i
        
        # Add multiples of 5
        for j in range(5, n, 5):
            sum += j

        # subtract multiple of 3 and 5 due to common adds twice
        for k in range(15, n, 15):
            sum -= k

        return sum

def main():
    solve = Solve()

    result = solve.sum_multiples_35()

    print(result)

if __name__ == "__main__":
    main()