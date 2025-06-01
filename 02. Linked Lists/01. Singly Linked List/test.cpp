// Author: Mrunal Nirajkumar Shah
// Date  : 1st June 2025

// Singly Linked List Test Code

#include <iostream>

#include "SinglyLinkedList.cpp"

using namespace std;

int main() {
  cout << "Singly Linked List Implementation with INTEGER" << endl;

  SinglyLinkedList<int> mySolution;

  int data;
  int index;

  bool loop = true;
  int selectOption;
  int errorCode;

  while (loop) {
    cout << "Select Option: " << endl;
    cout << "1. Insert At End" << endl;
    cout << "2. Remove At End" << endl;
    cout << "3. Insert At Begin" << endl;
    cout << "4. Remove At Begin" << endl;
    cout << "5. Insert Any Index" << endl;
    cout << "6. Remove Any Index" << endl;
    cout << "7. Print Whole Linked List" << endl;
    cout << "Select Option: ";
    cin >> selectOption;

    switch (selectOption) {
      case 1:
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insertAtEnd(data);
        break;
      case 2:
        errorCode = mySolution.removeAtEnd();
        break;
      case 3:
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insertAtBegin(data);

        break;
      case 4:
        errorCode = mySolution.removeAtBegin();

        break;
      case 5:
        cout << "Enter Index: ";
        cin >> index;
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.insert(index, data);

        break;
      case 6:
        cout << "Enter Index: ";
        cin >> index;

        errorCode = mySolution.remove(index);

        break;
      case 7:
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