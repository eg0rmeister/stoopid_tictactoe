#include <iostream>
#include <optional>
#include <stack>
#include <vector>

template <typename T>
class HeapMax {
 public:
  void Insert(T value) {
    heap_.push_back(value);
    SiftUp(size_);
    size_++;
  }
  std::optional<T> ExtractMax() {
    if (size_ == 0) {
      return std::nullopt;
    }
    size_--;
    std::swap(heap_[0], heap_[size_]);
    T ret = heap_.back();
    heap_.pop_back();
    SiftDown(0);
    return std::optional<T>(ret);
  }
  std::optional<T> GetMax() {
    if (size_ == 0) {
      return std::nullopt;
    }
    return heap_[0];
  }
  size_t Size() { return size_; }

 private:
  std::vector<T> heap_;
  size_t size_ = 0;
  void SiftDown(size_t index);
  void SiftUp(size_t index);
};

template <typename T>
void HeapMax<T>::SiftDown(size_t index) {
  size_t to_swap_index = index;
  if (2 * index + 1 < size_ && heap_[2 * index + 1] > heap_[to_swap_index]) {
    to_swap_index = 2 * index + 1;
  }
  if (2 * index + 2 < size_ && heap_[2 * index + 2] > heap_[to_swap_index]) {
    to_swap_index = 2 * index + 2;
  }
  if (to_swap_index == index) {
    return;
  }
  std::swap(heap_[index], heap_[to_swap_index]);
  SiftDown(to_swap_index);
}

template <typename T>
void HeapMax<T>::SiftUp(size_t index) {
  if (index == 0) {
    return;
  }
  if (heap_[(index - 1) / 2] < heap_[index]) {
    std::swap(heap_[index], heap_[(index - 1) / 2]);
    SiftUp((index - 1) / 2);
  }
}

int main() {
  HeapMax<std::uint64_t> heap;
  std::uint64_t size_of_sequence;
  std::uint64_t to_out_amount;
  std::uint64_t a0;
  std::uint64_t x;
  std::uint64_t y;
  std::cin >> size_of_sequence >> to_out_amount >> a0 >> x >> y;
  std::uint64_t curr = a0;
  for (std::uint64_t i = 0; i < size_of_sequence; ++i) {
    curr = (x * curr + y) % (1073741824ull);
    if (heap.Size() >= to_out_amount) {
      if (heap.GetMax() > curr) {
        heap.ExtractMax();
        heap.Insert(curr);
      }
    } else {
      heap.Insert(curr);
    }
  }
  std::stack<std::uint64_t> out;
  while (heap.Size() != 0) {
    out.push(heap.ExtractMax().value());
  }
  while (!out.empty()) {
    std::cout << out.top() << " ";
    out.pop();
  }
  std::cout << "\n";
  return 0;
}
