/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 19th of May, 2024

    Details : Insertion Sort.


    CONCEPT :
    Sorting refers to rearrangement of a given array or list of elements
according to a comparison operator on the elements.

    Insertion sort is a simple sorting algorithm that works by iteratively
inserting each element of an unsorted list into its correct position in a sorted
portion of the list. It is a stable sorting algorithm, meaning that elements
with equal values maintain their relative order in the sorted output.

    Insertion sort is like sorting playing cards in your hands. You split the
cards into two groups: the sorted cards and the unsorted cards. Then, you pick a
card from the unsorted group and put it in the right place in the sorted group.

  Insertion Sort divides the array into parts and work on it in parts.


    i = 1, j = i - 1.
    Example : 2, 3, 4, 1, 6

  1]   2    3    4    1    6
       j    i
      j = i - 1

      if(3 < 2) then swap 3 and 2.
      NO, Move ahead.

  2]   2    3    4    1    6
            j    i

      if(4 < 3) then swap 4 and 3.
      No, also if 4 is not less than 3 then 4 can never be less than anything
left of 3. because everything is sorted in left of 3, so we are on 4.

  3]   2    3    4    1    6
                 j    i

      if( 1 < 4 ) then swap 1 and 4.
      Yes so swap 1 and 4.
      2    3    1    4    6
                j    i
      now j = j - 1.

      compare j and j+1 again., why ? because j + 1 = 1.

      if(1 < 3) then swap 1 and 3.
      2    1   3    4    6
      again
      1    2   3    4    6

  4]  1    2   3    4    6
                    j    i

      if(6 < 4) then swap 6 and 4.
      NO and as 6 > 4, anything left of 4 will be smaller than 6. because its
sorted.

This is INSERTION SORT.

*/

#include <iostream>
#include <vector>

template <class Type>
class InsertionSort {
  std::vector<Type> myArray;
  std::vector<Type> mySortedArray;

  void insertionSort() {
    mySortedArray = myArray;

    for (int i = 1; i < mySortedArray.size(); i++) {
      int j = i - 1;

      while (j >= 0 && mySortedArray[j + 1] < mySortedArray[j]) {
        Type temp = mySortedArray[j];
        mySortedArray[j] = mySortedArray[j + 1];
        mySortedArray[j + 1] = temp;

        j--;
      }
    }
  }

 public:
  void print(std::vector<Type> vectorArray) {
    for (int i = 0; i < vectorArray.size(); i++) {
      std::cout << vectorArray[i] << std::endl;
    }
  }
  void getArray() {
    Type data;
    std::cout << "Enter Values into vector Array : " << std::endl;

    int selectOption;
    int check = 1;
    while (check) {
      std::cout << " 1 for Insert" << std::endl;
      std::cout << " 2 for exit" << std::endl;
      std::cout << "Enter : ";
      std::cin >> selectOption;

      switch (selectOption) {
        case 1:
          std::cout << "Enter a value : ";
          std::cin >> data;
          myArray.push_back(data);
          break;

        default:
          check = 0;
          break;
      }
    }
  }

  void doInsertionSort() {
    if (myArray.empty()) {
      std::cout << "myArray is empty so cannot sort anything..." << std::endl;
    } else {
      insertionSort();
      std::cout << "Default Array : " << std::endl;
      print(myArray);
      std::cout << "Sorted Array : " << std::endl;
      print(mySortedArray);
    }
  }
};

int main() {
  InsertionSort<int> myInsertionSort;

  myInsertionSort.getArray();
  myInsertionSort.doInsertionSort();
  return 0;
}