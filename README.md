The assignment06 file includes a MedianHeap class.
The MedianHeap class uses two heaps: a maxheap and a minheap. The maxheap (low) stores
the smaller half of the data, and the minheap (high) stores the larger half.

The elements in 'low' are always less than or equal to the elements in 'high'.
The median is the middle element of the data.

The insert method checks if new data is less than or equal to the median.
If it is, it is added to the low heap, otherwise it is added to the high heap. 

