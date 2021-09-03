#!/usr/bin/env python

import sys

def statistics(args):
    stats = {}
    stats['count'] = get_count(args)
    stats['sum'] = get_sum(args)
    stats['mean'] = get_mean(args)
    return stats

def get_count(lst):
    return len(lst)

def get_sum(lst):
    return sum(lst)

def get_mean(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    print(statistics(list(map(int, sys.argv[1:]))))
