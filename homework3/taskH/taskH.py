class StackWithTopSum:
    def __init__(self):
        self.stack: list[int] = []
        self.total_sum: list[int] = [0, ]
        self.sum: int = 0

    def __repr__(self):
        return str(self.stack)

    def add(self, value: int) -> None:
        self.stack.append(value)
        self.total_sum.append(self.sum + value)
        self.sum += value

    def pop(self) -> int:
        to_pop = self.stack[-1]
        self.sum -= to_pop
        self.total_sum.pop()
        self.stack.pop()
        return to_pop

    def sum_top_elements(self, k: int) -> int:
        return self.sum - self.total_sum[len(self.total_sum) - k - 1]

    def process_operations(self, operations: list[str]) -> list[int]:

        results = []

        for operation in operations:
            if operation.startswith("+"):
                self.add(int(operation[1:]))
            elif operation.startswith("-"):
                results.append(self.pop())
            if operation.startswith("?"):
                top_elements = int(operation[1:])
                results.append(self.sum_top_elements(k=top_elements))

        return results


if __name__ == "__main__":
    n = int(input())
    operations = []
    for _ in range(n):
        operations.append(input())

    stack = StackWithTopSum()
    res = stack.process_operations(operations=operations)
    print(*res, sep="\n")
