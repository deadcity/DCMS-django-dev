## @module DCMS.sequence_tools
#  Provides some common tools for iterators.


## Returns the first item from `iterator` that passes the predicate `function`.
#
#  @arg function A function that takes a single argument and returns a boolean
#      value.
#  @arg iterator An iterable to search through.
def find (function, iterator):
    for item in iterator:
        if function(item):
            return item
