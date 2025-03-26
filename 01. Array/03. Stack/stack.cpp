// Author: Mrunal Nirajkumar Shah
// Date: 26 March 2025

/*
    Stack
    A Stack is a data structure that operates on "Last In First Out" concept
   meaning the last element to enter, will be the first element to exit.

   EXAMPLE :
   1 -> 2 -> 3 (Enter Sequence)
   3 <- 2 <- 1 (Exit Sequence)

   1,2,3 -> 3,2,1
   Enter    Exit

    We use our home grown dynamic array module made before this.

    Methods [Big O notation]:
    1. push [O(1)]
    2. pop [O(1)]
    3. print all elements [O(n)]

    ErrorCode:
     0 : Success
*/

#include <iostream>

#include "dynamic-array.cpp"

template <class TypeName>
class Stack {
  DynamicArray<TypeName> myArray;

 public:
  // Stack Constructor
  Stack() { std::cout << "Stack Initialized" << std::endl; }

  // Stack Destructor
  ~Stack() { std::cout << "Stack Destroyed" << std::endl; }

  // Push the element at the end
  int push(TypeName data) {
    myArray.insert(data);
    return 0;
  }

  // Pop the last pushed element from end
  int pop() {
    myArray.remove();
    return 0;
  }

  // Print all elements in stack
  void printStack() { myArray.printArray(); }

  // Return the status of the error code
  void errorCode(int code) {
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }
  }
};