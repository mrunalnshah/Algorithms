/*
        Static Arrays

        Author : Mrunal Nirajkumar Shah
        Date   : 30 of July, 2024


        Static Arrays means they are fixed size arrays. Once allocated the size
   in RAM, it cannot be changed.

   Some Values:
    topIndex starts from -1, -1 means empty.
    size is always topIndex - 1.
        example:
            size = 5
            topIndex can go 0,1,2,3,4 {total 5}



   We Implement:
                1. read at any index
                2. write at any index {not insert, you need an element to exist}
                3. insert at end
                4. remove at end
                5. insert at any position
                6. remove at any position
                7. print all elements in array



        To Read at any index 				 --> O(1)
        To Insert at the end of Static Array --> O(1)
        To Remove at the end of Static Array --> O(1)
        To Insert at any index               --> O(n)
                {Worst case : insert at first position}
*/

#include <iostream>

template <class dataType>
class staticArray {
  dataType *myArray;
  int topIndex;
  int size;

 public:
  // constructer
  staticArray(int arraySize) {
    size = arraySize;
    topIndex = -1;
    myArray = new dataType[arraySize];

    std::cout << std::endl;
    std::cout << "Size : " << size << std::endl;
    std::cout << "topIndex : " << topIndex << std::endl;
    std::cout << "Static Array is Created" << std::endl;
    std::cout << std::endl;
  }

  // destructor
  ~staticArray() {
    delete[] myArray;

    std::cout << std::endl;
    std::cout << "Size : " << size << std::endl;
    std::cout << "topIndex : " << topIndex << std::endl;
    std::cout << "Static Array is Destroyed" << std::endl;
    std::cout << std::endl;
  }

  // Read from any index O(1)
  dataType read(int index) {
    if (index <= topIndex && topIndex != -1) {
      return myArray[index];
    } else {
      return -911;
    }
  }

  // Write to any Index O(1)
  void write(dataType data, int index) {
    if (index <= topIndex && topIndex != -1) {
      myArray[index] = data;
    } else {
      std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                << topIndex << "\nSize : " << size << "\nGiven Index " << index
                << std::endl;
    }
  }

  // Insert at end of the Array O(1)
  void insert(dataType data) {
    if (topIndex < size) {
      topIndex++;
      myArray[topIndex] = data;
    } else {
      std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                << topIndex << "\nSize : " << size << std::endl;
    }
  }

  // Remove from end of the Array O(1)
  void remove() {
    if (topIndex != -1) {
      topIndex--;
    } else {
      std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                << topIndex << "\nSize : " << size << std::endl;
    }
  }

  // Insert at any index O(n)
  void insert(dataType data, int index) {
    if (topIndex < size && index <= topIndex + 1) {
      if (index == topIndex + 1) {
        insert(data);  // Calling Above made function.
      } else if (index <= topIndex) {
        for (int i = topIndex; i >= index; i--) {
          if (i > index) {
            myArray[i + 1] = myArray[i];
          } else if (i == index) {
            myArray[i + 1] = myArray[i];
            myArray[i] = data;
            topIndex++;
          } else {
            break;
          }
        }
      } else {
        std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                  << topIndex << "\nSize : " << size << "\nGiven Index "
                  << index << std::endl;
      }

    } else {
      std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                << topIndex << "\nSize : " << size << "\nGiven Index " << index
                << std::endl;
    }
  }

  // Remove at any index O(n)
  void remove(int index) {
    if (index <= topIndex && topIndex != -1) {
      if (index == topIndex) {
        topIndex--;
      } else if (index < topIndex) {
        for (int i = 0; i <= topIndex; i++) {
          if (i <= index) {
            continue;
          } else {
            myArray[i - 1] = myArray[i];
          }
        }
        topIndex--;
      } else {
        std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                  << topIndex << "\nSize : " << size << "\nGiven Index "
                  << index << std::endl;
      }
    } else {
      std::cout << "\nSomething went wrong...\nArray : \ntopIndex : "
                << topIndex << "\nSize : " << size << "\nGiven Index " << index
                << std::endl;
    }
  }

  // Print all index in Array O(n)
  void print() {
    for (int i = 0; i <= topIndex; i++) {
      std::cout << "Index : " << i << "\tElement : " << myArray[i] << std::endl;
    }
  }
};

int main() {
  staticArray<int> testStaticArray(10);

  int data;
  int index;

  int option;
  int check = 1;
  while (check) {
    std::cout << "1. Read at index." << std::endl;
    std::cout << "2. Write at index" << std::endl;
    std::cout << "3. Insert at end" << std::endl;
    std::cout << "4. Remove at end" << std::endl;
    std::cout << "5. Insert at any Position" << std::endl;
    std::cout << "6. Remove at any Position" << std::endl;
    std::cout << "7. Print the array" << std::endl;
    std::cout << "Anything else to end..." << std::endl;

    std::cout << "Enter Number : ";
    std::cin >> option;

    switch (option) {
      case 1:
        std::cout << "Read at index : ";
        std::cin >> index;
        std::cout << "Value is " << testStaticArray.read(index) << std::endl;
        break;
      case 2:
        std::cout << "Write at Index : ";
        std::cin >> index;
        std::cout << "Value : ";
        std::cin >> data;
        testStaticArray.write(data, index);
        break;
      case 3:
        std::cout << "Enter Data to insert at end : ";
        std::cin >> data;
        testStaticArray.insert(data);
        break;
      case 4:
        testStaticArray.remove();
        std::cout << "Data removed at end..." << std::endl;
        break;
      case 5:
        std::cout << "Index to insert data at : ";
        std::cin >> index;
        std::cout << "Data : ";
        std::cin >> data;
        testStaticArray.insert(data, index);
        break;
      case 6:
        std::cout << "index to remove data at : ";
        std::cin >> index;
        testStaticArray.remove(index);
        break;
      case 7:
        testStaticArray.print();
        break;
      default:
        check = 0;
        break;
    }
  }
}