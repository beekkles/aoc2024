with open('input.txt','r') as f:
    lines = f.readlines()

n = len(lines)

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    lines[i] = lines[i].strip()
    for j in range(n):
        if lines[i][j] == '.':
            matrix[i][j] = 2
        elif lines[i][j] == '#':
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

block_map = {
    0: "minecraft:gold_block",
    1: "minecraft:red_concrete",
    2: "minecraft:black_concrete"
}

commands = []

m = len(matrix)
n = len(matrix[0])

for r in range(m):
    for c in range(n):
        value = matrix[r][c]
        block = block_map.get(value, "minecraft:gold_block")

        commands.append(f"execute at @s run setblock {c} 0 {r} {block}")

        if block == "minecraft:red_concrete":
            commands.append(f"execute at @s run setblock {c} 1 {r} minecraft:red_concrete")
            commands.append(f"execute at @s run setblock {c} 2 {r} minecraft:red_concrete")
            
            commands.append(f"execute at @s run setblock {c-1} -1 {r} minecraft:blue_concrete")
            commands.append(f"execute at @s run setblock {c+1} -1 {r} minecraft:magenta_concrete")
            commands.append(f"execute at @s run setblock {c} -1 {r-1} minecraft:purple_concrete")
            commands.append(f"execute at @s run setblock {c} -1 {r+1} minecraft:cyan_concrete")


max_lines = 32000
file_count = 1
while commands:
    with open(f"generar_mapa_{file_count}.mcfunction", "w") as f:
        for _ in range(min(max_lines, len(commands))):
            f.write(commands.pop(0) + "\n")
    file_count += 1
