import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

#Open cv reads images in BGR by default
nemo = cv2.imread('/mnt/c/projects/opencv/nemo0.jpg')
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo)
plt.show()

# Visualize nemo in RGB and HSV

# Split an image into component channels and set up the plot
r, g, b = cv2.split(nemo)
fig = plt.figure()
axis = fig.add_subplot(1,1,1,projection="3d")

# Pretvara sliku niz gde je svaki element vrednost RGB piksela
pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

# Plotting
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()