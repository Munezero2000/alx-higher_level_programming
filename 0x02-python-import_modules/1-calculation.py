#!/usr/bin/python3
import calculator_1.py

if __name__=="__main___":
    a= 10
    b=5
    print("{} + {}={}".format(a,b,calculator_1.add(a,b)))
    print("{} - {}={}".format(a,b, calculator_1.sub(a,b)))
    print("{} * {}={}".format(a,b, calculator_1.mul(a,b)))
    print("{} / {}={}".format(a,b, calculator_1.div(a,b)))
