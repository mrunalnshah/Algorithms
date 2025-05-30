// Author: Mrunal Nirajkumar Shah
// Date  : 30th May 2025

// Dynamic Array [ Vector STL Implementation in C++ ]

#include <iostream>

template <class TypeName>
class Vector {
 private:
  TypeName* myArray;  // Pointer to dynamically allocated array
  size_t size;        // Number of elements in the vector
  size_t capacity;    // Capacity of the vector

  void resize();  // Utility function to handle resizing

 public:
  // Default constructor
  Vector();
  // Destructor
  ~Vector();

  // Copy constructor
  Vector(const Vector& other);
  // Copy assignment operator
  Vector& operator=(const Vector& other);

  // Move constructor
  Vector(Vector&& other) noexcept;
  // Move assignment operator
  Vector& operator=(Vector&& other) noexcept;

  // Add element
  void push_back(const TypeName& element);
  // Remove last element
  void pop_back();

  size_t get_size() const;
  size_t get_capacity() const;

  TypeName& operator[](size_t index);
};

// Default constructor
template <typename T>
Vector<T>::Vector() : size(0), capacity(1) {
  myArray = new T[capacity];
}

// Destructor
template <typename T>
Vector<T>::~Vector() {
  delete[] myArray;
}

// Copy constructor
template <typename T>
Vector<T>::Vector(const Vector& other)
    : size(other.size), capacity(other.capacity) {
  myArray = new T[capacity];
  for (size_t i = 0; i < size; i++) {
    myArray[i] = other.myArray[i];
  }
}

// Copy assignment operator
template <typename T>
Vector<T>& Vector<T>::operator=(const Vector<T>& other) {
  // Self-assignment check
  if (this == &other) {
    return *this;
  }

  // Free existing memory
  delete[] myArray;

  size = other.size;
  capacity = other.capacity;
  myArray = new T[capacity];
  for (size_t i = 0; i < size; ++i) {
    myArray[i] = other.myArray[i];
  }

  return *this;
}

// Move constructor
template <typename T>
Vector<T>::Vector(Vector&& other) noexcept
    : myArray(other.myArray), size(other.size), capacity(other.capacity) {
  other.myArray = nullptr;
  other.size = 0;
  other.capacity = 0;
}

// Move assignment operator
template <typename T>
Vector<T>& Vector<T>::operator=(Vector&& other) noexcept {
  // Self-assignment check
  if (this == &other) {
    return *this;
  }

  // Release the current memory
  delete[] myArray;

  myArray = other.myArray;
  size = other.size;
  capacity = other.capacity;

  // Reset the other vector
  other.myArray = nullptr;
  other.size = 0;
  other.capacity = 0;

  return *this;
}

// Utility function to handle resizing
template <typename T>
void Vector<T>::resize() {
  capacity *= 2;

  T* newArray = new T[capacity];
  for (size_t i = 0; i < size; ++i) {
    newArray[i] = myArray[i];
  }

  delete[] myArray;

  myArray = newArray;
}

// Add element
template <typename T>
void Vector<T>::push_back(const T& element) {
  if (size == capacity) {
    resize();
  }

  myArray[size] = element;
  ++size;
}

// Remove last element
template <typename T>
void Vector<T>::pop_back() {
  if (size > 0) {
    --size;
  }
}

// allow random access
template <typename T>
T& Vector<T>::operator[](size_t index) {
  if (index >= size) {
    throw std::out_of_range("Index out of bounds");
  }
  return myArray[index];
}

// get size
template <typename T>
size_t Vector<T>::get_size() const {
  return size;
}

// get capacity
template <typename T>
size_t Vector<T>::get_capacity() const {
  return capacity;
}
