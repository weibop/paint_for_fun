import matplotlib.pyplot as plt
#import math
import triangle
import edge

class spinTri():  
   def __init__(self, t, iteration=24, ratio = 0.2):
      self.ratio = ratio
      self.origT = t
      #self.currT = t
      #self.startVtx = t.longVtx[0]
      self.iter = iteration
      self.x_min = t.x_min
      self.x_max = t.x_max
      self.y_min = t.y_min
      self.y_max = t.y_max
         
      return
   
   def drawFrame(self, color='b', linewidth=1.0):
      for i in self.origT.edge:
         i.draw(color, linewidth)
      return
   
   def drawSpin(self, color='b', linewidth=1.0, lineratio=1.0):
      currT = self.origT
      width = linewidth
      for i in range(self.iter):
         ratioX = abs(currT.v[1][0] - currT.v[2][0])*self.ratio
         ratioY = abs(currT.v[1][1] - currT.v[2][1])*self.ratio
         if(currT.v[1][0] > currT.v[2][0]):
            newX = currT.v[1][0] - ratioX
         else:
            newX = currT.v[1][0] + ratioX
         if(currT.v[1][1] > currT.v[2][1]):
            newY = currT.v[1][1] - ratioY
         else:
            newY = currT.v[1][1] + ratioY
         newPoint = [newX, newY]
         newEdge = edge.edge(currT.v[0], newPoint)
         newEdge.draw(color, width)
         width = width*lineratio
         newT = triangle.triangle(newPoint, currT.v[2], currT.v[0])
         currT = newT
         
      return
   
   def draw(self, color='b', linewidth=1.0, lineratio=1.0):
      self.drawFrame(color, linewidth)
      self.drawSpin(color, linewidth, lineratio)
      return 

   def drawAlone(self, color='b', linewidth=1.0, lineratio=1.0):
      # 'r' for red
      margin = 1
      self.draw(color, linewidth, lineratio)
      plt.axis([self.x_min-margin, self.x_max+margin, self.y_min-margin, self.y_max+margin])
      plt.show()
      return     

   def show(self, color='b'):
      # 'r' for red
      margin = 1
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
   it1 = spinTri(t1)
   it2 = spinTri(t2, 24, 0.2)
   it1.draw('r', 0.1)
   it2.draw('k', 0.5)
   it2.show()
   #it2.drawAlone();

