import matplotlib.pyplot as plt
import triangle
import spinTri
import spltTri

if __name__ == "__main__":
   print(__name__, "start ...")
   ratio = 0.08
   iteration = 50
   split = 5
   color = 'b'
   width = 1
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
      t = spinTri.spinTri(i, iteration, ratio);
      t.draw(color, width)
      
   print('123')
   for i in it2.subT:
      print('%d', i)
      t = spinTri.spinTri(i, iteration, ratio);
      t.draw(color, width)
      
   t1.show();

