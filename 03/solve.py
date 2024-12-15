import re

def solve1():
    with open('input.txt', 'r') as f:
        inp = f.read()

    nums = re.findall(r"mul\(-?\d+,-?\d+\)", inp)

    res = 0
    for num in nums:
        r1 =(re.findall(r"-?\d+",num))
        r1[0],r1[1] = int(r1[1]), int(r1[0])
        res += r1[0]*r1[1]

    print(res)

def solve2():
    with open("input.txt", "r") as f:
        lineas = f.readlines()

    nums = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
    res = 0
    do = True
    for line in lineas:
        for num in nums.findall(line):
            if num[0] == "do()":
                do = True
            elif num[0] == "don't()":
                do = False
            elif do:
                res += int(num[1]) * int(num[2])

    print(res)

if __name__ == "__main__":
    solve1()
    solve2()