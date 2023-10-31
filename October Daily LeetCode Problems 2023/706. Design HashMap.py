class MyHashMap:
    def __init__(self):
        self.ans=dict()

    def put(self, key: int, value: int) -> None:
        self.ans[key]=value

    def get(self, key: int) -> int:
        if key in self.ans:
            return self.ans.get(key)
        else:
            return-1

    def remove(self, key: int) -> None:
        if key in self.ans:
            del self.ans[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)