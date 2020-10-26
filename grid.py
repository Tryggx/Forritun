class Grid:
    def __init__(self,x=1,y=1):
        self.x=int(x)
        self.y=int(y)
        self.ystring="o"*int(y)
        self.pos=[0,0]
        self.move()


    def __str__(self):
        self.str='\n'.join(self.list)
        return self.str + '\n'

    def move(self):
        self.list=[]
        for i in range(self.x):
            self.list.append(self.ystring)
        return self.list
       
    


a_grid=Grid(3,4)
print(a_grid)