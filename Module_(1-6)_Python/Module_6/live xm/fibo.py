class Fibonacci:
    def number_term(self, n):
        fib_series = [0, 1]
        for _ in range(n - 2):
            fib_series.append(fib_series[-1] + fib_series[-2])

        print(f"Fibonacci Series ({n} terms):",", ".join(map(str, fib_series[:n])))


    def maximum_value(self, max_val):
        fib_series = [0, 1]
        while True:
            next_term = fib_series[-1] + fib_series[-2]
            if next_term > max_val:
                break
            fib_series.append(next_term)
        print(f"Fibonacci Series (up to {max_val}):",", ".join(map(str, fib_series)))

    def exit(self):
        print("Goodbye!")
