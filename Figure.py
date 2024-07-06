import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

points = np.array([[5, 5, 5], [0, 5, 5], [5, 0, 5],[2.5, 2.5, 2.5], [0, 0, 5], [0, 0, 0],[5, 0, 0],[5, 5, 0],[0, 5, 0],[7.5, 2.5, 2.5],[-2.5, 2.5, 2.5]])
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o', s=100)


ax.plot([points[0, 0], points[3, 0]],
         [points[0, 1], points[3, 1]],
         [points[0, 2], points[3, 2]], 'b')
ax.plot([points[1, 0], points[3, 0]],
         [points[1, 1], points[3, 1]],
         [points[1, 2], points[3, 2]], 'b')
ax.plot([points[2, 0], points[3, 0]],
         [points[2, 1], points[3, 1]],
         [points[2, 2], points[3, 2]], 'b')
ax.plot([points[4, 0], points[3, 0]],
         [points[4, 1], points[3, 1]],
         [points[4, 2], points[3, 2]], 'b')
ax.plot([points[5, 0], points[3, 0]],
         [points[5, 1], points[3, 1]],
         [points[5, 2], points[3, 2]], 'b')
ax.plot([points[6, 0], points[3, 0]],
         [points[6, 1], points[3, 1]],
         [points[6, 2], points[3, 2]], 'b')
ax.plot([points[7, 0], points[3, 0]],
         [points[7, 1], points[3, 1]],
         [points[7, 2], points[3, 2]], 'b')
ax.plot([points[8, 0], points[3, 0]],
         [points[8, 1], points[3, 1]],
         [points[8, 2], points[3, 2]], 'b')
ax.plot([points[8, 0], points[3, 0]],
         [points[8, 1], points[3, 1]],
         [points[8, 2], points[3, 2]], 'b')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()