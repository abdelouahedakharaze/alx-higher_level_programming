#!/usr/bin/python3
for wahadat in range(0, 10):
    for asharats in range(wahadat + 1, 10):
        if wahadat == 8 and asharats == 9:
            print("{}{}".format(wahadat, asharats))
        else:
            print("{}{}".format(wahadat, asharats), end=", ")
