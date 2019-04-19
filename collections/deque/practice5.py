import collections

deq = collections.deque(['a', 'b', 'c'])
deq.extendleft('de')
print(deq)
