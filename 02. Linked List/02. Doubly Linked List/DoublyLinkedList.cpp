// AUTHOR : Mrunal Nirajkumar Shah
// DATE   : 18 October 2024

/*
  Doubly Linked List
    Doubly Linked List is a data structure which is used to store data in
  unordered memory  while maintaining its address to fetch it in ordered way.

    Mostly Doubly Linked list contains :
      1. Data
      2. Two Addressess for next and previous Doubly Linked List

       5   6   7   9
      $5  $7  $2  $11

      When storing using Doubly Linked List, we see
                    (prevNode , nextNode)
        $5  -- 5 & (nullptr ,  $7)
        $7  -- 6 & ($5 , $2)
        $2  -- 7 & ($7 , $11)
        $11 -- 9 & ($2, nullptr)
        nullptr because, its first elements's prevNode and last element's
  nextNode is empty in Linked List, so we use nullptr to bifurcate.

     Implementing this Doubly Linked List, requires :
      1. head : to maintain start
      2. tail : to maintain end
      3. totalIndex : to know how many index
      4. DoublyLinkedList : to store data and two address : prevNode and
  nextNode.

     Functions :
      1. insert(data) [ O(1) ] : insert data at the tail.
      2. insert(index,data) [ (O(n) ] : insert data at any index, from head to
  tail.
      3. remove() [ O(n) ]  : remove last index, of tail.
      4. remove(index) [ O(n) ]: remove any index between head to tail
      5. print()  [ O(n) ]: prints whole array from head to tail.

   void errorCode(int code);
     0 -> success
     1 -> Index Out of Bound
     2 -> index == -1
     -1 -> out of if-else case
     -2 -> Main Ended with some error

     Thanks for reading my code
     Mrunal Nirajkumar Shah.
*/

#include <iostream>

template <class typeName>
class DoublyLinkedList {
  struct DLL {
    typeName data;
    DLL* prevNode;
    DLL* nextNode;
  };
  DLL* head = nullptr;
  DLL* tail = nullptr;
  int totalIndex = -1;

 public:
  // Constructor Created with initializing a Doubly Linked List.
  DoublyLinkedList() {
    std::cout << "Creating Doubly Linked List Class." << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
    std::cout << "Total Index is " << totalIndex << std::endl;
  }

  // Destructor destroying the Doubly Linked List and ending the implementation
  // at end.
  ~DoublyLinkedList() {
    std::cout << "Destroying Doubly Linked List Class." << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
    std::cout << "Total Index is " << totalIndex << std::endl;

    DLL* curNode = head;
    while (curNode != nullptr) {
      DLL* nextNode = curNode->nextNode;
      delete curNode;
      curNode = nextNode;
    }
  }

  // Insert data at the end. [ O(1) ]
  int insert(typeName data) {
    DLL* newNode = new DLL;
    newNode->data = data;
    newNode->nextNode = nullptr;
    newNode->prevNode = nullptr;

    if (totalIndex == -1) {
      head = newNode;
      tail = newNode;
    } else {
      tail->nextNode = newNode;
      newNode->prevNode = tail;
      tail = tail->nextNode;
    }
    totalIndex++;
    return 0;
  }

  // Insert data at any position in Doubly Linked List [ O(n) ]
  int insert(typeName data, int index) {
    if (index < 0 || index > totalIndex + 1) {
      return 1;
    }
    DLL* newNode = new DLL;
    newNode->data = data;
    newNode->nextNode = nullptr;
    newNode->prevNode = nullptr;

    if (index == 0) {
      if (head == nullptr && tail == nullptr) {
        head = newNode;
        tail = newNode;
      } else {
        head->prevNode = newNode;
        newNode->nextNode = head;
        head = newNode;
      }
    } else if (index > 0 && index <= totalIndex) {
      DLL* curNode = head;
      int i = 0;
      while (i != index) {
        curNode = curNode->nextNode;
        i++;
      }
      newNode->prevNode = curNode->prevNode;
      newNode->nextNode = curNode;
      curNode->prevNode->nextNode = newNode;
      curNode->prevNode = newNode;
    } else if (index == totalIndex + 1) {
      tail->nextNode = newNode;
      newNode->prevNode = tail;
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
      DLL* temp = tail;
      tail = tail->prevNode;
      tail->nextNode = nullptr;
      delete temp;
    }
    totalIndex--;
    return 0;
  }

  // Remove data from any position between head and tail. [ O(n) ]
  int remove(int index) {
    if (totalIndex == -1) {
      return 2;
    }
    if (index < 0 || index > totalIndex) {
      return 1;
    }

    if (index == 0) {
      DLL* temp = head;
      if (head == tail) {
        head = nullptr;
        tail = nullptr;
      } else {
        head = head->nextNode;
        head->prevNode = nullptr;
      }
      delete temp;
    } else if (index > 0 && index < totalIndex) {
      DLL* curNode = head;

      int i = 0;
      while (i != index) {
        curNode = curNode->nextNode;
        i++;
      }
      curNode->prevNode->nextNode = curNode->nextNode;
      curNode->nextNode->prevNode = curNode->prevNode;

      delete curNode;
    } else if (index == totalIndex) {
      DLL* temp = tail;
      tail = tail->prevNode;
      if (tail) {
        tail->nextNode = nullptr;
      } else {
        head = nullptr;
      }
      delete temp;
    } else {
      return -1;
    }
    totalIndex--;
    return 0;
  }

  // Print whole Linked list from head to tail. [ O(n) ]
  int print() {
    if (totalIndex == -1) {
      return 2;
    }
    DLL* curNode = head;
    while (curNode != nullptr) {
      std::cout << curNode << " : " << curNode->data << std::endl;
      curNode = curNode->nextNode;
    }
    return 0;
  }

  // Printing ErrorCode [ O(1) ]
  void errorCode(int code) {
    if (code == -2) {
      std::cout << "ERROR(-2) : MAIN ENDED WITH SOME ERROR " << std::endl;
    }
    if (code == -1) {
      std::cout << "ERROR(-1) : OUT OF BOUND IF CASE " << std::endl;
    }
    if (code == 1) {
      std::cout << "ERROR(1) : Index Out of Bound " << std::endl;
    }
    if (code == 2) {
      std::cout << "ERROR(2) : Total Index is -1" << std::endl;
    }
  }
};

int main() {
  std::cout << "Doubly Linked List\n" << std::endl;

  DoublyLinkedList<int> myDoublyLinkedList;
  int data;
  int index;

  int code;

  int selectOption;
  bool isTrue = true;
  while (isTrue) {
    std::cout << "Doubly Linked List." << std::endl;
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
        code = myDoublyLinkedList.insert(data);
        break;
      case 2:
        std::cout << "Enter Data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        code = myDoublyLinkedList.insert(data, index);
        break;
      case 3:
        code = myDoublyLinkedList.remove();
        break;
      case 4:
        std::cout << "Enter Index : ";
        std::cin >> index;
        code = myDoublyLinkedList.remove(index);
        break;
      case 5:
        code = myDoublyLinkedList.print();
        break;
      default:
        isTrue = false;
        return 0;
    }
    myDoublyLinkedList.errorCode(code);
  }
  return -2;
}