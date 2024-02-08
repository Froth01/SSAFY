import sys

N = int(sys.stdin.readline())
stack = []
for n in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif word[0] == 'push':
        stack.append(int(word[1]))
