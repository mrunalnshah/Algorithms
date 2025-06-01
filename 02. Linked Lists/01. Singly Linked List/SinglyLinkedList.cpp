// Author: Mrunal Nirajkumar Shah
// Date  : 1th June 2025 - 2nd June 2025(Night)

/*
    Singly Linked List:
    A Linked List is a data structure which stores the node which is comprised
   of data, and an address (minimum) pointing to the next node. This stores the
   node randomly in the memory while connecting them with each other through
   pointer address in each nodes.

    Node Structure for Singly Linked List:
    1. Data
    2. Address for Next Node (nullptr if no next node)

    Example:

    Node          :    A    B    C
    Data          :    5    6    10
    Memory Address:   $5   $1    $99

    The way to store A, B, C in sequence using linked List is
      A          B           C
    5 | B      6 | C      10 | nullptr

    This connects A->B->C->nullptr

    nullptr marks end of linked list.

    Methods:
    1. insertAtEnd
    2. removeAtEnd
    3. insertAtBegin
    4. removeAtBegin
    5. insert anywhere
    6. remove anywhere
    7. print linked list
    8. get_size
*/

#include <iostream>

template <typename DataType>
struct Node {
  DataType data;
  Node* nextNode;
};

template <class TypeName>
class SinglyLinkedList {
  Node<TypeName>* head;
  Node<TypeName>* tail;
  int size;

 public:
  SinglyLinkedList() {
    head = nullptr;
    tail = nullptr;
    size = 0;

    std::cout << "Singly Linked List Created." << std::endl;
    std::cout << "head: " << head << std::endl;
    std::cout << "tail: " << tail << std::endl;
    std::cout << "Size: " << size << std::endl;
  }
  ~SinglyLinkedList() {
    Node<TypeName>* cur = head;
    while (cur != nullptr) {
      Node<TypeName>* next = cur->nextNode;
      delete cur;
      cur = next;
    }

    std::cout << "Singly Linked List Created." << std::endl;
    std::cout << "head: " << head << std::endl;
    std::cout << "tail: " << tail << std::endl;
    std::cout << "Size: " << size << std::endl;
  }

  // Insert Data at the end of a Linked List {O(1)}
  int insertAtEnd(TypeName data) {
    Node<TypeName>* newNode = new Node<TypeName>();
    newNode->data = data;
    newNode->nextNode = nullptr;

    if (head == nullptr) {
      head = newNode;
      tail = newNode;

      size++;
      return 0;
    }

    tail->nextNode = newNode;
    tail = newNode;

    size++;
    return 0;
  }

  // Remove Data from the end of Linked Lint {O(n)}
  int removeAtEnd() {
    if (head == tail) {
      delete tail;
      head = nullptr;
      tail = nullptr;

      size = 0;
      return 0;
    }

    Node<TypeName>* cur = head;
    while (cur->nextNode != tail) {
      cur = cur->nextNode;
    }

    delete tail;
    cur->nextNode = nullptr;
    tail = cur;

    size--;
    return 0;
  }

  // Insert As First Node {O(1)}
  int insertAtBegin(TypeName data) {
    Node<TypeName>* newNode = new Node<TypeName>();
    newNode->data = data;
    newNode->nextNode = nullptr;

    if (head == nullptr) {
      head = newNode;
      tail = newNode;

      size++;
      return 0;
    }

    newNode->nextNode = head;

    head = newNode;

    size++;
    return 0;
  }

  // Remove the First Node {O(1)}
  int removeAtBegin() {
    if (head == tail) {
      delete head;
      head = nullptr;
      tail = nullptr;

      size = 0;
      return 0;
    }

    Node<TypeName>* cur = head;
    head = head->nextNode;

    delete cur;

    size--;
    return 0;
  }

  // Insert Anywhere in Linked List based on index {O(n)}
  int insert(int index, TypeName data) {
    if (index < 0 && index > size) {
      return 1;
    }

    Node<TypeName>* newNode = new Node<TypeName>();
    newNode->data = data;
    newNode->nextNode = nullptr;

    if (index == 0) {
      insertAtBegin(data);
      return 0;
    } else if (index > 0 && index <= size) {
      Node<TypeName>* cur = head;

      int i = 0;
      while (i != index - 1) {
        cur = cur->nextNode;
        i++;
      }

      newNode->nextNode = cur->nextNode;
      cur->nextNode = newNode;

      size++;
      return 0;

    } else if (index == size + 1) {
      insertAtEnd(data);
      return 0;
    } else {
      return -1;
    }
  }

  // Remove Anywhere in Linked List based on index {O(n)}
  int remove(int index) {
    if (index < 0 || index > size) {
      return 1;
    }

    Node<TypeName>* cur = head;

    if (index == 0) {
      removeAtBegin();
      return 0;
    } else if (index > 0 && index < size) {
      Node<TypeName>* cur = head;

      int i = 0;
      while (i != index - 1) {
        cur = cur->nextNode;
        i++;
      }
      Node<TypeName>* nodeToBeDeleted = cur->nextNode;
      cur->nextNode = cur->nextNode->nextNode;

      delete nodeToBeDeleted;

      size--;
      return 0;

    } else if (index == size) {
      removeAtEnd();
      return 0;
    } else {
      return -1;
    }
  }

  // Print All Linked List {O(n)}
  void print() {
    if (head == nullptr) {
      std::cout << "Empty Linked List" << std::endl;
    }

    Node<TypeName>* cur = head;

    while (cur != nullptr) {
      std::cout << "Value: " << cur->data << " -->  Address: " << cur
                << std::endl;
      cur = cur->nextNode;
    }
  }

  // get Size {O(1)}
  int get_size() { return size; }

  void errorInformation(int code) {
    if (code == 0) {
      std::cout << "Success" << std::endl;
    }

    if (code == 1) {
      std::cout << "Out of Bound" << std::endl;
    }

    if (code == -1) {
      std::cout << "Loop Finished, No Case Valid. FAILED" << std::endl;
    }
  }
};
