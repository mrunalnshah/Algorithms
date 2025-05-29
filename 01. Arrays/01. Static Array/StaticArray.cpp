// Author: Mrunal Nirajkumar Shah
// Date  : 29th May 2025

/*
Static Array
A Array is a data stored in a contiguous block in a Memory (mainly RAM). A
Static Array is an Array which has a fixed size block in RAM.

If we have x elements to store, we cannot store x + 1 elements in Array.


Methods:
1. Write
2. Insert at End
3. Remove at End
4. Insert at Begin
5. Remove at Begin
6. Insert anywhere
7. Remove anywhere
8. Print Array

ErrorCode:
1 -> Out of Bound
-1 -> Loop Finished, Case Not Found.
*/

#include <iostream>

template <class TypeName>
class StaticArray {
  TypeName* myArray;
  int arraySize;
  int top;

 public:
  StaticArray(int size) {
    arraySize = size;
    myArray = new TypeName[arraySize];
    top = -1;

    std::cout << "Static Array Initialized." << std::endl;
    std::cout << "Array Size: " << arraySize << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  ~StaticArray() {
    delete[] myArray;

    std::cout << "Static Array Destroyed." << std::endl;
    std::cout << "Array Size: " << arraySize << std::endl;
    std::cout << "top Value: " << top << std::endl;
  }

  // Modify At Any Position {O(1)}
  int write(int index, TypeName data) {
    if (index <= top) {
      myArray[index] = data;
      return 0;
    } else {
      return 1;
    }
  }

  // Insert At End {O(1)}
  int insertAtEnd(TypeName data) {
    if (top < arraySize - 1) {
      myArray[++top] = data;
      return 0;
    }
    return 1;
  }

  // Remove At End {O(1)}
  int removeAtEnd() {
    if (top > -1) {
      top--;
      return 0;
    }
    return 1;
  }

  // Insert At Begin {O(n)}
  int insertAtBegin(TypeName data) {
    if (top < arraySize - 1) {
      if (top == -1) {
        myArray[++top] = data;
        return 0;
      } else {
        for (int i = top; i >= 0; i--) {
          myArray[i + 1] = myArray[i];

          if (i == 0) {
            myArray[i] = data;
            ++top;
            return 0;
          }
        }
        return -1;
      }
    } else {
      return 1;
    }
  }

  // Remove At Begin {O(n)}
  int removeAtBegin() {
    if (top > -1) {
      if (top == 0) {
        top--;
        return 0;
      } else {
        for (int i = 0; i <= top; i++) {
          myArray[i] = myArray[i + 1];
        }
        top--;
        return 0;
      }
    } else {
      return 1;
    }
  }

  // Insert Anywhere {O(n)}
  int insert(int index, TypeName data) {
    if (top < arraySize - 1) {
      if (index <= top + 1) {
        if (index == 0) {
          insertAtBegin(data);
          return 0;
        } else if (index > 0 && index <= top) {
          for (int i = top; i >= index; i--) {
            myArray[i + 1] = myArray[i];
            if (i == index) {
              myArray[i] = data;
              ++top;
              return 0;
            }
          }
        } else {
          insertAtEnd(data);
          return 0;
        }
        return -1;
      }
      return -1;
    } else {
      return 1;
    }
  }

  // Remove Anywhere {O(n)}
  int remove(int index) {
    if (top > -1 && index <= top) {
      if (index == 0) {
        removeAtBegin();
        return 0;
      }
      if (index > 0 && index < top) {
        for (int i = index; i <= top; i++) {
          myArray[i] = myArray[i + 1];
        }
        --top;
        return 0;
      }
      if (index == top) {
        removeAtEnd();
        return 0;
      }

      return -1;
    }

    return 1;
  }

  // Print Whole Array {O(n)}
  void print() {
    for (int i = 0; i <= top; i++) {
      std::cout << i << " -> " << myArray[i] << std::endl;
    }
  }

  // Error Information {O(1)}
  void errorInformation(int code) {
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }

    if (code == 1) {
      std::cout << "Out of Bound" << std::endl;
    }

    if (code == -1) {
      std::cout << "Loop Finished, Case Not Found." << std::endl;
    }
  }
};