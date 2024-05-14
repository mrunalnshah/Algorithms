/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 14th of May, 2024

    Details : Doubly Linked List with Insert, Delete, Modify, Print Method.

    CONCEPT :
    Doubly Linked List is
        -> structure with a data and two address [one pointing to previous node
   and one to next node].
        -> prevNode address points either null if last . or points to previous
   node.
        -> nextNode address points either null if last . or points to next node.
        -> we store head and tail address, int totalNode data also for keeping
   track of the structure.


        -> {null, 5 , B }   {A, 8 ,C}   {B, 33 ,NULL}
                  A             B           C
                  A = head                  C = tail
                            totalNode = 3
*/

#include <iostream>

template <class Type>
class DoublyLinkedList {
  struct DLLnode {
    Type data;
    DLLnode *prevNode = nullptr;
    DLLnode *nextNode = nullptr;
  };
  int totalNode = -1;

  DLLnode *head = nullptr;
  DLLnode *tail = nullptr;

 public:
  DoublyLinkedList() {
    std::cout << "DOUBLY LINKED LIST CREATED..." << std::endl;
    std::cout << "[Starts from 0, -1 is none] Total Node is " << totalNode
              << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
  }
  ~DoublyLinkedList() {
    std::cout << "DOUBLY LINKED LIST DESTROYED..." << std::endl;
    std::cout << "[Starts from 0, -1 is none] Total Node is " << totalNode
              << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;

    DLLnode *temp = head;
    DLLnode *next = nullptr;
    while (temp != nullptr) {
      next = temp->nextNode;
      delete temp;
      temp = next;
    }
  }
  void insertNode(Type data) {
    DLLnode *newNode = new DLLnode;
    newNode->data = data;
    if (totalNode == -1) {
      newNode->prevNode = nullptr;
      head = newNode;
    } else {
      tail->nextNode = newNode;
      newNode->prevNode = tail;
    }
    newNode->nextNode = nullptr;
    tail = newNode;

    totalNode++;
  }
  void insertNode(Type data, int index) {
    if (index == 0 && totalNode == -1) {
      DLLnode *newNode = new DLLnode;
      newNode->data = data;
      newNode->prevNode = nullptr;
      newNode->nextNode = nullptr;
      head = newNode;
      tail = newNode;

      totalNode++;
    } else if (index == 0 && totalNode > -1) {
      DLLnode *newNode = new DLLnode;
      newNode->data = data;
      newNode->prevNode = nullptr;

      head->prevNode = newNode;
      newNode->nextNode = head;
      head = newNode;

      totalNode++;
    } else if (index > 0 && totalNode == -1) {
      std::cout << "Index is " << index
                << " Total Nodes [Starts from 0, -1 is none] : " << totalNode
                << " . TAIL : " << tail << " and HEAD : " << head << std::endl;
      return;
    } else if (index > 0 && index <= totalNode) {
      DLLnode *newNode = new DLLnode;
      newNode->data = data;

      DLLnode *storeNode = new DLLnode;
      DLLnode *temp = head;
      for (int i = 0; i < index; i++) {
        if (i == index - 1) {
          storeNode = temp->nextNode;
          temp->nextNode = newNode;
          newNode->prevNode = temp;
          newNode->nextNode = storeNode;
          storeNode->prevNode = newNode;
        }
        temp = temp->nextNode;
      }
      totalNode++;
    } else if (index > 0 && index == totalNode + 1) {
      DLLnode *newNode = new DLLnode;
      newNode->data = data;

      tail->nextNode = newNode;
      newNode->nextNode = nullptr;
      tail = newNode;

      totalNode++;
    } else {
      std::cout << "Index is " << index
                << " Total Nodes[Starts from 0, -1 is none] : " << totalNode
                << " . TAIL : " << tail << " and HEAD : " << head << std::endl;
    }
  }

  void deleteNode() {
    if (totalNode != -1) {
      if (totalNode == 0) {
        head = nullptr;
        tail = nullptr;
        totalNode = -1;
      } else {
        tail = tail->prevNode;
        tail->nextNode = nullptr;
        totalNode--;
      }
    } else {
      std::cout << " Total Nodes[Starts from 0, -1 is none] : " << totalNode
                << " . TAIL : " << tail << " and HEAD : " << head << std::endl;
    }
  }
  void deleteNode(int index) {
    if (index >= 0 && totalNode != -1 && index <= totalNode) {
      if (index == 0 && totalNode == 0) {
        head = nullptr;
        tail = nullptr;
        totalNode = -1;
      } else if (index == 0 && index < totalNode) {
        head = head->nextNode;
        head->prevNode = nullptr;
        totalNode--;
      } else if (index > 0 && index < totalNode) {
        DLLnode *storeNode = new DLLnode;

        DLLnode *temp = head;
        for (int i = 0; i <= index; i++) {
          if (i == index) {
            storeNode = temp->nextNode;
            temp = temp->prevNode;
            temp->nextNode = storeNode;
            storeNode->prevNode = temp;

            totalNode--;
            return;
          }
          temp = temp->nextNode;
        }
      } else if (index > 0 && index == totalNode) {
        tail = tail->prevNode;
        tail->nextNode = nullptr;
        totalNode--;
      } else {
        std::cout << "Index is " << index
                  << " Total Nodes[Starts from 0, -1 is none] : " << totalNode
                  << " . TAIL : " << tail << " and HEAD : " << head
                  << std::endl;
      }
    } else {
      std::cout << "Index is " << index
                << " Total Nodes[Starts from 0, -1 is none] : " << totalNode
                << " . TAIL : " << tail << " and HEAD : " << head << std::endl;
    }
  }

  void modifyNode(Type data, int index) {
    if (totalNode / 2 - index >= 0) {
      DLLnode *temp = head;
      for (int i = 0; i <= index; i++) {
        if (i == index) {
          temp->data = data;
        }
        temp = temp->nextNode;
      }
    } else {
      DLLnode *temp = tail;
      for (int i = totalNode; i >= index; i--) {
        if (i == index) {
          temp->data = data;
        }
        temp = temp->prevNode;
      }
    }
  }

  void print() {
    DLLnode *temp = head;

    while (temp != nullptr) {
      std::cout << temp << " VALUE IS : " << temp->data << std::endl;
      temp = temp->nextNode;
    }
  }
};

int main() {
  DoublyLinkedList<int> dll;
  int data;
  int index;

  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "Doubly Linked List : " << std::endl;
    std::cout << "Select One Operation : " << std::endl;
    std::cout << " 1 for Insert at End " << std::endl;
    std::cout << " 2 for Insert at Index " << std::endl;
    std::cout << " 3 for Delete at End " << std::endl;
    std::cout << " 4 for Delete at Index " << std::endl;
    std::cout << " 5 for Modify at Index " << std::endl;
    std::cout << " 6 for Print Doubly Linked List " << std::endl;
    std::cout << " anyother for Exit... " << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "Enter Data : ";
        std::cin >> data;
        dll.insertNode(data);
        break;
      case 2:
        std::cout << "Enter Data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        dll.insertNode(data, index);
        break;
      case 3:
        dll.deleteNode();
        break;
      case 4:
        std::cout << "Enter Index : ";
        std::cin >> index;
        dll.deleteNode(index);
        break;
      case 5:
        std::cout << "Enter Data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        dll.modifyNode(data, index);
        break;
      case 6:
        dll.print();
        break;
      default:
        check = 0;
        break;
    }
  }

  return 0;
}