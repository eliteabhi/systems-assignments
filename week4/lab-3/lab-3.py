from time import time

def fibonacci( n: int ) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci( n-1 ) + fibonacci( n-2 )

def fibonacci_memo( n: int ) -> int:
    memo = {0: 0, 1: 1}
    def fib( n ):
        if n not in memo:
            memo[n] = fib( n-1 ) + fib( n-2 )
        return memo[n]
    return fib( n )

# ----------------------------------------------------------------

start_time = time()
fib= fibonacci( 40 )
fib_naive_time = time() - start_time

start_time = time()
fib = fibonacci_memo( 40 )
fib_memo_time = time() - start_time

print(f"Fib Naive time: { fib_naive_time } seconds")
print(f"Fib Memo time: { fib_memo_time } seconds")
