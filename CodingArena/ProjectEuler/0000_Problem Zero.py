"""
Problem Number: 0
Link: https://projecteuler.net/register

Author: Mrunal Nirajkumar Shah
Date  : 30th January, 2026
"""

class Solve():
    @staticmethod
    def odd_square_sum(n=977000):
       sum = 0
       
       for i in range(n):
          squared_num = pow(i, 2)

          if squared_num % 2 == 0:
             continue
          
          sum += squared_num
       return sum
    
def main():
  solve = Solve()

  result = solve.odd_square_sum()
  print(result)

if __name__ == "__main__":
   main()
