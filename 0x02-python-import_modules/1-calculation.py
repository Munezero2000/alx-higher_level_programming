#!/usr/bin/python3

if __name__=="__main___":
    from calculator_1.py import add, sub, mul, div
    """print the sum, differnce, product, and the quotiebt of 10 and 5""""
    
    a = 10
    b = 5
    
    print("{} + {}={}".format(a,b, add(a,b)))
    print("{} - {}={}".format(a,b, sub(a,b)))
    print("{} * {}={}".format(a,b, mul(a,b)))
    print("{} / {}={}".format(a,b, div(a,b)))
