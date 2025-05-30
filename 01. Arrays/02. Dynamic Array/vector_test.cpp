// Author: Mrunal Nirajkumar Shah
// Date  : 30th May 2025

// Vector Test Code

#include "vector.h"

#include <iostream>

int main() {
  Vector<int> myVec;
  myVec.push_back(50);
  myVec.push_back(90);
  myVec.push_back(100);
  myVec.push_back(55);
  myVec.push_back(2);
  myVec.push_back(0);

  // Test copy constructor
  Vector<int> tempVec = myVec;

  // Test move constructor
  Vector<int> tempVec2 = std::move(tempVec);

  // Test copy assignment
  tempVec = tempVec2;

  // Test move assignment
  tempVec2 = std::move(tempVec);

  std::cout << "Vector elements in tempVec2: ";
  for (size_t i = 0; i < tempVec2.get_size(); ++i) {
    std::cout << tempVec2[i] << " ";
  }
  std::cout << std::endl;

  std::cout << "Size of myVec: " << myVec.get_size() << std::endl;
  std::cout << "Capacity of myVec: " << myVec.get_capacity() << std::endl;

  return 0;
}