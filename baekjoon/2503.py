def strike_check(n,site):
    global q_strike
    if n==int(num[site]):
        q_strike+=1

def ball_check(n,m,site):
    global q_ball
    if n==int(num[site]) or m==int(num[site]):
        q_ball+=1

N = int(input())
positive = 0
question = [list(input().split()) for _ in range(N)]
for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if x==y or y==z or z==x:
                continue
            correct = 0
            for q in question:
                num = q[0]
                strike = q[1]
                ball = q[2]
                q_strike = 0
                q_ball = 0
                strike_check(x,0)
                strike_check(y,1)
                strike_check(z,2)
                ball_check(y,z,0)
                ball_check(z,x,1)
                ball_check(x,y,2)
                if int(strike)==q_strike and int(ball)==q_ball:
                    correct+=1
                else:
                    break
            if correct==N:
                positive+=1
print(positive)



