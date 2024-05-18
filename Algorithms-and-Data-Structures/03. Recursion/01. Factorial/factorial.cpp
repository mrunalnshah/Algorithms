/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 18th of May, 2024

    Details : Factorial is implemented using Recursion.


    CONCEPT :
    Recursion means "defining a problem in terms of itself".

     A recursive function solves a particular problem by calling a copy of
   itself and solving smaller subproblems of the original problems.

    Factorial = 5;
    5!
       5 * 4!
           4 * 3!
                3 * 2!
                     2 * 1!
                          1

      1 * 2 * 3 * 4 * 5 = 120;
      This is recursive way of finding factorials.

      Honestly this is bad way, because it take O(n) speed and O(n) memory while
   a while or for loop can do it in O(n) speed and O(1) memory.

   BUT there are more efficent ways to use recursion to get better outputs.

*/

#include <iostream>

class Factorial {
  int number;
  int factorialNumber;

  int find_factorial(int number) {
    if (number < 0) {
      return -1;
    }
    if (number == 1 || number == 0) {
      return 1;
    }
    return number * find_factorial(number - 1);
  }

 public:
  void get_Factorial() {
    std::cout << "Enter a Number : ";
    std::cin >> number;

    factorialNumber = find_factorial(number);
    if (factorialNumber >= 0) {
      std::cout << "Factorial of " << number << " is " << factorialNumber
                << std::endl;
    } else {
      std::cout << "Factorial of " << number << " is not possible . "
                << std::endl;
      std::cout << "In mathematics, the factorial of a natural number n "
                   "(written n!) is the product of the strictly positive "
                   "integer numbers less than or equal to n.\n"
                << std::endl;
    }
  }
};

int main() {
  Factorial myFactorial;

  myFactorial.get_Factorial();

  return 0;
}