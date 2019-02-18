'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers

Result: 906609
'''

x = 999
palindromes = []

while x > 100:
    y = x
    while y > 100:
        z = str(x * y)
        if z == z[::-1]:
            palindromes.append(int(z))
            break
        y -= 1
    x -= 1

print(max(palindromes))
