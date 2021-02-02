n = int(input())
uniforms = []

output = 0

for _ in range(n):
    h, a = map(int, input().split())
    uniforms.append([h, a])

for i in range(len(uniforms) - 1):
    for j in range(i + 1, len(uniforms)):
        output += int(uniforms[i][0] == uniforms[j][1])
        output += int(uniforms[i][1] == uniforms[j][0])

print(output)