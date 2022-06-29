'''
The difference between ascending order, descending order, 
non-ascending order, non-descending order

ascending order = increasing order: [1, 2, 3, 4, 5, 6, ....] element[i] < element[i + 1]
descending order = decreasing order: [... 6, 5, 4, 3, 2, 1]
non-descending: element[i] <= element[i + 1]
non-ascending order == non-decreasing order: [1, 2, 2, 3, 4, 4, 5, 6, 6, 6 ...]
non-descending order == non-increasing order: [... 5, 5, 4, 3, 2, 2, 2, 1]
Non-descending" means element i+1 >= element i rather than just greater than


Non-ascending (and non-descending) include the possibility of adjacent terms 
being equal. [1, 2, 2] is non-descending, but isn't ascending.

Non-decreasing order is when the numbers may or may not increase 
but they never decrease for example: [1, 2, 2, 3, 3, 4, 5, 6, 6]


------------------------------------------------------------------------
is a "non-decreasing" sequence "increasing"?:

Increasing - 1 2 3 4

Non-decreasing - 1 1 2 3

The difference being that in an increasing sequence, for x(n) and x(n+1), x(n+1) > x(n) whereas in a non-decreasing sequence, x(n+1) >= x(n)

1,2,3,4 is an increasing sequence or a non-decreasing sequence.

1,1,1,1 is a non-decreasing sequence but isn't an increasing sequence.

------------------------------------------------------------------------

'''
