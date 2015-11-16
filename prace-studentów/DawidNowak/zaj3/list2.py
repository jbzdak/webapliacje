#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
import unittest, math
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  mylist=[]
  for i in nums:
    if i not in mylist:
      mylist.append(i)
  return mylist


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  l1=len(list1)
  l2=len(list2)
  mylist=[]
  for i in range(l1+l2):
      if len(list1)==1 and len(list2)==1:
        if list1[0]>list2[0]:
          mylist.append(list1.pop(0))
          mylist.append(list2.pop(0))
          break
        else:
          mylist.append(list2.pop(0))
          mylist.append(list1.pop(0))
          break
      elif len(list1)==0:
        for ii in range(len(list2)):
          mylist.append(list2.pop(-1))
        break
      elif len(list2)==0:
        for ii in range(len(list1)):
          mylist.append(list1.pop(-1))
        break
      elif list2[-1]>list1[-1]:
        mylist.append(list2.pop(-1))
      elif list2[-1]<=list1[-1]:
        mylist.append(list1.pop(-1))


  mylist.reverse()
  return mylist

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'zz'], ['bb', 'cc', 'dd', 'hh', 'yy']),
       ['aa', 'bb', 'cc', 'dd', 'hh', 'yy',  'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
