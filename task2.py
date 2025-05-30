from collections import deque

def is_palindrome(text):
    normalized_text = ''.join(char.lower() for char in text if char.isalnum())
    dq = deque(normalized_text)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

def main():
    print(is_palindrome('Anna'))
    print(is_palindrome('qq'))
    print(is_palindrome('quest'))

if __name__ == "__main__":
    main()