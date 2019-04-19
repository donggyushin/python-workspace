import collections

lst = ['a', 'b', 'c']
print('list.pop() ->', end=' ')
while True:
    try:
        print(lst.pop(), end=' ')
    except IndexError:
        break

print()

deq = collections.deque(['a', 'b', 'c'])
print('deque.pop() ->', end=' ')
while True:
    try:
        print(deq.pop(), end=' ')
    except IndexError:
        break
