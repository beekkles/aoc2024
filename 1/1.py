l1 = []
l2 = []

with open('input.txt','r') as file:
    for line in file:
        nums = line.strip()
        nums = nums.split()

        izq = int(nums[0])
        l1.append(izq)

        der = int(nums[1])
        l2.append(der)

    file.close()

def solve1(l1,l2):
    res = 0
    for _ in range(len(l1)):
        m1 = min(l1)
        m2 = min(l2)

        l1.remove(m1)
        l2.remove(m2)

        res += m1-m2 if m1>m2 else m2-m1
        
    return str(res)

def solve2(l1,l2):
    res = 0
    for n in l1:
        apar = 0

        for m in l2:
            if n == m:
                apar+=1
             
        res += n * apar

    return str(res)

open('output1.txt','w').write(solve1(l1[:],l2[:]))
open('output2.txt','w').write(solve2(l1,l2))