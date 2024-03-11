# def sum_num(start,sums):
#     global min_cnt,cnt
#     sums+=nums[start]
#     cnt+=1
#     if sums>=S:
#         if min_cnt>cnt:
#             min_cnt=cnt
#             if start==len(nums)-1:
#                 return min_cnt
#         cnt=0
#     elif start==len(nums)-1:
#         return
#     else:
#         sum_num(start+1,sums)

# for n in range(N):
#     sum_num(n,0)
# if min_cnt>10:
#     print(0)
# else:
#     print(min_cnt)

N,S = map(int,input().split())
nums = list(map(int,input().split()))
if S==0:
    print(1)
    exit()
elif sum(nums)<S:
    print(0)
    exit()
min_cnt = 100001
left_p = 0
right_p = 0
sum_num = nums[0]
cnt = 1
while left_p<N-1 and right_p<N-1:
    while sum_num<S:
        right_p+=1
        sum_num+=nums[right_p]
        cnt+=1
        if right_p>=N-1:
            break
    while sum_num>=S:
        if sum_num>=S and min_cnt>cnt:
            min_cnt = cnt
        sum_num-=nums[left_p]
        left_p+=1
        cnt-=1
print(min_cnt)
