# This is the program of implementing stack from list in the simplest way
stack = []

# 4 functions-push, pop, peek, isEmpty
def push(n):
    if len(stack) == n:
        return "Stack is full!"
    stack.append(eval(input()))
    return f"New stack is:{stack}"

def pop_stack():
    if isEmpty():
        return "Stack is empty"
    return f"Popped element:{stack.pop()}"

def peek():
    if isEmpty():
        return "No top is present"
    return f"Top position:{stack[-1]}"

def isEmpty():
    if not stack:
        return True
    return False

n = int(input("How many elements you want to enter in Stack?"))
while True:
    print("Enter your choice:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    ch = int(input())

    if ch == 1:
        print(push(n))
    elif ch == 2:
        print(pop_stack())
    elif ch == 3:
        print(peek())
    else:
        print("Invalid Input.")
    
    print("Would you like to continue?Y/N:")
    should_continue = input()
    if should_continue.lower() == 'n':
        break