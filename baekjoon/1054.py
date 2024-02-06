from itertools import permutations

def palindrome(s):
    for n in range(len(s)//2):
        s[n],s[-n] = s[-n-1],s[n]
    return s == s[::-1]

def count_palindrome(word):
    count = 0
    for n in range(1,len(word)+1):
        for perm in permutations(word,n):
            sentence = ' '.join(perm)
            if palindrome(sentence.replace(" ", "")):
                count += 1
    return count

N = int(input())
words = [input() for _ in range(N)]
result = count_palindrome(words)
print(result)