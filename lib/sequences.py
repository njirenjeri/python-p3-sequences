#!/usr/bin/env python3

def print_fibonacci(length):
    my_fibonacci = []
    if length > 0:
        my_fibonacci.append(0)
    if length >= 2:
        my_fibonacci.append(1)
        for i in range(2, length):
            my_fibonacci.append(my_fibonacci[-1] + my_fibonacci[-2])
    print (my_fibonacci)
    pass