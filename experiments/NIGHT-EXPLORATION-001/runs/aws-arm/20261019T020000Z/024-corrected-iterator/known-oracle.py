#!/usr/bin/env python3
import json

def recurrence(a,b,seed,n):
    mask=(1<<64)-1;ma,mb=1,0
    while n:
        if n&1:ma,mb=(a*ma)&mask,(a*mb+b)&mask
        a,b=(a*a)&mask,(a*b+b)&mask;n//=2
    return (ma*seed+mb)&mask

print(json.dumps(dict(rounds=100000000,before=f'{recurrence(6364136223846793005,1442695040888963407,1,100000000):016x}',inside=f'{recurrence(2862933555777941757,3037000493,3,100000000):016x}',after=f'{recurrence(6364136223846793005,1442695040888963407,7,100000000):016x}')))
