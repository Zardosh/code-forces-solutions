n = int(input())

polyhedrons = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20,
}

output = 0

for _ in range(n):
    s = input()

    output += polyhedrons[s]

print(output)