// Author: Mrunal Nirajkumar Shah
// Date  : 31th May 2025

/*
Dynamic Array
A Array is a data stored in a contiguous block in a Memory (mainly RAM). A
Dynamic Array is an Array which can resize the block in RAM based on number of
input data. If the data input exceed existing array size, than we can create a
new block of memory with double the previous array size and store all data into
it to fix the fixed size problems.

Number of Operations     Memory
        1                   1
        2                 1  2
        4                1 2 3 4
        8               1 2 3 4 5 6 7 8

        8 >= 1 + 2 + 4

        Number of Operations are needed for allocating new array, so we also
need more operations to push data into it. but as we dont allocate data so
frequently, we dont care about the operations. (Ammortized Complexity).



Methods:
0. resize
1. Write
2. Insert at End
3. Remove at End
4. Insert at Begin
5. Remove at Begin
6. Insert anywhere
7. Remove anywhere
8. Print Array
9. get_top
10. get_value

ErrorCode:
1 -> Out of Bound
2 -> Empty Array
-1 -> Loop Finished, Case Not Found.
*/

#include <iostream>

template <class TypeName>
class DynamicArray {
  TypeName* myArray;
  int arraySize = 1;
  int top;

  // Create newArray and Copy myArray's element into the new array. {O(n)}
  // Ammortized Complexity as its not gonna be called everytime.
  void resize() {
    arraySize = arraySize * 2;
    TypeName* newArray = new TypeName[arraySize];

    for (int i = 0; i <= top; i++) {
      newArray[i] = myArray[i];
    }

    delete[] myArray;
    myArray = newArray;
  }

 public:
  DynamicArray() {
    arraySize = 1;
    myArray = new TypeName[arraySize];
    top = -1;

    std::cout << "Dynamic Array Initialized." << std::endl;
    std::cout << "Array Size: " << arraySize << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  ~DynamicArray() {
    delete[] myArray;

    std::cout << "Dynamic Array Destroyed." << std::endl;
    std::cout << "Array Size: " << arraySize << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  // Modify At Any Position {O(1)}
  int write(int index, TypeName data) {
    if (index <= top && index > -1) {
      myArray[index] = data;
      return 0;
    }
    return 1;
  }

  // Insert At End {O(1)}
  int insertAtEnd(TypeName data) {
    if (top >= arraySize - 1) {
      resize();
    }

    myArray[++top] = data;
    return 0;
  }

  // Remove At End {O(1)}
  int removeAtEnd() {
    if (top == -1) {
      return 2;
    }

    top--;
    return 0;
  }

  // Insert At Begin {O(n)}
  int insertAtBegin(TypeName data) {
    if (top >= arraySize - 1) {
      resize();
    }

    if (top == -1) {
      top++;
      myArray[top] = data;
      return 0;
    }

    for (int i = top; i >= 0; i--) {
      myArray[i + 1] = myArray[i];

      if (i == 0) {
        top++;
        myArray[i] = data;
        return 0;
      }
    }
    return -1;
  }

  // Remove At Begin {O(n)}
  int removeAtBegin() {
    if (top == -1) {
      return 2;
    }

    for (int i = 0; i <= top; i++) {
      myArray[i] = myArray[i + 1];
    }

    top--;
    return 0;
  }

  // Insert Anywhere {O(n)}
  int insert(int index, TypeName data) {
    if (index < 0 || index > top + 1) {
      return 1;
    }

    if (index == 0) {
      insertAtBegin(data);
      return 0;
    } else if (index > 0 && index <= top) {
      if (top >= arraySize - 1) {
        resize();
      }

      for (int i = top; i >= index; i--) {
        myArray[i + 1] = myArray[i];
      }

      myArray[index] = data;
      top++;
      return 0;

    } else if (index == top + 1) {
      insertAtEnd(data);
      return 0;
    } else {
      return -1;
    }
    return -1;
  }

  // Remove Anywhere {O(n)}
  int remove(int index) {
    if (top == -1) {
      return 2;
    }

    if (index < 0 || index > top) {
      return 1;
    }

    if (index == 0) {
      removeAtBegin();
      return 0;
    } else if (index > 0 && index < top) {
      for (int i = index; i < top; i++) {
        myArray[i] = myArray[i + 1];
      }
      top--;
      return 0;
    } else if (index == top) {
      removeAtEnd();
      return 0;
    } else {
      return -1;
    }
    return -1;
  }

  // Print Whole Array {O(n)}
  void print() {
    for (int i = 0; i <= top; i++) {
      std::cout << i << " -> " << myArray[i] << std::endl;
    }
  }

  // Return top value {O(1)}
  int get_top() { return top; }

  // get Value at Index {O(1)}
  TypeName get_value(int index) {
    if (index < 0 || index > top) {
      throw std::out_of_range("Out of Bound");
    }

    return myArray[index];
  }

  // Error Information {O(1)}
  void errorInformation(int code) {
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }

    if (code == 1) {
      std::cout << "Out of Bound" << std::endl;
    }

    if (code == 2) {
      std::cout << "Empty Array" << std::endl;
    }

    if (code == -1) {
      std::cout << "Loop Finished, Case Not Found." << std::endl;
    }
  }
};