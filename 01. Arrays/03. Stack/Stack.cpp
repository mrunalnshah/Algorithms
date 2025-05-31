// Author: Mrunal Nirajkumar Shah
// Date  : 31th May 2025

/*
Stack
A Stack is a Last In First Out (LIFO) Data Structure.

* Implemented with my Previous Dynamic Array Code with a get_top() addon in the
dynamic array code.

Adding into Stack:  1 -> 2 -> 3
Poping from Stack:  3 -> 2 -> 1
Last In First Out.


Methods:
1. push
2. pop
3. peek

ErrorCode:
1 -> Out of Bound

*/

#include <iostream>

#include "DynamicArray.cpp"

template <class TypeName>
class Stack {
  DynamicArray<TypeName> myArray;
  int top;

 public:
  Stack() {
    top = -1;

    std::cout << "Stack Initialized." << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  ~Stack() {
    std::cout << "Stack Destroyed." << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  // Push At the end {O(1)}
  int push(TypeName data) {
    myArray.insertAtEnd(data);
    return 0;
  }

  // Pop from the end {O(1)}
  int pop() {
    if (myArray.get_top() == -1) {
      return 1;
    }
    myArray.removeAtEnd();
    return 0;
  }

  // Get The Data in the Top of Stack {O(1)}
  TypeName peek() {
    if (myArray.get_top() == -1) {
      throw std::out_of_range("Array is Empty");
    }

    return myArray.get_value(myArray.get_top());
  }

  void errorInformation(int code) {
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }
    if (code == 1) {
      std::cout << "Out of Bound Index" << std::endl;
    }
  }
};