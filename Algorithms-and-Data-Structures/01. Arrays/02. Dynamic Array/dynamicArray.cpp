/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 9th of May, 2024

    Details : Dynamic Array Class with Insert, Delete and Modify Methods

    CONCEPT :
    Dynamic Array have a no fixed array size and is runtime allocated.

    so it works like power-series

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
class dynamicArray {
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
  dynamicArray() {
    std::cout << "Object CREATED!! with dynamic array size of "
              << sizeof(Type) * capacity << " bytes equivalent to  " << capacity
              << " data " << std::endl;
  };
  ~dynamicArray() {
    delete[] arr;
    std::cout << "Object Destroyed with dynamic array size of "
              << sizeof(Type) * capacity << " bytes equivalent to  " << capacity
              << " data " << std::endl;
  };

  void push_back(Type data) {
    if (top < capacity - 1) {
      top++;
      arr[top] = data;
    } else {
      resize();
      push_back(data);
    }
  }

  void push_back(Type data, int index) {
    if (top < capacity - 1) {
      if (index > top + 1) {
        std::cout << "\n\nIndex is " << index << " top is " << top
                  << " and capacity is " << capacity << std::endl;
      } else if (index == top + 1) {
        push_back(data);
      } else {
        top++;
        Type *pArr = new Type[capacity];

        for (int i = 0; i <= top; i++) {
          if (i < index) {
            pArr[i] = arr[i];
          } else if (i == index) {
            pArr[i] = data;
          } else {
            pArr[i] = arr[i - 1];
          }
        }
        delete[] arr;
        arr = pArr;
      }
    } else {
      resize();
      push_back(data, index);
    }
  }

  void pop_back() {
    if (top != -1) {
      --top;
    } else {
      std::cout << "\n\nTOP is " << top << " and Capacity is " << capacity
                << std::endl;
    }
  }

  void pop_back(int index) {
    if (top != -1) {
      if (index <= top) {
        Type *pArr = new Type[capacity];

        for (int i = 0; i <= top; i++) {
          if (i < index) {
            pArr[i] = arr[i];
          } else if (i == index) {
            continue;
          } else {
            pArr[i - 1] = arr[i];
          }
        }
        --top;
        delete[] arr;
        arr = pArr;
      } else {
        std::cout << "\n\nIndex is " << index << " top is " << top
                  << " and capacity is " << capacity << std::endl;
      }

    } else {
      std::cout << "\n\nTOP is " << top << " and Capacity is " << capacity
                << std::endl;
    }
  }

  void print() {
    for (int i = 0; i <= top; i++) {
      std::cout << i << " = " << arr[i] << std::endl;
    }
  }
};

int main() {
  dynamicArray<int> temp;

  std::cout << "DYNAMIC ARRAY : " << std::endl;

  int switchValue;
  int data;
  int index;

  int check = 1;
  while (check) {
    std::cout << "\n\nSelect 1 Operations : " << std::endl;
    std::cout << " 1 for Push at End " << std::endl;
    std::cout << " 2 for Pop at End " << std::endl;
    std::cout << " 3 for Push at Random " << std::endl;
    std::cout << " 4 for Pop at Random " << std::endl;
    std::cout << " 5 for print " << std::endl;
    std::cout << " Anything else to exit..." << std::endl;
    std::cout << " ENTER : ";
    std::cin >> switchValue;
    std::cout << std::endl;
    switch (switchValue) {
      case 1:
        std::cout << "Enter data to be pushed : ";
        std::cin >> data;
        temp.push_back(data);
        break;
      case 2:
        temp.pop_back();
        break;
      case 3:
        std::cout << "Enter data to be pushed : ";
        std::cin >> data;
        std::cout << "Enter Index where data to be pushed : ";
        std::cin >> index;
        temp.push_back(data, index);
        break;
      case 4:
        std::cout << "Enter Index where data to be poped : ";
        std::cin >> index;
        temp.pop_back(index);
        break;
      case 5:
        temp.print();
        break;
      default:
        check = 0;
        break;
    }
  }

  return 0;
}