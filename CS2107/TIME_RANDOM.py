#!/usr/bin/env python
from __future__ import print_function
import datetime, random, sys, time

def readline():
    return sys.stdin.readline().strip()

def get_epoch_seconds(timestamp):
    return int((timestamp - datetime.datetime.utcfromtimestamp(0)).total_seconds())

def main():
    flag = "You need to interact with the server to get the prize."

    current_timestamp = datetime.datetime.utcnow()

    print("The current time is: {timestamp}".format(timestamp=current_timestamp.strftime("%Y-%m-%d %H:%M:%S")))
    print()

    t = readline()

    timestamp = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

    random.seed(get_epoch_seconds(timestamp))

    # Five attempts to guess my random number
    for i in range(1, 6):
        answer = int(random.random() * 133333333333337)
        print(str(answer))


if __name__ == "__main__":
    main()
