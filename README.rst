Levenshtein package
===================

The Levenshtein distance is a string metric for measuring the difference
between two strings. With this package you can calculate the Levenshtein
distance and ratio between two words, or get the most similar word in a
list of words.


More info at
https://en.wikipedia.org/wiki/Levenshtein_distance

Installation
------------

.. code:: bash

   pip install levenshtein-package

Available methods
-----------------

-  ``calculate_distance``
-  ``calculate_similarity``
-  ``get_most_similar_in_list``

Examples
--------

.. code:: python

   >>> from levenshtein import calculate_distance, calculate_similarity, get_most_similar_in_list

   >>> calculate_distance("apple", "pear")
   4

   >>> calculate_similarity("apple", "pear")
   0.4444444444444444

   >>> get_most_similar_in_list("apple", ["pear", "peach", "apricot", "banana"])
   'pear'