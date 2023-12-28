
def main():
    fib = [1, 2]
    sum = 2

    while fib[len(fib) - 1] <= 4000000:
        num = fib[len(fib) - 1] + fib[len(fib) - 2]
        if num % 2 == 0:
            sum += num
        fib.append(num)

    print(sum)

if __name__ == "__main__":
    main()