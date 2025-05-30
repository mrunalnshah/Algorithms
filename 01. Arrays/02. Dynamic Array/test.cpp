// Author: Mrunal Nirajkumar Shah
// Date  : 30th May 2025

// Dynamic Array Test Code

#include <iostream>

#include "DynamicArray.cpp"

using namespace std;

int main() {
  cout << "Dynamic Array Implementation with INTEGER" << endl;

  DynamicArray<int> mySolution;

  int index;
  int data;

  bool loop = true;
  int selectOption;
  int errorCode;

  while (loop) {
    cout << "Select Option: " << endl;
    cout << "1. Write" << endl;
    cout << "2. Insert At End" << endl;
    cout << "3. Remove At End" << endl;
    cout << "4. Insert At Begin" << endl;
    cout << "5. Remove At Begin" << endl;
    cout << "6. Insert Anywhere" << endl;
    cout << "7. Remove Anywhere" << endl;
    cout << "8. Print Whole Array" << endl;
    cout << "Select Option: ";
    cin >> selectOption;

    switch (selectOption) {
      case 1:
        cout << "Enter Index: ";
        cin >> index;
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.write(index, data);
        break;
      case 2:
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insertAtEnd(data);
        break;
      case 3:
        errorCode = mySolution.removeAtEnd();

        break;
      case 4:
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insertAtBegin(data);
        break;
      case 5:
        errorCode = mySolution.removeAtBegin();

        break;
      case 6:
        cout << "Enter Index: ";
        cin >> index;
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insert(index, data);
        break;
      case 7:
        cout << "Enter Index: ";
        cin >> index;

        errorCode = mySolution.remove(index);

        break;
      case 8:
        mySolution.print();
        break;
      default:
        loop = false;
        break;
    }
    mySolution.errorInformation(errorCode);
  }

  return 0;
}