n = int(input())
forces = [list(map(int, input().split())) for _ in range(n)]
net_force = [0, 0, 0]
for force in forces:
    net_force[0] += force[0]
    net_force[1] += force[1]
    net_force[2] += force[2]
if net_force == [0, 0, 0]:
    print("YES")
else:
    print("NO")
