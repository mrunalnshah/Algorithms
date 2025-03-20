// Author: Mrunal Nirajkumar Shah
// Date: 20 March 2025

/*
    Static Array
    A Array is a contiguous block of data, and a Static Array is a fixed size
   array, which cannot be resized.

    Once the static array is full, it cannot add new data into it without old
   data being deleted.

    Methods [Big O notation]:
    1. size [O(1)]
    2. count [O(1)]
    3. insert at end [O(1)]
    4. insert at any position [O(n)]
    5. delete at end [O(1)]
    6. delete at any position [O(n)]
    7. print all elements [O(n)]

    ErrorCode:
    -2 : insertion failed, didnt execute i == index
    -1 : All Case failed.
     0 : Success
     1 : topOfArray < sizeOfArray - 1
     2 : topOfArray == -1
     3 : index cant be >= sizeOfArray
*/

#include <iostream>

template <class TypeName>
class StaticArray {
  int top_of_array = -1;
  int array_size;
  TypeName* array;

 public:
  StaticArray(int size) {
    array_size = size;
    array = new TypeName[array_size];
    std::cout << "Static Array Initalized with size : " << StaticArray::size()
              << std::endl;
    std::cout << "Static Array Initalized with count: " << StaticArray::count()
              << std::endl;
  }
  ~StaticArray() {
    delete[] array;
    std::cout << "Static Array Destroyed with size : " << size() << std::endl;
    std::cout << "Static Array Destroyed with count: " << count() << std::endl;
  }

  // Returns the Size Of The Array
  int size() { return array_size; }

  // Returns the Number of Elements Added into the Array aka top_of_array
  int count() { return top_of_array + 1; }

  // inserts the data at the end of the array
  int insert(TypeName data) {
    if (top_of_array < array_size - 1) {
      top_of_array++;
      array[top_of_array] = data;
      return 0;
    }
    return 1;
  }

  // inserts the data at any index of the array
  int insert(TypeName data, int index) {
    if (index >= array_size) {
      return 3;
    }

    if (top_of_array < array_size - 1) {
      if (index == top_of_array + 1) {
        insert(data);
      } else if (index <= top_of_array) {
        for (int i = top_of_array; i >= index; i--) {
          array[i + 1] = array[i];

          if (i == index) {
            array[i] = data;
            top_of_array++;
            return 0;
          }
        }
        return -2;
      }
      return -1;
    }
    return 1;
  }

  // remove the data from end of array
  int remove() {
    if (top_of_array == -1) {
      std::cout << "o" << std::endl;
      std::cout << top_of_array << std::endl;
      return 2;
    }
    top_of_array--;
    std::cout << top_of_array << std::endl;
    return 0;
  }

  // remove data from any part of the array
  int remove(int index) {
    if (top_of_array == -1) {
      return 2;
    }

    if (index == top_of_array) {
      remove();
      return 0;
    } else if (index < top_of_array) {
      for (int i = index; i < top_of_array; i++) {
        array[i] = array[i + 1];
      }
      top_of_array--;
      return 0;
    }

    return 0;
  }

  // prints whole array
  void printArray() {
    for (int i = 0; i <= top_of_array; i++) {
      std::cout << "Data : " << array[i] << " --> Index: " << i << std::endl;
    }
  }

  // prints the errorcode got from methods runned.
  void errorCode(int code) {
    std::string errorMessage;
    switch (code) {
      case 0:
        errorMessage = "Success";
        break;
      case 1:
        errorMessage = "Error: top_of_array < array_size - 1";
        break;
      case 2:
        errorMessage = "Error: top_of_array == -1";
        break;
      case 3:
        errorMessage = "Error: index cant be >= array_size ";
        break;
      case -1:
        errorMessage = "Error: All Case failed";
        break;
      case -2:
        errorMessage = "Error: insertion failed, didnt execute i == index";
        break;
      default:
        break;
    }
    std::cout << errorMessage << std::endl;
  }
};