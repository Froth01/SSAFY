def check(case):
    year = int(case[:4])
    month = int(case[4:6])
    day = int(case[6:])
    if year == 0 or month > 12 or month == 0 or day > 31 or (month == 2 and day > 28) or (month in {'04','06','09','11'} and day > 30) :
        return None
    return f'{year:04d}/{month:02d}/{day:02d}'

if __name__ == "__main__":
    T = int(input())
    for test_case in range(T):
        case = str(input())
        if check(case) == None :
            print(f'#{test_case+1} {-1}')
        else : 
            print(f'#{test_case+1} {check(case)}')