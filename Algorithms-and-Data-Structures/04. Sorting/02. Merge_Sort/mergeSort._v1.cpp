/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 23th of May, 2024

    Details : Merge Sort.


    CONCEPT :
    Sorting refers to rearrangement of a given array or list of elements
according to a comparison operator on the elements.

    Merge sort is a sorting algorithm that follows the divide-and-conquer
approach. It works by recursively dividing the input array into smaller
subarrays and sorting those subarrays then merging them back together to obtain
the sorted array.

    In simple terms, we can say that the process of merge sort is to divide the
array into two halves, sort each half, and then merge the sorted halves back
together. This process is repeated until the entire array is sorted.

    [Divide and Conquer]

    Example : 2, 3, 4, 1, 6

       2    3    4    1    6
       2    3    4 |  1    6  [Divide into 2]
       2    3 |  4 |  1  | 6  [Furthur Divide into 2]
       2  | 3 |  4 |  1  | 6  [we are at individual level, so return arr]

       2   3  | 4  |  1  | 6  [merge and return]
       2   3    4  |  1  | 6  [merge and return]
       2   3    4  |  1    6  [merge and retunr]
       1   2    3     4    6  [ merger and return, final end!]

    This is merge Sort.


*/

#include <iostream>
#include <vector>

template <class Type>
class MergeSort {
  std::vector<Type> myArray;
  std::vector<Type> mySortedArray;

  void merge(std::vector<Type>& arr, int start, int middle, int end) {
    std::vector<Type> Left = {arr.begin() + start, arr.begin() + middle + 1};
    std::vector<Type> Right = {arr.begin() + middle + 1, arr.begin() + end + 1};

    int i = 0;
    int j = 0;
    int k = start;

    while (i < Left.size() && j < Right.size()) {
      if (Left[i] <= Right[j]) {
        arr[k] = Left[i];
        i++;
      } else {
        arr[k] = Right[j];
        j++;
      }
      k++;
    }

    while (i < Left.size()) {
      arr[k] = Left[i];
      i++;
      k++;
    }

    while (j < Right.size()) {
      arr[k] = Right[j];
      j++;
      k++;
    }
  }

  std::vector<Type> mergeSort(std::vector<Type>& arr, int start, int end) {
    if (end - start + 1 <= 1) {
      return arr;
    }
    int middle = (start + end) / 2;

    mergeSort(arr, start, middle);
    mergeSort(arr, middle + 1, end);

    merge(arr, start, middle, end);

    return arr;
  }

 public:
  void insert_into_array(Type data) { myArray.push_back(data); }

  void apply_mergeSort() {
    int start = 0;
    int end = myArray.size() - 1;
    mySortedArray = myArray;
    if (mySortedArray.empty()) {
      std::cout << "\n\nEmpty myArray " << std::endl;
    } else {
      mergeSort(mySortedArray, start, end);

      std::cout << " Default Array is " << std::endl;
      print_array(myArray);
      std::cout << " Sorted Array is " << std::endl;
      print_array(mySortedArray);
    }
  }

  void print_array(std::vector<Type> arr) {
    for (int i = 0; i < arr.size(); i++) {
      std::cout << arr[i] << std::endl;
    }
  }
};

int main() {
  MergeSort<int> mySort;
  int data;

  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "Merge Sort : " << std::endl;

    std::cout << "1 for Push into myArr" << std::endl;
    std::cout << "2 for Sorting" << std::endl;
    std::cout << "anyother for exiting" << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;
    switch (selectOption) {
      case 1:
        std::cout << "Enter Data : ";
        std::cin >> data;
        mySort.insert_into_array(data);
        break;
      case 2:
        mySort.apply_mergeSort();
        break;
      default:
        check = 0;
        break;
    }
  }

  return 0;
}