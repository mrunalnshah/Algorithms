/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 10th of May, 2024

    Details : Singly Linked List with Insert, Delete, Modify, Print Method.

    CONCEPT :
    Singly Linked List is
        -> structure with a data and a address.
        -> address points either null if last or points to next structure
   storing different data.
        -> we store head and tail address, int totalNode data also for keeping
   track of the structure.

   
        -> {5, B }   {8, C }   { 33, NULL }
             A         B           C
             A = head              C = tail
                   totalNode = 3
*/

#include <iostream>

template <class Type>
class SinglyLinkedList {
  struct SLLnode {
    Type data;
    SLLnode *next = nullptr;
  };

  int totalNode = -1;
  SLLnode *head = nullptr;
  SLLnode *tail = nullptr;

 public:
  SinglyLinkedList() {
    std::cout << "Total Nodes[starts from 0] : " << totalNode << std::endl;
    std::cout << "HEAD : " << head << std::endl;
    std::cout << "TAIL : " << tail << std::endl;
  }
  ~SinglyLinkedList() {
    std::cout << "Total Nodes[starts from 0]  : " << totalNode << std::endl;
    std::cout << "HEAD : " << head << std::endl;
    std::cout << "TAIL : " << tail << std::endl;

    SLLnode *deletingAllNodes = head;
    while (deletingAllNodes != nullptr) {
      SLLnode *next = deletingAllNodes->next;
      delete deletingAllNodes;
      deletingAllNodes = next;
      totalNode--;
    }
  }

  void insertNode(Type data) {
    if (totalNode == -1) {
      SLLnode *newNode = new SLLnode;
      newNode->data = data;
      newNode->next = nullptr;
      head = newNode;
      tail = newNode;
      totalNode++;
    } else if (totalNode > -1) {
      SLLnode *newNode = new SLLnode;
      newNode->data = data;
      newNode->next = nullptr;
      tail->next = newNode;
      tail = newNode;
      totalNode++;
    } else {
      std::cout << "Total Nodes[starts from 0] is  " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }
  void insertNode(Type data, int index) {
    if (index == 0) {
      SLLnode *newNode = new SLLnode;
      newNode->data = data;
      newNode->next = nullptr;
      if (totalNode == -1) {
        head = newNode;
        tail = newNode;
      } else {
        newNode->next = head;
        head = newNode;
      }
      totalNode++;
    } else if (index > 0 && index <= totalNode) {
      SLLnode *newNode = new SLLnode;
      newNode->data = data;
      newNode->next = nullptr;

      SLLnode *prevNode = nullptr;
      SLLnode *indexNode = nullptr;

      SLLnode *temp = head;
      for (int i = 0; i < index; i++) {
        if (i == index - 1) {
          prevNode = temp;
          indexNode = temp->next;
        }
        temp = temp->next;
      }
      prevNode->next = newNode;
      newNode->next = indexNode;
      totalNode++;
    } else if (index == totalNode + 1) {
      SLLnode *newNode = new SLLnode;
      newNode->data = data;
      newNode->next = nullptr;

      tail->next = newNode;
      tail = newNode;
      totalNode++;
    } else {
      std::cout << "Total Nodes[starts from 0] is " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }

  void deleteNode() {
    if (totalNode != -1) {
      if (totalNode == 0) {
        head = nullptr;
        tail = nullptr;
        totalNode = -1;
      } else {
        SLLnode *temp = head;

        while (temp->next != tail) {
          temp = temp->next;
        }
        temp->next = nullptr;
        delete tail;
        tail = temp;
        totalNode--;
      }
    } else {
      std::cout << "Total Nodes[starts from 0] is " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }
  void deleteNode(int index) {
    if (totalNode != -1 && index <= totalNode) {
      if (index == 0) {
        if (totalNode == 0) {
          head = nullptr;
          tail = nullptr;
          totalNode = -1;
        } else {
          head = head->next;
          totalNode--;
        }
      } else if (index > 0 && index < totalNode) {
        SLLnode *prevNode = nullptr;
        SLLnode *nextNode = nullptr;

        SLLnode *temp = head;
        for (int i = 0; i <= index; i++) {
          if (i == index - 1) {
            prevNode = temp;
          }
          if (i == index) {
            nextNode = temp->next;
          }
          temp = temp->next;
        }
        prevNode->next = nextNode;
        totalNode--;
      } else if (index == totalNode) {
        SLLnode *temp = head;

        while (temp->next != tail) {
          temp = temp->next;
        }
        temp->next = nullptr;
        tail = temp;
        totalNode--;
      } else {
        std::cout << "Total Nodes[starts from 0] is " << totalNode
                  << " and HEAD is " << head << " and TAIL is " << tail
                  << std::endl;
      }
    } else {
      std::cout << "Total Nodes[starts from 0] is " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }

  void modifyNode(Type data, int index) {
    if (totalNode != -1 && index <= totalNode) {
      SLLnode *modifyNode = head;
      for (int i = 0; i <= index; i++) {
        if (i == index) {
          modifyNode->data = data;
        }
        modifyNode = modifyNode->next;
      }
    } else {
      std::cout << "Total Nodes[starts from 0] is " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }

  void print() {
    if (totalNode != -1) {
      SLLnode *printNode = head;

      while (printNode != nullptr) {
        std::cout << printNode << " :  " << printNode->data << std::endl;
        printNode = printNode->next;
      }
    } else {
      std::cout << "Total Nodes[starts from 0] is " << totalNode
                << " and HEAD is " << head << " and TAIL is " << tail
                << std::endl;
    }
  }
};

int main() {
  SinglyLinkedList<int> singlyLinkedList;
  int data;
  int index;

  int selectOption;
  int isTrue = 1;
  while (isTrue) {
    std::cout << "Singly Linked List : " << std::endl;
    std::cout << " 1 for Insert at End " << std::endl;
    std::cout << " 2 for Insert at any Index " << std::endl;
    std::cout << " 3 for Delete at End " << std::endl;
    std::cout << " 4 for Delete at Index " << std::endl;
    std::cout << " 5 for Modify at Index " << std::endl;
    std::cout << " 6 for print whole Singly Linked List" << std::endl;
    std::cout << "anything else to end " << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;

    switch (selectOption) {
      case 1:
        std::cout << "Enter data : ";
        std::cin >> data;
        singlyLinkedList.insertNode(data);
        break;
      case 2:
        std::cout << "Enter data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        singlyLinkedList.insertNode(data, index);
        break;
      case 3:
        singlyLinkedList.deleteNode();
        break;
      case 4:
        std::cout << "Enter Index : ";
        std::cin >> index;
        singlyLinkedList.deleteNode(index);
        break;
      case 5:
        std::cout << "Enter data : ";
        std::cin >> data;
        std::cout << "Enter Index : ";
        std::cin >> index;
        singlyLinkedList.modifyNode(data, index);
        break;
      case 6:
        singlyLinkedList.print();
        break;
      default:
        isTrue = 0;
        break;
    }
  }

  return 0;
}