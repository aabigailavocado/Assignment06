"""
CS3C: Assignment 06: Min Heap coding exercises, problem 3
Abigail Wong
"""

from MinHeap import MinHeap

class MaxHeap(MinHeap):
    def insert(self, data):
        super().insert(-data)

    def remove(self):
        return -super().remove()

    def peek(self):
        return -super().peek()

"""Explanation:
The MedianHeap class uses two heaps: a maxheap and a minheap. The maxheap (low) stores
the smaller half of the data, and the minheap (high) stores the larger half.

The elements in 'low' are always less than or equal to the elements in 'high'.
The median is the middle element of the data.

The insert method checks if new data is less than or equal to the median.
If it is, it is added to the low heap, otherwise it is added to the high heap. 
"""

class MedianHeap:
    def __init__(self, initial_data=None):
        self.low = MaxHeap()
        self.high = MinHeap()
        if initial_data:
            for item in initial_data:
                self.insert(item)

    def __len__(self):
        return len(self.low) + len(self.high)

    def __str__(self):
        return f"size={len(self)}, low={self.low}, high={self.high}"

    def insert(self, data):
        if len(self.low) == 0 or data <= self.low.peek():
            self.low.insert(data)
        else:
            self.high.insert(data)

        #balance heaps
        if len(self.low) > len(self.high) + 1:
            self.high.insert(self.low.remove())
        elif len(self.high) > len(self.low):
            self.low.insert(self.high.remove())

    def remove(self):
        if len(self) == 0:
            raise IndexError("removing from empty median heap")
        if len(self.low) >= len(self.high):
            return self.low.remove()
        else:
            return self.high.remove()

    def peek(self):
        if len(self) == 0:
            raise IndexError("peekinf from empty median heap")
        #return self.low.peek()
        if len(self.low) >= len(self.high):
            return self.low.peek()
        else:
            return self.high.peek()