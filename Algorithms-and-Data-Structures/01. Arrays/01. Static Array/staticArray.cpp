/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 6th of May, 2024

    Details : Static Array Class with Insert, Delete and Modify Methods
	
	CONCEPT : 
		Static Array have a fixed array size and is compile-time allocated.
*/

#include <iostream>

// Static Array Class with Methods
template <class Type, int SizeOfArray>
class myStaticArray {
  int top = -1;
  Type myArray[SizeOfArray];

 public:
  void print() {
    for (int i = 0; i <= top; i++) {
      std::cout << myArray[i] << std::endl;
    }
  }

  // ...INSERT...
  void myInsert(Type data) {
    if (top < SizeOfArray) {
      top++;
      myArray[top] = data;
    } else {
      std::cout << "top is " << top << " and Size is " << SizeOfArray
                << std::endl;
    }
  }

  void myInsert(Type data, int index) {
    if (top < index && !(top == index - 1)) {
      std::cout << "top is " << top << " and Size is " << SizeOfArray
                << " and Index is  " << index << std::endl;
    } else {
      if (top < SizeOfArray) {
        top++;
        Type tempArray[SizeOfArray];

        for (int i = 0; i <= top; i++) {
          if (i < index) {
            tempArray[i] = myArray[i];
          } else if (i == index) {
            tempArray[i] = data;
          } else {
            tempArray[i] = myArray[i - 1];
          }
        }

        for (int i = 0; i <= top; i++) {
          myArray[i] = tempArray[i];
        }
      } else {
        std::cout << "top is " << top << " and Size is " << SizeOfArray
                  << std::endl;
      }
    }
  }

  // ...DELETE...
  void myDelete() {
    if (top != -1) {
      --top;
    } else {
      std::cout << "top is " << top << " and Size is " << SizeOfArray
                << std::endl;
    }
  }

  void myDelete(int index) {
    if (top < index) {
      std::cout << "top is " << top << " and Size is " << SizeOfArray
                << " and Index is  " << index << std::endl;
    } else {
      if (top != -1) {
        Type tempArray[SizeOfArray];
        for (int i = 0; i <= top; i++) {
          if (i < index) {
            tempArray[i] = myArray[i];
          } else {
            tempArray[i] = myArray[i + 1];
          }
        }
        top--;

        for (int i = 0; i <= top; i++) {
          myArray[i] = tempArray[i];
        }
      } else {
        std::cout << "top is " << top << " and Size is " << SizeOfArray
                  << std::endl;
      }
    }
  }

  // ...MODIFY...
  void myModify(Type data, int index) { myArray[index] = data; }
};

// MAIN FUNCTION
int main() {
  const int SizeOfArray = 5;

  myStaticArray<char, SizeOfArray> myArray;

  std::cout << " INSERT " << std::endl;
  myArray.myInsert('a', 0);
  myArray.myInsert('b', 1);
  myArray.myInsert('c', 2);
  myArray.myInsert('d', 3);
  myArray.myInsert('e', 4);

  myArray.print();

  std::cout << " DELETE " << std::endl;
  myArray.myDelete();
  myArray.myDelete(2);

  myArray.print();

  std::cout << " MODIFY " << std::endl;
  myArray.myModify('x', 0);
  myArray.print();

  return 0;
}