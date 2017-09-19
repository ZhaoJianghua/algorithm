# coding=utf-8
# author=JHZ

from __future__ import print_function

from collections import Counter


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


def edit_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    table = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    for i in range(len1):
        table[i + 1][0] = i + 1
    for j in range(len2):
        table[0][j + 1] = j + 1

    for i in range(len1):
        for j in range(len2):
            fij = 0 if word1[i] == word2[j] else 1
            table[i + 1][j + 1] = min(table[i + 1][j] + 1,
                                      table[i][j + 1] + 1,
                                      table[i][j] + fij)

    return table[len1][len2]


if __name__ == "__main__":
    print("permutation of number list [1, 1, 2]:")
    permutation([1, 1, 2])

    dis = edit_distance("kitten", "sitting")
    print("edit distance between 'kitten' and 'sitting' is %s." % dis)
