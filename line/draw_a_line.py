import matplotlib.pyplot as plt

x1 = 0
y1 = 1
x2 = 40
y2 = 40

margin = 1

# 'r' for red
plt.plot([x1,x2], [y1,y2], 'r')
plt.axis([min(x1,x2)-margin, max(x1,x2)+margin, min(y1,y2)-margin, max(y1,y2)+margin])
plt.show()