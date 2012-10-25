#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pentagonal numbers are generated by the formula, P(n) = n * (3 * n - 1) / 2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P(4) + P(7) = 22 + 70 = 92 = P(8). However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P(j) and P(k), for which their sum and
difference is pentagonal and D = |P(k) - P(j)| is minimised; what is the
value of D?
"""

# global variables.
#   pentagonal number list and the list length
g_pentagonals = []
g_len = 0


def grow_pentagonal():
  """grow g_pentagonals; global pentagonal number list"""
  global g_pentagonals, g_len
  g_len += 1
  val = pentagonal(g_len)
  g_pentagonals.append(val)


def is_pentagonals(num):
  """
  check num is pentagonal
  by seaching num from global g_pentagonals list
  """
  global g_pentagonals
  return g_pentagonals.count(num) > 0


def property_pair():
  """
  search pentagonal number index pair than satisfies problem property;
  pair (k, j), P(k)+P(j) is pentagonal and P(k)-P(j) is pentagonal too.

  check only g_pentagonals last entry because repeat grow and check.
  if last entry is not satisfy the property, return None
  """
  target = g_pentagonals[-1]
  for i in range(g_len - 1):
    for j in range(i + 1, g_len - 1):
      if ((g_pentagonals[j] + g_pentagonals[i] == target) and
          is_pentagonals(g_pentagonals[j] - g_pentagonals[i])):
        return (j, i)
  return None


def pentagonal(n):
  """pentagonal number at n"""
  return (n * (3 * n - 1)) / 2


def main():
  """main function"""
  global g_pentagonals
  pair = None
  while not pair:
    grow_pentagonal()
    pair = property_pair()
  print g_pentagonals[pair[0]] - g_pentagonals[pair[1]]


if __name__ == "__main__":
  main()
