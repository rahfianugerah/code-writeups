"""
Quest: No zeroes for Heroes (8 Kyu)

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450   -> 145
960000 -> 96
1050   -> 105
-1050  -> -105
0      -> 0
Note: Zero should be left as it is.

"""

def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    else:
        while n % 10 == 0:
            n //= 10
        return n
    
print(no_boring_zeros(-1450))    # -145
print(no_boring_zeros(960000))  # 96