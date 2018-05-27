The ILP Manager class
=====================
|
|


ILP Formulation
***************
|

This class models Euler's 185th riddle with the following Integer Linear Problem:

 Let :math:`\left\{ x_{i,c}\right\} _{i\in[m],c\in[10]}` be binary variables indicating \
 the color of the digits in :math:`s^{*}`, that is: \
 :math:`x_{j,c}=1\thinspace\thinspace\iff\thinspace\thinspace v_{j}^{*}=c`.

 Since each vertex in :math:`s^{*}` has only one color, we get the constraints: \
 :math:`\left\{ \sum_{c=0}^{9}x_{j,c}=1\right\} _{j\in[m]}`

 And from the input of correct vertices we get the constraints: \
 :math:`\left\{ \sum_{j\in[m]}x_{j,v_{j}^{\left(i\right)}}=d^{\left(i\right)}\right\} _{i\in[n]}`

 Since we are guarantied that only one solution exists, we can put a dummy objective function of our choice, \
 and solve the ILP to get the unique solution.

|

Class Methods
######################################################

.. Notice the markers line is longer than the headline.
.. It is allowed. but markers lines shorter than headlines are not allowed.
..
   Notice further: each time you change the type of heading marker
   (here we started with =, then * then #)
   The heading level drops (heading 1 => heading 2 => etc.)

|

.. autoclass:: src.ilp_manager.ILPManager

|
|

This page was generated using this .rst code:
*********************************************

|

.. literalinclude:: ilp_manager.rst

|
|

:ref:`Return Home <mastertoc>`
