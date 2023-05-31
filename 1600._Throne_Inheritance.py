'''
question: given the kingsName and his childs store the families kingdom
list or structure inorder and return them when called.
​
solution: store the given childs in adjcency list and hold the dead
peoples in set and whenever `getInheritanceOrder` is called do simple
dfs on the adjecency list and return the list of structures.
'''
class ThroneInheritance:
​
    def __init__(self, kingName: str):
        self.parents = defaultdict(list)
        self.dead = set()
        self.king = kingName
​
    def birth(self, parentName: str, childName: str) -> None:
        self.parents[parentName].append(childName)
        
​
    def death(self, name: str) -> None:
        self.dead.add(name)
​
    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(node, deadppl):
            if node not in deadppl :
                res.append(node)
            for child in self.parents[node]:
                dfs(child, deadppl)
        dfs(self.king, self.dead)
        return res
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
