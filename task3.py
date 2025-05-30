def is_symmetrical(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()

    return "Симетрично" if not stack else "Несиметрично"

def main():
    print("( ){[ 1 ]( 1 + 3 )( ){ }}:", is_symmetrical("( ){[ 1 ]( 1 + 3 )( ){ }}"))
    print("( 23 ( 2 - 3);:", is_symmetrical("( 23 ( 2 - 3);"))
    print("( 11 }:", is_symmetrical("( 11 }"))

if __name__ == "__main__":
    main()