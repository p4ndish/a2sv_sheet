# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
count= dict()
words = set()
for i in range(N):
    word = input()
    words.add(word)
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
    
print(len(count))
for w in words:
    print(count[w], end=" ")
