from functools import cache

@cache
def fib(n):
    print("adsad", n)
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    print(fib(10))
    print(fib(11))
    print(fib(9))

if __name__ == '__main__':
    main()