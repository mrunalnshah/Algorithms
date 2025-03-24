// Author: Mrunal Nirajkumar Shah
// Date: 20 March 2025

/*
    Dynamic Array
    A Array is a contiguous block of data, and a Dynamic Array is a dynamic size
   array, which can be resized when the array is out of space. The Dynamic Array
   creates a new array 2 times the size of old array and store all the values
   from old array into new array and add the latest data also into the array.

    Once the dynamic array is full, it can add new data into it by creating a
   new array double the size of old array.

    Elements to be added: {1,2,3,4,5,6}
    1: 1                    [Array Size = 1]
    2: 1, 2                 [Array Size = 2] {Resized}
    4: 1, 2, 3, 4           [Array Size = 4]
    8: 1, 2, 3, 4, 5, 6     [Array Size = 8]

    8 >= 1 + 2 + 4 {ALWAYS}
    Array Size goes as 1,2,4,8,16,32,64,...

    O(n) to Resize, and O(n) to insert but as O(n) for resizing is less
   frequent, its an Ammortized Complexity.

   We donot care about O(2n) or O(n) + constant, because at some point that will
   intersect with a bigger complexity like O(n^2) and is always going to be
   small after that point.

    Methods [Big O notation]:
    1. resize [O(n)] {Ammortized Complexity}
    1. size [O(1)]
    2. count [O(1)]
    3. insert at end [O(1)]
    4. insert at any position [O(n)]
    5. delete at end [O(1)]
    6. delete at any position [O(n)]
    7. print all elements [O(n)]

    ErrorCode:
     0 : Success
     1 : index > top_of_array + 1 (Out Of Range)
     2 : topOfArray == -1
*/

#include <iostream>

template <class TypeName>
class DynamicArray {
  int top_of_array = -1;
  int array_size = 1;
  TypeName *array;

  // resize the array.
  void resize() {
    array_size = array_size * 2;
    TypeName *new_array = new TypeName[array_size];

    for (int i = 0; i <= top_of_array; i++) {
      new_array[i] = array[i];
    }

    delete[] array;
    array = new_array;
  }

 public:
  DynamicArray() {
    array = new TypeName[array_size];
    std::cout << "Dynamic Array initialized with Size " << DynamicArray::size()
              << std::endl;
    std::cout << "Dynamic Array initialized with Count "
              << DynamicArray::count() << std::endl;
  }
  ~DynamicArray() {
    delete[] array;
    std::cout << "Dynamic Array Destroyed with Size " << DynamicArray::size()
              << std::endl;
    std::cout << "Dynamic Array Destroyed with Count " << DynamicArray::count()
              << std::endl;
  }

  // Return the size of the Array
  int size() { return array_size; }

  // Return the Number of elements added into the array aka top_of_array
  int count() { return top_of_array + 1; }

  // inserts the data at the end of the array
  int insert(TypeName data) {
    if (top_of_array >= array_size - 1) {
      DynamicArray::resize();
    }
    array[++top_of_array] = data;
    return 0;
  }

  // inserts the data at any index of the array
  int insert(TypeName data, int index) {
    if (index > top_of_array + 1) {
      return 1;
    }

    if (top_of_array >= array_size - 1) {
      DynamicArray::resize();
    }
    if (index == top_of_array + 1) {
      insert(data);
    } else {
      for (int i = top_of_array; i >= index; i--) {
        array[i + 1] = array[i];
        if (i == index) {
          array[i] = data;
          top_of_array++;
        }
      }
    }
    return 0;
  }

  // remove the data from end of array
  int remove() {
    if (top_of_array == -1) {
      return 2;
    }
    top_of_array--;
    return 0;
  }

  // remove data from any part of the array
  int remove(int index) {
    if (top_of_array == -1) {
      return 2;
    }
    for (int i = index; i <= top_of_array - 1; i++) {
      array[i] = array[i + 1];
    }
    top_of_array--;
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
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }
    if (code == 1) {
      std::cout << "index > top_of_array + 1 (Out Of Range)" << std::endl;
    }
    if (code == 2) {
      std::cout << "topOfArray == -1" << std::endl;
    }
  }
};