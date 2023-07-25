# Important general assumptions/notes (more are in code):

- Assumed question is asking for timespan between start of the filling process
and end of filling the last bottle to be filled, rather than the sum 
of times to fill each bottle for example.

- Optimising for worst-case time and auxiliary space complexity, prioritising 
the former in the case of trade-offs.

- Have chosen to implement the SLAP style for function reusability and 
readability.

- Assuming I shouldn't modify the arrays input to the functions being 
asked for, in order to make the functions pure and in case said arrays 
are used elsewhere.

- Assuming system can handle all numbers involved however large they 
become.

- Assuming that, wherever I am asked in the Bonus questions to adapt 
my previous function slightly, this means the first function with 
input validation, so it does the exact same things if applicable but with 
extra features.

- Written using Python 3.9.

- Units:
  - Sizes and volumes: ml
  - Time: seconds
  - Flow rate: ml per second

- Used heap to minimise the worst-case time complexities of the requested 
functions. The worst-case complexities are, in Big-O notation, where m is 
the number of bottles and n the number of taps:
  - Time: O(mlog(n) + n)
  - Auxiliary space: O(n)