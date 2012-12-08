#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

  Triangle     T(n) = n(n+1)/2      1, 3, 6, 10, 15, ...
  Pentagonal   P(n) = n(3n-1)/2     1, 5, 12, 22, 35, ...
  Hexagonal    H(n) = n(2n-1)       1, 6, 15, 28, 45, ...

It can be verified that T(285) = P(165) = H(143) = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
"""

def triangle(n):
  """triangle number of n"""
  return (n * (n + 1)) / 2

def pentagonal(n):
  """pentagonal number of n"""
  return (n * (3 * n - 1)) / 2

def hexagonal(n):
  """hexagonal number of n"""
  return n * (2 * n - 1)

def found_next_idxs(t, p, h):
  """
  found nexs index for satisfy property:
  triangle(t) == pentagonal(p) == hexagonal(h)
  """
  idx_t, idx_p, idx_h = t, p, h
  val_t, val_p, val_h = triangle(idx_t), pentagonal(idx_p), hexagonal(idx_h)
  while not (val_t == val_p == val_h):
    min_val = min(val_t, val_p, val_h)
    if min_val == val_t:
      idx_t += 1
      val_t = triangle(idx_t)
    elif min_val == val_p:
      idx_p += 1
      val_p = pentagonal(idx_p)
    else:
      idx_h += 1
      val_h = hexagonal(idx_h)
  return idx_t, idx_p, idx_h

def main():
  """main function"""
  t, p, h = found_next_idxs(285+1, 165, 143)
  print triangle(t)

if __name__ == "__main__":
  main()