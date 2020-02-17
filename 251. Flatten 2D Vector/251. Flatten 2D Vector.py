"""
class Vector2D:
    
    def __init__(self, v: List[List[int]]):
        self.flat = [x for row in v for x in row]
        self.index = 0
        

    def next(self) -> int:
        temp = self.index
        self.index += 1
        return self.flat[temp]

    def hasNext(self) -> bool:
        return self.index < len(self.flat)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
"""