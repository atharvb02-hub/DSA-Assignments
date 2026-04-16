# Data Structures - Unit 1 Assignment

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Factorial (Recursive)

def factorial(n):
    if n < 0:
        return "Invalid input (negative number)"
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Fibonacci

def fibonacci(n):
    if n < 0:
        return "Invalid input (negative number)"
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Tower of Hanoi

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)

# Recursive Binary Search

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)



def main():
    print("====== AERT TOOLKIT OUTPUT ======\n")

    print("FACTORIAL TESTS:")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) =", factorial(n))

    print("\n")

    print("FIBONACCI TESTS:")
    for n in [5, 10, 20, 30]:
        print(f"fibonacci({n}) =", fibonacci(n))

    print("\n")
    
    print("TOWER OF HANOI (N=3):")
    hanoi_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', hanoi_stack)

    print("\nTotal Moves Stored in Stack:", hanoi_stack.size())
    print("\n")


    print("BINARY SEARCH TESTS:")
    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        bs_stack = StackADT()
        index = binary_search(arr, key, 0, len(arr) - 1, bs_stack)
        print(f"\nSearching {key} -> Index:", index)
        print("Mid indices visited:", bs_stack.items)

    empty_arr = []
    bs_stack = StackADT()
    index = binary_search(empty_arr, 5, 0, -1, bs_stack)
    print("\nSearching in empty array -> Index:", index)


if __name__ == "__main__":
    main()