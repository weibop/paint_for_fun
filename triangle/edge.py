import matplotlib.pyplot as plt
import math

class edge():
   def __init__(self, p1=[0, 0], p2=[20, 20]): 
      if(self.checkPoint(p1) or self.checkPoint(p2)):
         print("input point error")
         return 0;
      self.p1 = p1
      self.p2 = p2
      self.x_min = min(self.p1[0],self.p2[0])
      self.x_max = max(self.p1[0],self.p2[0])
      self.y_min = min(self.p1[1],self.p2[1])
      self.y_max = max(self.p1[1],self.p2[1])
      self.mid = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
      self.len = math.sqrt(math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2))

   def checkPoint(self, p):
      if(len(p)==2):
         return 0;
      else:
         return 1;

   def draw(self, color='b'):
      plt.plot([self.p1[0],self.p2[0]] , [self.p1[1],self.p2[1]], color)
      return
   
   def drawAlone(self, color='b'):
      # 'r' for red
      margin = 1
      self.draw(color) #plt.plot([self.p1[0],self.p2[0]] , [self.p1[1],self.p2[1]], color)
      print('mid point: x=%0.2f,y=%0.2f'%(self.mid[0], self.mid[1]))
      plt.plot(self.mid[0], self.mid[1], 'o')
      plt.axis([self.x_min-margin, self.x_max+margin, self.y_min-margin, self.y_max+margin])
      plt.title('Drawing edge, Length = %0.2f'%self.len, fontsize=20)
      plt.show()
      return
      
if __name__ == "__main__":
   print(__name__, "start ...")
   a = [0, 1]
   b = [40, 40]
   e = edge(a,b)
   e.drawAlone();
