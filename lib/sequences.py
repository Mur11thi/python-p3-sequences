#!/usr/bin/env python3

def print_fibonacci(length):
    fibo_list=[0, 1]
    if length >1:
        for _ in range(2,length):
            fibo_list.append(fibo_list[-1] + fibo_list[-2])
        print(fibo_list)
    elif  length <1: print([])    
    else: print([0])    
print_fibonacci(9)    