#!/usr/bin/env python

import sys

def statistics(args):
    stats = {}
    stats['count'] = get_count(args)
    stats['sum'] = get_sum(args)
    stats['mean'] = get_mean(args)
    stats['median'] = get_median(args)
    return stats

def get_count(lst):
    return len(lst)

def get_sum(lst):
    return sum(lst)

def get_mean(lst):
    return sum(lst) / len(lst)

def get_median(lst):
    lst.sort()
    return lst[round(len(lst)/2)]

if __name__ == '__main__':
    print(statistics(list(map(int, sys.argv[1:]))))
