with open('test1.txt', 'r') as f:
    lines = f.readlines()

si = []
sj = []

for line in lines:
    parts = line.strip().split(':')
    si.append(int(parts[0].strip()))
    sj_in = [int(x) for x in parts[1].strip().split()]
    sj.append(sj_in)


def solve1():
    res = 0
    for j in range(0,len(si)):
        sn = si[j]
        sm = sj[j]
        def rec(i,s):
            if s == 0 and i < 0:
                return True
            if s < 0 or i < 0:
                return False
        
            return rec(i-1,s-sm[i]) or rec(i-1,s/sm[i])
        
        res += sn if rec(len(sm)-1,sn) else 0
    return res

def move(n1,n2):
    return (n1 - n2)/(10**(len(str(n2))))

def solve2():
    res = 0
    for j in range(0,len(si)):
        sn = si[j]
        sm = sj[j]
        def rec(i,s):
            if s == 0 and i < 0:
                return True
            if s < 0 or i < 0:
                return False
        
            return rec(i-1,s-sm[i]) or rec(i-1,s/sm[i]) or rec(i-1,move(s,sm[i]))
        
        res += sn if rec(len(sm)-1,sn) else 0
    return res

print(solve2())
