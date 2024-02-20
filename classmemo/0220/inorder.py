def inorder_traverse(lst,start):
    if start<=N:
        inorder_traverse(lst,2*start)
        print(lst[start-1],end='')
        inorder_traverse(lst,2*start+1)

for t in range(10):
    N = int(input())
    bin_tree = []
    for n in range(N):
        order = input().split()
        bin_tree.append(order[1])
    print(f'#{t+1}',end=' ')
    inorder_traverse(bin_tree,1)
    print()
