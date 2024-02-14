def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES

    if k == input:
        print(a)
    else:
        k+=1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k]=c[i]
            backtrack(a,k,input)

def construct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0]*NMAX
backtrack(a,0,3)