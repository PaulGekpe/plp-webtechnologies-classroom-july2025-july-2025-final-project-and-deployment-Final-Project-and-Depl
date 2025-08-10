# calculator.py

def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Please enter a valid number (e.g., 12, 3.5, -7).")

def get_operator(prompt):
    allowed = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in allowed:
            return op
        print("Please choose one of: +  -  *  /")

def compute(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

def fmt(n):
    # Show 15 instead of 15.0, but keep decimals when needed (e.g., 2.5)
    return int(n) if isinstance(n, float) and n.is_integer() else n

def main():
    print("Basic Calculator 🧮")
    a = get_number("Enter the first number: ")
    op = get_operator("Enter an operation (+, -, *, /): ")
    b = get_number("Enter the second number: ")

    try:
        result = compute(a, op, b)
        print(f"{fmt(a)} {op} {fmt(b)} = {fmt(result)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
