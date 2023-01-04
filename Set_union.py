# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())
english = set(input().split()) 

n2 = int(input())
# for x in input().split(): english.add(x)
french = set(input().split())
print(len(english.union(french)))
