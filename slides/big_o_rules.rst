Big O notation rules
====================

Only big numbers are took into account
--------------------------------------

We are looking how this algorithm complexity grows with number of inputs, so we are looking to the numbers
close to infinity. So the case close to 0 should be ignored. We dont care that linear and quadratic has intersection at 1.

.. image:: /_static/images/close_scale.png
  :width: 400

When you add function, the less growing part could be ignored
-------------------------------------------------------------

Does y = x grows faster when y = x + 1,
or y = x\ :sup:`2` grows faster when y = x\ :sup:`2` + x?

You can see that actually they grow pretty the same. So we can simplify.
Always drop the parts that grows slower.

.. image:: /_static/images/linear_plus.png
  :width: 400

.. image:: /_static/images/quadratic_plus.png
  :width: 400


.. list-table:: Remove smaller part
   :header-rows: 1

   * - Before
     - After
   * - O(n) + O(1)
     - O(n)
   * - O(n\ :sup:`2`) + O(n)
     - O(n\ :sup:`2`)
   * - O(n\ :sup:`2`) + O(n\ :sup:`2`)
     - 2O(n\ :sup:`2`),  O(2n\ :sup:`2`)


Coefficient does not matters
----------------------------

Even on that small plot x\ :sup:`2` / 2 overrun 2x.
So we could just drop coefficients, because they does not make huge difference.

.. image:: /_static/images/coefficients_compare.png
  :width: 400

.. list-table:: Remove coefficients
   :header-rows: 1

   * - Before
     - After
   * - O(2n)
     - O(n)
   * - 2O(n)
     - O(n)
   * - 2O(n\ :sup:`2`)
     - O(n\ :sup:`2`)
   * - O(2n\ :sup:`2`)
     - O(n\ :sup:`2`)

Keep it simple
--------------

.. list-table:: Remove small parts and coefficients
   :header-rows: 1

   * - Before
     - After
   * - aO(n\ :sup:`2`) + bO(n) + c
     - O(n\ :sup:`2`)

Summary
-------

Complexity is not the execution time, you can drop less significant part easily.
The same rules that are used for comparing the function between themself are used to simplify them.
