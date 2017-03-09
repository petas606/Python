#!/usr/bin/env python3

import sys

# Zeit:

import time
time.time()
# OUT: 1444327310.2887266
time.localtime()
# OUT: time.struct_time(tm_year=2015, tm_mon=10, tm_mday=8, tm_hour=20,
# tm_min=2, tm_sec=11, tm_wday=3, tm_yday=281, tm_isdst=1)
time.localtime()[0]
# OUT: 2015
list(time.localtime())
# OUT: [2015, 10, 8, 20, 3, 1, 3, 281, 1]
time.localtime().tm_year
# OUT: 2015

# Ladebalken:

import time
while True:
    print(".", end="")
    sys.stdout.flush()
    time.sleep(1)
# OUT: ...........................................
