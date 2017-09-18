# coding=utf-8
# author=JHZ

from __future__ import print_function

from collections import Counter
from copy import deepcopy


def edit_distance(word1, word2):
    pass


def _do_permutation(counter, length=0, result=None):
    if result is None:
        result = []

    available = [k for k, v in counter.items() if v > 0]
    if not available:
        print(result)
    else:
        for k in available:
            if length > 0 and k == result[length - 1]:
                continue
            st = 1 if len(available) > 1 else counter[k]
            for i in range(st, counter[k] + 1):
                counter[k] -= i
                result = result[:length] + [k] * i
                _do_permutation(counter, length + i, result)
                counter[k] += i


def permutation(lst):
    if not lst:
        print("lst cannot not be empty.")
        return
    count = Counter(lst)
    _do_permutation(count)


if __name__ == "__main__":
    permutation([1, 1, 1, 1])
