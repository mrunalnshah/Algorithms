/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 19th of May, 2024

    Details : Fibonacci is implemented using Recursion.
    [Double Branch Recurssion]


    CONCEPT :
    Recursion means "defining a problem in terms of itself".

     A recursive function solves a particular problem by calling a copy of
   itself and solving smaller subproblems of the original problems.

    Fibonacci(n) = (n-1) + (n-2);

    We Know this :
    Fibonacci(0) = 0
    Fibonacci(1) = 1

Step 1 : n = 5, make a recurssive tree.
    Fib(5) =         Fib(4)            +                 Fib(3)
           Fib(3)      +          Fib(2)            Fib(2)  +   Fibo(1)
     Fib(2)  +   Fib(1)      Fib(1) + Fib(0)   Fib(1) +  Fib(0)
Fib(1) + Fib(0)

STEP 2 : Input what we know and move from base to top.
    Fib(5) =         Fib(4)            +                 Fib(3)
           Fib(3)      +          Fib(2)            Fib(2)  +   1
     Fib(2)  +   1                1 + 0            1  +  0
     1 + 0

Step 3 : get the answer :
      Fib(5) = 5;

      Honestly this is bad way, because it take O(2^n) speed and O(n) memory
while a while or for loop can do it in O(n) speed and O(1) memory.

   BUT there are more efficent ways to use recursion to get better outputs.

*/

#include <iostream>

class Fibonacci {
  int number;
  int fibonacciNumber;

  int fibonacci(int number) {
    if (number < 0) {
      return -1;
    }
    if (number == 0) {
      return 0;
    }

    if (number == 1) {
      return 1;
    }

    return fibonacci(number - 1) + fibonacci(number - 2);
  }

 public:
  void get_Fibonacci() {
    std::cout << "Enter a Number : ";
    std::cin >> number;
    fibonacciNumber = fibonacci(number);
    if (fibonacciNumber == -1) {
      std::cout << "NO Fibonacci Number for " << number << std::endl;
    } else {
      std::cout << "Fibonacci for " << number << " is " << fibonacciNumber
                << std::endl;
    }
  }
};

int main() {
  Fibonacci myFibo;

  myFibo.get_Fibonacci();
  return 0;
}