# 2N_sort
A simple sort that works on smaller lists that costs (number of elements in list + size of largest element)

Brad and I were discussing "best algorithms" for sorting because Dan is working through this.
This algorithm runs on iteration through the length of the list (number of elements) and then
one iteration through the size of the largest number in the list.  No nesting.

The algorithm uses what may be a sparse array (if the size of the list << the biggest number) or 
a dense array (if the size of the list ~= the biggest number).
