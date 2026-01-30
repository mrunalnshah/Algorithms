"""
Problem Number: 2
Link: https://projecteuler.net/problem=2

Author: Mrunal Nirajkumar Shah
Date  : 30th January, 2026
"""

class Solve:
    @staticmethod
    def even_sum_fib(n = 4000000):
        first_term = 1
        second_term = 2

        sum = 0
        while first_term < n:
            if first_term % 2 == 0:
                sum += first_term
            
            temp = second_term
            second_term += first_term
            first_term = temp
        
        return sum

def main():
    solve = Solve()

    result = solve.even_sum_fib()
    print(result)


if __name__ == "__main__":
    main()