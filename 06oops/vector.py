'''
2d Vector => 5i^ + 6j^
3d Vector => 5i^ + 6j^ + 4k^

'''

class Vec2D:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^")


class Vec3D(Vec2D):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k
    
    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")


obj = Vec2D(5,6)
obj.show()

obj2 = Vec3D(3,5,6)
obj2.show()