// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 13 September 2024

/*
    Stack
    Implemented using Dynamic Arrays, Stack is a Last In, First Out Data
Structure used to store data.
    LIFO ( Last in First out).

   1 2 3 4 5 6 7 8

   Push -> 1
        1
   Push -> 2
        1 2
   Push -> 3,4,5,6,7,8 in sequence.
        1 2 3 4 5 6 7 8

   Pop  -> 8
   Pop  -> 7
   Pop 6 times we get -> 6, 5, 4, 3, 2, 1

   So to conclude, Stack is something which push data to top and when to be
popped we take out last element pushed.


   Implementing this array, requires :
    Nothing, we use Dynamic Array we created, i have included the Dynamic Array
in header file.

    Functions :
    1. Push(data) [O(1)] : Push the Data at end of the array.
    2. Pop(data) [O(1)]  : Pop the data from end of the array.
    3. seek()    [O(1)]  : Print the data at end of the array.

    Look at code for more understanding...

    Error i got implementing this :
      When you declare Stack as a template class, you need to specify that
      DynamicArray is also a template class.

    ERROR CODE:
    void errorCode(int code);

     1  --> Array is Empty, top is -1
     0 --> SUCCESS
     ** Dynamic Array may contain its own errorCode.

     By The Way we can use ENUM for more better Error part code writing.

     Thanks for reading my code
     Mrunal Nirajkumar Shah.
*/

#include "DynamicArray.h"

template <class Typename>
class Stack : public DynamicArray<Typename> {
 public:
  Stack() {
    std::cout << "Stack is built on Dynamic Array" << std::endl;
    std::cout << "Top is " << this->topOfArray << std::endl;
  }
  ~Stack() {
    std::cout << "Stack is deleted." << std::endl;
    std::cout << "Top is " << this->topOfArray << std::endl;
  }

  int push(Typename data) {
    if (this->topOfArray >= this->sizeOfArray - 1) {
      this->resize();
    }
    this->topOfArray++;
    this->arr[this->topOfArray] = data;
    return 0;
  }

  int pop() {
    if (this->topOfArray == -1) {
      return 1;
    }
    this->topOfArray--;
    return 0;
  }

  int seek() {
    if (this->topOfArray == -1) {
      std::cout << " Stack is Empty. " << std::endl;
      return 1;
    }
    std::cout << "Data is " << this->arr[this->topOfArray] << std::endl;
    return 0;
  }
};

int main() {
  Stack<int> myStack;

  int selectOption;
  int data;

  int errorCode;
  bool check = true;
  while (check) {
    std::cout << "Stack : " << std::endl;
    std::cout << "1. Push the value on top." << std::endl;
    std::cout << "2. Pop the value from top." << std::endl;
    std::cout << "3. Seek the value at top." << std::endl;
    std::cout << "4. Print Dynamic Array." << std::endl;
    std::cout << "5+. Exit" << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "Enter data to be pushed : ";
        std::cin >> data;
        errorCode = myStack.push(data);
        break;
      case 2:
        errorCode = myStack.pop();
        break;
      case 3:
        errorCode = myStack.seek();
        break;
      case 4:
        errorCode = myStack.print();
        break;
      default:
        check = false;
    }
    myStack.errorCode(errorCode);
  }
  return 0;
}