Datastructures
==============

Information and operations over it.

Array
-----

This is the base data structure that is used to build many others.

.. image:: /_static/images/array.png
  :width: 400

The sequence of elements of fixed size where each nth element address could be found by formula
i * size, 0 is the first, size is the second, 2*size is third.

Operations
++++++++++

.. list-table:: Array operations
    :header-rows: 1

    * - Operation
      - Average Case
    * - Copy
      -  O(n)
    * - Insert
      - O(n)
    * - Get Item
      - O(1)
    * - Set Item
      - O(1)
    * - Iteration
      - O(n)
    * - Sort
      - O(n log n)
    * - x in s
      - O(n)
    * - min(s), max(s)
      - O(n)
    * - Get Length
      - O(1)

Python implementation
+++++++++++++++++++++

- `array`_,
  I have never used it in practice.
- `tuple`_,
  same fixed size, but no changes are allowed.


Dynamic array
-------------
Array that could change its size.

Also known as growable array, resizable array, dynamic table, mutable array, or array list.

Inside this is array. When you need more space it will create a new array twice bigger and copy data to it.

Now length is a number of real elements, but the capacity is a size of underlined array list.
So when length is about to exceed capacity, you have to enlarge.

.. list-table:: List operations
    :header-rows: 1

    * - Operation
      - Average Case
    * - Copy
      -  O(n)
    * - Append
      - O(1)
    * - Pop last
      - O(1)
    * - Pop intermediate
      -  O(n)
    * - Insert
      - O(n)
    * - Get Item
      - O(1)
    * - Set Item
      - O(1)
    * - Delete Item
      - O(n)
    * - Iteration
      - O(n)
    * - Extend
      - O(k)
    * - Sort
      - O(n log n)
    * - x in s
      - O(n)
    * - min(s), max(s)
      - O(n)
    * - Get Length
      - O(1)

Python implementation
+++++++++++++++++++++

- `list`_


Linked list
-----------

.. image:: /_static/images/linked_list.png
  :width: 400

A sequence of nodes with value and link to the next one.

.. list-table:: Linked list operations
    :header-rows: 1

    * - Operation
      - Average Case
    * - Copy
      - O(n)
    * - append
      - O(1)
    * - appendleft
      -	O(1)
    * - pop
      - O(1)
    * - popleft
      - O(1)
    * - extend
      - O(k)
    * - extendleft
      - O(k)
    * - remove
      - O(n)

Python implementation
+++++++++++++++++++++

- `collections.deque`_,
  this one is more complex, since have 2 links one to the child as a linked list and
  another to the parent, so you could iterate in both directions.

Summary
-------

Datastructures is an essential part of the everyday programmers life.
Knowing what is inside is a good thing.
`TimeComplexity`_ of basic Python collections, is the document that worth reading.


.. _array.array: https://docs.python.org/3/library/array.html
.. _tuple: https://docs.python.org/3/library/stdtypes.html#tuple
.. _list: https://docs.python.org/3/library/stdtypes.html#list
.. _collections.deque: https://docs.python.org/3/library/collections.html#collections.deque
.. _TimeComplexity: https://wiki.python.org/moin/TimeComplexity
