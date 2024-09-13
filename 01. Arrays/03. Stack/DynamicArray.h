// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 13 September 2024

/*
        Dynamic Array Implemented and modified for Stack Implementation.

        can look at :
        https://github.com/mrunalnshah/Algorithms
        for detailed Dynamic Array Implementation.
*/

#include <iostream>

template <class Typename>
class DynamicArray {
 protected:
  int topOfArray = -1;
  int sizeOfArray = 1;
  Typename* arr;

 public:
  // Constructor Created with initializing an array of size defined.
  DynamicArray() {
    arr = new Typename[sizeOfArray];
    std::cout << "Dynamic Array is Created." << std::endl;
    std::cout << "Dynamic Array Size : " << sizeOfArray << std::endl;
    std::cout << "Top is " << topOfArray << std::endl;
    std::cout << std::endl;
  }

  // Destructor destroying the array and ending the implementation at end.
  ~DynamicArray() {
    std::cout << std::endl;
    std::cout << "Array Size : " << sizeOfArray << std::endl;
    std::cout << "Top is " << topOfArray << std::endl;
    delete[] arr;
    std::cout << "Dynamic Array is Destroyed." << std::endl;
  }

  // Resizing the Array for size Requirement,
  // O(1){assigning new Array} + O(n) {copying elements} = O(n)
  void resize() {
    sizeOfArray = 2 * sizeOfArray;
    Typename* newArr = new Typename[sizeOfArray];
    for (int i = 0; i <= topOfArray; i++) {
      newArr[i] = arr[i];
    }
    delete[] arr;
    arr = newArr;
  }

  // Print Whole Array [ O(n) ]
  int print() {
    if (topOfArray == -1) {
      return 1;
    }
    std::cout << "Printing Index to Values :-" << std::endl;
    for (int i = 0; i <= topOfArray; i++) {
      std::cout << i << " : " << arr[i] << std::endl;
    }
    return 0;
  }

  // Printing ErrorCode [ O(1) ]
  void errorCode(int code) {
    if (code == 1) {
      std::cout << "Array is Empty, top is -1." << std::endl;
    }
    if (code == 2) {
      std::cout << "Index is not appropriate" << std::endl;
    }
    if (code == -1) {
      std::cout << "No Memory Available." << std::endl;
    }
    if (code == -2) {
      std::cout << "It is breaking continuity. Size is " << sizeOfArray
                << " Top is " << topOfArray << std::endl;
    }
  }
};