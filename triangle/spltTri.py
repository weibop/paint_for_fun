import matplotlib.pyplot as plt
import triangle

class spltTri():  
   def __init__(self, t, iteration=4):
      self.iter = iteration
      self.numT = 2**self.iter
      self.subT = [t]*self.numT
      self.x_min = t.x_min
      self.x_max = t.x_max
      self.y_min = t.y_min
      self.y_max = t.y_max
      for i in range(self.iter):
         for j in range(2**i):
            [t1, t2] = self.__split(self.subT[j*(2**(self.iter-i))])
            self.subT[j*(2**(self.iter-i)) + 0] = t1
            self.subT[j*(2**(self.iter-i)) + (2**(self.iter-1-i))] = t2
         
      return
      
   def __split(self, t):
      tempT1 = triangle.triangle(t.longVtx[1], t.longVtx[0], t.longEdge.mid);
      tempT2 = triangle.triangle(t.longVtx[2], t.longVtx[0], t.longEdge.mid);
      return [tempT1, tempT2]
      
   def draw(self, color='b', linewidth=1.0):
      for i in self.subT:
         i.draw(color, linewidth)
      return 

   def drawAlone(self, color='b', linewidth=1.0):
      # 'r' for red
      margin = 1
      self.draw(color, linewidth)
      plt.axis([self.x_min-margin, self.x_max+margin, self.y_min-margin, self.y_max+margin])
      plt.show()
      return      


if __name__ == "__main__":
   print(__name__, "start ...")
   a = [0, 0]
   b = [40, 30]
   c = [40, 0]
   d = [0, 30]
   t1 = triangle.triangle(a,b,c)
   t2 = triangle.triangle(a,b,d)
   it1 = spltTri(t1,6)
   it2 = spltTri(t2,3)
   it1.draw()
   it2.drawAlone('r', 0.1);

