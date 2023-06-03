n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
link = [0] * n
linked = [0] * n 

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            link[i] += 1 
            linked[j] += 1 
            
sources = []
sinks = []
for i in range(n):
    if link[i] == 0:
        sinks.append(i+1)
    if linked[i] == 0 :
        sources.append(i+1)
        
        
print(len(sources), *sources)
print(len(sinks), *sinks)
