import matplotlib.pyplot as plt
import math
import edge as edge

class triangle():  
   def __init__(self, v0=[0,40], v1=[40,40], v2=[10,0]):
      if(self.__checkPoint(v0) or self.__checkPoint(v1) or self.__checkPoint(v2)):
         print("input point error")
         return 0;
      self.v = [v0, v1, v2]
      self.x_min = min(v0[0], v1[0], v2[0])
      self.x_max = max(v0[0], v1[0], v2[0])
      self.y_min = min(v0[1], v1[1], v2[1])
      self.y_max = max(v0[1], v1[1], v2[1])
      self.edge = [edge.edge(self.v[1],self.v[2]), edge.edge(self.v[0],self.v[2]), edge.edge(self.v[0],self.v[1])]
      if(self.edge[0].len >= max(self.edge[1].len,self.edge[2].len)):
         self.longEdge = self.edge[0]
         self.longVtx = [self.v[0], self.v[1], self.v[2]]
      elif(self.edge[1].len >= self.edge[2].len):
         self.longEdge = self.edge[1]
         self.longVtx = [self.v[1], self.v[2], self.v[0]]
      else:
         self.longEdge = self.edge[2]
         self.longVtx = [self.v[2], self.v[0], self.v[1]]

      return
   
      
   def __checkPoint(self, p):
      if(len(p)==2):
         return 0;
      else:
         return 1;
      
   def draw(self, color='b', linewidth=1.0):
      for i in self.edge:
         i.draw(color, linewidth)
      return 0

   def drawAlone(self, color='b', linewidth=1.0):
      # 'r' for red
      margin = 1
      self.draw(color, linewidth)
      self.longEdge.draw('g', linewidth)
      plt.plot(self.longVtx[0][0], self.longVtx[0][1], 'o')
      plt.plot(self.longEdge.mid[0], self.longEdge.mid[1], 'o')
      #plt.plot(self.mid[0], self.mid[1], 'o')
      plt.axis([self.x_min-margin, self.x_max+margin, self.y_min-margin, self.y_max+margin])
      #plt.title('Drawing edge, Length = %0.2f'%self.len, fontsize=20)
      plt.show()
      return      

   def show(self, color='b'):
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
   t = triangle(a,b,c)
   t1 = triangle(a,b,d)
   t.draw();
   t1.draw();
   t1.show();

