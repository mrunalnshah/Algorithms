// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 23 September 2024

/*
  Singly Linked List
    Singly Linked List is a data structure which is used to store data in
  unordered memory  while maintaining its address to fetch it in ordered way.

    Mostly Singly Linked list contains :
      1. Data
      2. Addressess for next and/or previous Singly Linked List

       5   6   7   9
      $5  $7  $2  $11

      When storing using Singly Linked List, we see

        $5  -- 5 & $7
        $7  -- 6 & $2
        $2  -- 7 & $11
        $11 -- 9 & nullptr
        nullptr because, its last element in Linked List, so we use nullptr to
  bifurcate.

     Implementing this Singly Linked List, requires :
      1. head : to maintain start
      2. tail : to maintain end
      3. totalIndex : to know how many index
      4. SinglyLinkedList : to store data and address.

     Functions :
      1. insert(data) [ O(1) ] : insert data at the tail.
      2. insert(index,data) [ (O(n) ] : insert data at any index, from head to
  tail.
      3. remove() [ O(n) ]  : remove last index, of tail.
      4. remove(index) [ O(n) ]: remove any index between head to tail
      5. print()  [ O(n) ]: prints whole array from head to tail.

   void errorCode(int code);
     0 -> success
     1 -> out of bound index
     2 -> index == -1
     -1 -> out of if-else case
     -2 -> node doesnt exist

     Thanks for reading my code
     Mrunal Nirajkumar Shah.
*/

#include <iostream>

template <class Typename>
class SinglyLinkedList {
  struct SLL {
    Typename data;
    SLL *next;
  };
  SLL *head = nullptr;
  SLL *tail = nullptr;
  int totalIndex = -1;

 public:
  // Constructor Created with initializing a Singly Linked List.
  SinglyLinkedList() {
    std::cout << "Creating Singly Linked List Class." << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
    std::cout << "Total Index is " << totalIndex << std::endl;
  }
  // Destructor destroying the Singly Linked List and ending the implementation
  // at end.
  ~SinglyLinkedList() {
    std::cout << "Destroying Singly Linked List Class." << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
    std::cout << "Total Index is " << totalIndex << std::endl;

    SLL *curNode = head;
    while (curNode != nullptr) {
      SLL *nextNode = curNode->next;
      delete curNode;
      curNode = nextNode;
    }
  }
  // Insert data at the end. [ O(1) ]
  int insert(Typename data) {
    SLL *newNode = new SLL;
    newNode->data = data;
    newNode->next = nullptr;

    if (head == nullptr && tail == nullptr) {
      head = newNode;
      tail = newNode;
    } else {
      tail->next = newNode;
      tail = newNode;
    }
    totalIndex++;

    return 0;
  }
  // Insert data at any position in Singly Linked List [ O(n) ]
  int insert(Typename data, int index) {
    if (index < 0 || index > totalIndex + 1) {
      return 1;
    }
    SLL *newNode = new SLL;
    newNode->data = data;
    newNode->next = nullptr;

    if (index == 0) {
      if (head == nullptr && tail == nullptr) {
        head = newNode;
        tail = newNode;
      } else {
        newNode->next = head;
        head = newNode;
      }
    } else if (index > 0 && index <= totalIndex) {
      SLL *curNode = head;
      int i = 0;
      while (i != index - 1) {
        curNode = curNode->next;
        i++;
      }
      newNode->next = curNode->next;
      curNode->next = newNode;
    } else if (index == totalIndex + 1) {
      tail->next = newNode;
      tail = newNode;
    } else {
      return -1;
    }
    totalIndex++;
    return 0;
  }
  // Remove data from the tail. [ O(1) ]
  int remove() {
    if (totalIndex == -1) {
      return 2;
    }
    if (head == tail) {
      delete head;
      head = nullptr;
      tail = nullptr;
    } else {
      SLL *curNode = head;
      while (curNode->next != tail) {
        curNode = curNode->next;
      }
      delete tail;
      tail = curNode;
      tail->next = nullptr;
    }
    totalIndex--;
    return 0;
  }

  // Remove data from any position between head and tail. [ O(n) ]
  int remove(int index) {
    if (index == -1) {
      return 2;
    }
    if (index > totalIndex) {
      return 1;
    }

    if (index == 0) {
      SLL *temp = head;
      if (head == tail) {
        delete head;
        head = nullptr;
        tail = nullptr;
      } else {
        head = head->next;
        delete temp;
      }
      totalIndex--;
      return 0;
    }

    SLL *curNode = head;

    for (int i = 0; i < index - 1; i++) {
      if (curNode == nullptr) {
        return 1;
      }
      curNode = curNode->next;
    }
    SLL *nodeToDelete = curNode->next;
    if (nodeToDelete == nullptr) {
      return -2;
    }
    curNode->next = nodeToDelete->next;

    if (nodeToDelete == tail) {
      tail = curNode;
    }
    delete nodeToDelete;
    totalIndex--;
    return 0;
  }

  // Print whole Linked list from head to tail. [ O(n) ]
  int print() {
    if (totalIndex == -1) {
      return 2;
    }
    SLL *curNode = head;
    while (curNode != nullptr) {
      std::cout << curNode << " : " << curNode->data << std::endl;
      curNode = curNode->next;
    }
    return 0;
  }

  // Printing ErrorCode [ O(1) ]
  void errorCode(int code) {
    if (code == 1) {
      std::cout << "Out of Bound." << std::endl;
    }
    if (code == 2) {
      std::cout << "totalIndex is -1" << std::endl;
    }

    if (code == -1) {
      std::cout << "out of cases in if-else" << std::endl;
    }
    if (code == -2) {
      std::cout << "Node doesnt exist." << std::endl;
    }
  }
};

int main() {
  std::cout << "Singly Linked List\n" << std::endl;

  SinglyLinkedList<int> mySinglyLinkedList;
  int data;
  int index;

  int code;

  int selectOption;
  bool isTrue = true;
  while (isTrue) {
    std::cout << "Singly Linked List." << std::endl;
    std::cout << "1. Insert at end" << std::endl;
    std::cout << "2. Insert at any position" << std::endl;
    std::cout << "3. Remove at end" << std::endl;
    std::cout << "4. Remove at any position" << std::endl;
    std::cout << "5. Print whole linked List" << std::endl;
    std::cout << "6+. Exit" << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "Enter Data : ";
        std::cin >> data;
        code = mySinglyLinkedList.insert(data);
        break;
      case 2:
        std::cout << "Enter Data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        code = mySinglyLinkedList.insert(data, index);
        break;
      case 3:
        code = mySinglyLinkedList.remove();
        break;
      case 4:
        std::cout << "Enter Index : ";
        std::cin >> index;
        code = mySinglyLinkedList.remove(index);
        break;
      case 5:
        code = mySinglyLinkedList.print();
        break;
      default:
        isTrue = false;
    }
    mySinglyLinkedList.errorCode(code);
  }
  return 0;
}