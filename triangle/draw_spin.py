import matplotlib.pyplot as plt
#  use below command to install matplotlib components:
#  pip install matplotlib
import triangle
import spinTri
import spltTri

if __name__ == "__main__":
   print(__name__, "start ...")
   triratio = 0.05
   iteration = 100
   split = 5
   color = 'b'
   linewidth = 0.08
   lineratio = 1.02
   a = [0, 0]
   b = [20, 20]
   c = [20, 0]
   d = [0, 20]
   t1 = triangle.triangle(a,b,c)
   t2 = triangle.triangle(a,b,d)
   #t1.draw()
   it1 = spltTri.spltTri(t1,split)
   it2 = spltTri.spltTri(t2,split)
   for i in it1.subT:
      print('%d', i)
      t = spinTri.spinTri(i, iteration, triratio);
      t.draw(color, linewidth, lineratio)
      
   print('123')
   for i in it2.subT:
      print('%d', i)
      t = spinTri.spinTri(i, iteration, triratio);
      t.draw(color, linewidth, lineratio)
      
   t1.show();

