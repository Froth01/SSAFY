def turn90(a):
    group1 = []
    for x in range(N):
        source = all_list[N-1-x][a]
        group1.append(source)
        result = ''.join(group1)
    return result
def turn180(a):
    group2 = []
    for x in range(N):
        source = all_list[N-1-a][N-1-x]
        group2.append(source)
        result = ''.join(group2)
    return result
def turn270(a):
    group3 = []
    for x in range(N):
        source = all_list[0+x][N-1-a]
        group3.append(source)
        result = ''.join(group3)
    return result

if __name__ == "__main__":
    test_case = int(input())
    for test in range(test_case):
        all_list = []
        N = int(input())
        for n in range(N):
            all_list.append(list(input().split()))
        print(f'#{test_case+1}')
        for a in range(N):
            print(f'{turn90(a)} {turn180(a)} {turn270(a)}')