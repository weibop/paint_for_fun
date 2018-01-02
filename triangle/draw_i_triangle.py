import matplotlib.pyplot as plt


class PlotDrawer():  
   def __init__(self):
      self.size = 10  
      self.x = [0.0] * self.size
      self.y = [0.0] * self.size
      self.mod_en = 0
      self.max = 200.0
      self.margin = 200.0
      self.x_min = -self.margin
      self.x_max = self.max+self.margin
      self.y_min = -self.margin
      self.y_max = self.max+self.margin
      self.extent = (self.x_min, self.x_max, self.y_min, self.y_max)
            
      return
      
   def init(self):      
      self.fig = plt.figure(tight_layout=True, figsize=(11,11))
      self.ax = self.fig.add_subplot(111)
      # some X and Y data
      self.li, = self.ax.plot(self.x, self.y, '-ro')
      # draw and show it
      self.fig.canvas.draw()
      plt.xlim((self.x_min,self.x_max))
      plt.ylim((self.y_min,self.y_max))
      self.extent = (self.x_min, self.x_max, self.y_min, self.y_max)      
      implot = plt.imshow(self.im, extent=self.extent)      
      plt.show(block=False)#True    

      return
      
   def run(self):
      while 1:  
         try: 
            self.li.set_ydata(self.y)
            self.li.set_xdata(self.x)
            self.fig.canvas.draw()
            # if 1:
               # implot = plt.imshow(self.im, extent=self.extent)
            #plt.show(block=False)#True
            #time.sleep(0.1)
         except :
            break
      return