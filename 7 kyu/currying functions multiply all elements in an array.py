def multiply_all(arr):
    def multiply(n):
        return [x * n for x in arr]
    return multiply