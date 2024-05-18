/*
    Author  : Mrunal Nirajkumar Shah
    Date    : 16th of May, 2024

    Details : Queue here is implemented using Singly Linked List with enqueue,
   dequeue and print methods.

    CONCEPT :
    Queue is
        -> FIFO : First IN First OUT
        -> structure with a data and a address.
        -> address points either null if last or points to next structure
   storing different data.
        -> we store head and tail address, int totalNode data also for keeping
   track of the structure.
        -> To enqueue, we use tail to store node, to dequeue we start from head.

        -> {5, B }   {8, C }   { 33, NULL }
             A         B           C
             A = head              C = tail
                   totalNode = 3
            Enqueue 88
            {5, B }   {8, C }   { 33, D }  {88, NULL}
             A         B           C            D
            Dequeue
            {8, C }   { 33, D }  {88, NULL}
              B           C            D
*/

#include <iostream>

template <class Type>
class Queue {
  struct SinglyLinkedList {
    Type data;
    SinglyLinkedList *next = nullptr;
  };
  SinglyLinkedList *head = nullptr;
  SinglyLinkedList *tail = nullptr;
  int totalNode = -1;

 public:
  Queue() {
    std::cout << "Total Nodes[Starts from 0, -1 is nil] : " << totalNode
              << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;
  }
  ~Queue() {
    std::cout << "Total Nodes[Starts from 0, -1 is nil] : " << totalNode
              << std::endl;
    std::cout << "Head is " << head << std::endl;
    std::cout << "Tail is " << tail << std::endl;

    while (head != nullptr) {
      SinglyLinkedList *temp = head;
      head = head->next;
      delete temp;
    }
  }
  void enqueue(Type data) {
    SinglyLinkedList *newNode = new SinglyLinkedList;
    newNode->data = data;
    newNode->next = nullptr;
    if (totalNode == -1) {
      head = newNode;
      tail = newNode;
    } else {
      tail->next = newNode;
      tail = newNode;
    }
    totalNode++;
  }

  void dequeue() {
    if (totalNode != -1) {
      if (totalNode == 0) {
        delete head;
        head = nullptr;
        tail = nullptr;
        totalNode = -1;
      } else {
        SinglyLinkedList *temp = head;
        head = head->next;
        delete temp;
        totalNode--;
      }
    } else {
      std::cout << "Total Nodes[Starts from 0, -1 is nil] : " << totalNode
                << std::endl;
    }
  }

  void print() {
    if (totalNode != -1) {
      SinglyLinkedList *travel = head;

      while (travel != nullptr) {
        std::cout << travel << "  :   " << travel->data << std::endl;
        travel = travel->next;
      }
    } else {
      std::cout << "Total Nodes[Starts from 0, -1 is nil] : " << totalNode
                << std::endl;
    }
  }
};

int main() {
  std::cout << "Queue : " << std::endl;

  Queue<int> myQueue;
  int data;

  int selectOption;
  int check = 1;
  while (check) {
    std::cout << "THIS IS QUEUE : " << std::endl;
    std::cout << " 1 for enqueue" << std::endl;
    std::cout << " 2 for dequeue" << std::endl;
    std::cout << " 3 for print queue" << std::endl;
    std::cout << " any for exit..." << std::endl;
    std::cout << "Enter : ";
    std::cin >> selectOption;
    switch (selectOption) {
      case 1:
        std::cout << "Enter Data to be enqueue : ";
        std::cin >> data;
        myQueue.enqueue(data);
        break;
      case 2:
        myQueue.dequeue();
        break;
      case 3:
        myQueue.print();
        break;
      default:
        check = 0;
        break;
    }
  }
  return 0;
}
