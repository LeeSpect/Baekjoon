# 16 6768 Don’t pass me the ball.py

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

n = int(input())
print(int(factorial(n-1)/factorial(n-4)/factorial(3)))