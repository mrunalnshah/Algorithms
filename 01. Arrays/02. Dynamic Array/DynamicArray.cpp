// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 11 September 2024

/*
    Dynamic Array
    An continuous block of memory, called array with specified memory allocated
   to it in the initial stage of creating array and then reallocating arrays
   depending on required size is Dynamic Array. It has dynamic size memory,
   which can be increased only.

   1 2 3 4 5 6 7 8
                                Size
   Array 1 : 1                    1
   Array 2 : 1 2                  2
   Array 3 : 1 2 3 4              4
   Array 4 : 1 2 3 4 5 6 7 8      8

   8 >= 1 + 2 + 4
   Amortized complexity.


   Implementing this array, requires :
    1. topOfTheArray : Maintains the last index of element present in array.
                [ -1 is not element present in the Array ]
    2. sizeOfArray   : keeps the latest size of Array.
    3. Array         : we need an Array of size x for our implementation.
    4. new Array     : When reassigning the array to meet size requirement, we
   need to push all elements to new Array and then reassign new array to old
   array.

    Functions :
    1. resize() [O(n)]  : reallocate the array to meet the size requirement.
    2. insert(data) [ O(1) ] : insert data at the topOfTheArray + 1 index, if
   space available.
    3. insert(index,data) [ (O(n) ] : insert data at any index, from 0 to
   topOfTheArray + 1.
    4. remove() [ O(1) ]  : remove last index, if available.
    5. remove(index) [ O(n) ]: remove any index between 0 to topOfTheArray
    6. print()  [ O(n) ]: prints whole array

    Look at code for more understanding...

    ERROR CODE:
    void errorCode(int code);

    -1 --> Out of Memory
    -2 --> It is breaking continuity of Array.
     1  --> Array is Empty, top is -1
     2  --> Index is not appropriate.
     0 --> SUCCESS

     By The Way we can use ENUM for more better Error part code writing.

     Thanks for reading my code
     Mrunal Nirajkumar Shah.
*/

#include <iostream>

template <class Typename>
class DynamicArray {
  int topOfArray = -1;
  int sizeOfArray = 1;
  Typename* arr;

 public:
  // Constructor Created with initializing an array of size defined.
  DynamicArray() {
    arr = new Typename[sizeOfArray];
    std::cout << "Initial Array Size : " << sizeOfArray << std::endl;
    std::cout << "Top is " << topOfArray << std::endl;
  }

  // Destructor destroying the array and ending the implementation at end.
  ~DynamicArray() {
    std::cout << "Array Size : " << sizeOfArray << std::endl;
    std::cout << "Top is " << topOfArray << std::endl;
    delete[] arr;
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

  // Insert data at the end of the array. [ O(1) ]
  int insert(Typename data) {
    if (topOfArray >= sizeOfArray - 1) {
      resize();
    }
    topOfArray++;
    arr[topOfArray] = data;

    return 0;
  }

  // Insert data at any position in the array [ O(n) ]
  int insert(Typename data, int index) {
    if (topOfArray >= sizeOfArray - 1) {
      resize();
    }
    if (index < 0 || index > topOfArray + 1) {
      return -2;
    }
    for (int i = topOfArray; i >= index; i--) {
      arr[i + 1] = arr[i];
    }
    topOfArray++;
    arr[index] = data;
    return 0;
  }

  // Remove data from the last index of array. [ O(1) ]
  int remove() {
    if (topOfArray == -1) {
      return 1;
    }
    topOfArray--;
    return 0;
  }

  // Remove data from any position between 0 to topOfTheArray [ O(n) ]
  int remove(int index) {
    if (topOfArray == -1) {
      return 1;
    }
    if (index < 0 || index > topOfArray) {
      return 2;
    }

    for (int i = index; i <= topOfArray - 1; i++) {
      arr[i] = arr[i + 1];
    }
    topOfArray--;
    return 0;
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

int main() {
  std::cout << "Dynamic Array\n" << std::endl;

  DynamicArray<int> myResult;

  int data;
  int index;

  int getErrorCode;
  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "Dynamic ARRAY : " << std::endl;
    std::cout << "1. Insert At End" << std::endl;
    std::cout << "2. Insert At Any Position" << std::endl;
    std::cout << "3. Remove At End" << std::endl;
    std::cout << "4. Remove At Any Position" << std::endl;
    std::cout << "5. Print All of Array" << std::endl;
    std::cout << "6+. Exit" << std::endl;
    std::cout << "Enter Option : ";
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "Enter Data : ";
        std::cin >> data;

        getErrorCode = myResult.insert(data);
        break;
      case 2:
        std::cout << "Enter Data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;

        getErrorCode = myResult.insert(index, data);
        break;
      case 3:
        getErrorCode = myResult.remove();
        break;
      case 4:
        std::cout << "Enter Index : ";
        std::cin >> index;

        getErrorCode = myResult.remove(index);
        break;
      case 5:
        getErrorCode = myResult.print();
        break;
      default:
        check = 0;
    }
    if (getErrorCode != 0) {
      myResult.errorCode(getErrorCode);
    } else {
      std::cout << "Success." << std::endl;
    }
  }
  return 0;
}