// Author: Mrunal Nirajkumar Shah
// Date  : 31th May 2025

// Stack Test Code

#include <iostream>

#include "Stack.cpp"

using namespace std;

int main() {
  cout << "Stack Implementation with INTEGER" << endl;

  Stack<int> mySolution;

  int data;

  bool loop = true;
  int selectOption;
  int errorCode;

  while (loop) {
    cout << "Select Option: " << endl;
    cout << "1. push_back" << endl;
    cout << "2. pop_back" << endl;
    cout << "3. peek" << endl;
    cout << "Select Option: ";
    cin >> selectOption;

    switch (selectOption) {
      case 1:
        cout << "Enter Data: ";
        cin >> data;

        errorCode = mySolution.push(data);
        break;
      case 2:
        errorCode = mySolution.pop();
        break;
      case 3:
        data = mySolution.peek();
        cout << "Peek Data: " << data << endl;

        break;
      default:
        loop = false;
        break;
    }
    mySolution.errorInformation(errorCode);
  }

  return 0;
}