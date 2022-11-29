# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300
first = 2
second = 1
print(first)
print(second)
ans = first+second
print(ans)
while ans < 300:
    first = ans
    ans = ans+second
    print(ans)
    second = ans
    answer = ans+first
    print(ans)