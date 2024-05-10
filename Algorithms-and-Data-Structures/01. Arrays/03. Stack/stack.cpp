/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 10th of May, 2024

    Details : Stack Class with Push, Pop and Seek methods

    CONCEPT :
    Stack Array is like Dynamic Array with push, pop and seek methods.
    it maintains only top value and pushes next to the top and pop from top ;
   seek returns the value of the value at top.

    its working is like Dynamic Array.
    so it works like power-series:

    items/Stored    Array Size
         0          1
         1          1
         2          2
         3          4
         4          4
         5          8
         6          8
         7          8
         8          8
         9          16
         .          .
         17         32
         .          .
         n         2 * n  [APPROX]

*/
#include <iostream>

template <class Type>
class Stack {
  int capacity = 1;
  int top = -1;
  Type *arr = new Type[capacity];

  void resize() {
    capacity = 2 * capacity;
    Type *newArr = new Type[capacity];

    for (int i = 0; i <= top; i++) {
      newArr[i] = arr[i];
    }
    delete[] arr;
    arr = newArr;
  }

 public:
  Stack() {
    std::cout << "\nStack Created with default size : "
              << sizeof(Type) * capacity << " bytes or equivalent of "
              << capacity << " data " << std::endl;
  }
  ~Stack() {
    std::cout << "\nStack Destroyed with default size : "
              << sizeof(Type) * capacity << " bytes or equivalent of "
              << capacity << " data " << std::endl;
  }
  void push(Type data) {
    if (top < capacity - 1) {
      top++;
      arr[top] = data;
    } else {
      resize();
      push(data);
    }
  }

  void pop() {
    if (top != -1) {
      top--;
    } else {
      std::cout << "\n\ntop is " << top << " and capacity is " << capacity
                << std::endl;
    }
  }

  std::pair<Type, int> seek() {
    if (top != -1) {
      return std::make_pair(arr[top], top);
    } else {
      std::cout << "\n\ntop is " << top << " and capacity is " << capacity
                << std::endl;
      return std::make_pair(-1, top);
    }
  }
};

int main() {
  std::cout << "Stack : " << std::endl;
  Stack<int> myStack;

  int data;
  std::pair<int, int> temp;

  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "Select anyone : " << std::endl;
    std::cout << "1 for PUSH : " << std::endl;
    std::cout << "2 for POP : " << std::endl;
    std::cout << "3 for SEEK/TOP ELEMENT : " << std::endl;
    std::cout << "any for Exit : " << std::endl;
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "\nEnter a value to be pushed : ";
        std::cin >> data;
        myStack.push(data);
        break;
      case 2:
        myStack.pop();
        break;
      case 3:
        temp = myStack.seek();
        if (temp.second != -1) {
          std::cout << "\nMy Seek or Top Data is  : " << temp.first
                    << std::endl;
        } else {
          std::cout << "\nmyStack is empty, no value to seek" << std::endl;
        }
        break;
      default:
        check = 0;
        break;
    }
  }

  return 0;
}