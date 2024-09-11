// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 03 September 2024

/*
    Static Array
    An continuous block of memory, called array with specified memory allocated
   to it in the initial stage of creating array is Static Array. It has fixed
   size memory, which cannot be increased/decreased.

   Implementing this array, requires :
    1. topOfTheArray : Maintains the last index of element present in array.
		[ -1 is not element present in the Array ]
    2. sizeOfArray   : keeps the size of Array.
    3. Array         : we need an Array of size x for our implementation.

    Functions :
    1. insert(data) [ O(1) ] : insert data at the topOfTheArray + 1 index, if
   space available.
    2. insert(index,data) [ (O(n) ] : insert data at any index, from 0 to
   topOfTheArray + 1.
    3. remove() [ O(1) ]  : remove last index, if available.
    4. remove(index) [ O(n) ]: remove any index between 0 to topOfTheArray
    5. print()  [ O(n) ]: prints whole array

    Look at code for more understanding...

    ERROR CODE:
    void errorCode(int code);

    -1 --> Out of Memory
    -2 --> It is breaking continuity of Array.
     1  --> Array is Empty, top is -1
     2 --> something wrong happened at insert(index, data) for loop part.
     3  --> Index is not appropriate.
     0 --> SUCCESS

     By The Way we can use ENUM for more better Error part code writing.

     Thanks for reading my code
     Mrunal Nirajkumar Shah.
*/

#include <iostream>

template <class Typename>
class StaticArray {
  int sizeOfArray = 0;
  int topOfTheArray = -1;

  Typename* arr;

 public:
  // Constructor Created with initializing an array of size defined.
  StaticArray(int arraySize) {
    sizeOfArray = arraySize;
    arr = new Typename[sizeOfArray];
    std::cout << " Array initialized with size " << sizeOfArray << std::endl;
    std::cout << " Top Of the array is (-1 is Empty) " << topOfTheArray
              << std::endl;
  }
  // Destructor destroying the array and ending the implementation at end.
  ~StaticArray() {
    delete[] arr;
    std::cout << " Array destroyed with size " << sizeOfArray << std::endl;
    std::cout << " Top Of the array is (-1 is Empty) " << topOfTheArray
              << std::endl;
  }

  // Insert data at the end of the array. [ O(1) ]
  int insert(Typename data) {
    if (topOfTheArray >= sizeOfArray - 1) {
      return -1;
    }
    topOfTheArray++;
    arr[topOfTheArray] = data;
    return 0;
  }

  // Insert data at any position in the array [ O(n) ]
  int insert(int index, Typename data) {
    if (index < 0 || index > topOfTheArray + 1) {
      return -2;
    }
    if (topOfTheArray >= sizeOfArray - 1) {
      return -1;
    }

    for (int i = topOfTheArray; i >= index; i--) {
      arr[i + 1] = arr[i];
    }
    arr[index] = data;
    topOfTheArray++;
    return 0;
  }

  // Remove data from the last index of array. [ O(1) ]
  int remove() {
    if (topOfTheArray == -1) {
      return 1;
    }
    topOfTheArray--;
    return 0;
  }

  // Remove data from any position between 0 to topOfTheArray [ O(n) ]
  int remove(int index) {
    if (topOfTheArray == -1) {
      return 1;
    }
    if (index < 0 || index > topOfTheArray) {
      return 3;
    }
    for (int i = index; i <= topOfTheArray - 1; i++) {
      arr[i] = arr[i + 1];
    }
    topOfTheArray--;
    return 0;
  }

  // Print Whole Array [ O(n) ]
  int print() {
    if (topOfTheArray == -1) {
      return 1;
    }
    std::cout << "Printing Index to Values :- " << std::endl;
    for (int i = 0; i <= topOfTheArray; i++) {
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
      std::cout
          << "something wrong happened at insert(index, data) for loop part."
          << std::endl;
    }
    if (code == 3) {
      std::cout << "Index is not appropriate" << std::endl;
    }
    if (code == -1) {
      std::cout << "No Memory Available." << std::endl;
    }
    if (code == -2) {
      std::cout << "It is breaking continuity. Size is " << sizeOfArray
                << " Top is " << topOfTheArray << std::endl;
    }
  }
};

int main() {
  std::cout << "Static Array\n" << std::endl;

  int sizeOfArray = 2;
  std::cout << "Enter Size of Static Array : ";
  std::cin >> sizeOfArray;

  StaticArray<int> myResult(sizeOfArray);

  int data;
  int index;

  int getErrorCode;
  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "STATIC ARRAY : " << std::endl;
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