#!/usr/bin/env python3

import sys
from collections import defaultdict


def count_loggers(logname):
    loggers = defaultdict(int)
    with open(logname) as logfile:
        for line in logfile:
            start_idx = line.find(']')
            if start_idx == -1:
                loggers['unknown logger'] += 1
                continue
            end_idx = line[start_idx:].find(':')
            if end_idx == -1:
                loggers['unknown logger'] += 1
                continue
            loggers[line[start_idx + 2: start_idx + end_idx - 1]] += 1
    return loggers


def usage():
    print('alice_test.py LOGFILE')


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    loggers = count_loggers(sys.argv[1])
    for logger, count in loggers.items():
        print(count, logger)


if __name__ == '__main__':
    main()
