import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
a = 1
points = np.array([
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
        (0, 0, 2),
        (0, 0, -2),
        (0, 2, 0),
        (0, -2, 0),
        (2, 0, 0),
        (-2, 0, 0), #13 номер
        (1.011,-1.011,1.011), #это настолько отвратительный код будет пиздец но я не придумал ничего лучше :(
        (2.01,0.01,0.01),
        (1.01, -1.01, -1.01),
        (0, -2, 0),
        (-1.011, -1.011, -1.011),
        (-1.011, 1.011, -1.011),
        (1.011, 1.011, -1.011)
    ])

ax.plot([points[12, 0], points[3, 0]],
         [points[12, 1], points[3, 1]],
         [points[12, 2], points[3, 2]], 'b')
ax.plot([points[11, 0], points[3, 0]],
         [points[11, 1], points[3, 1]],
         [points[11, 2], points[3, 2]], 'b')
ax.plot([points[9, 0], points[3, 0]],
         [points[9, 1], points[3, 1]],
         [points[9, 2], points[3, 2]], 'b')
ax.plot([points[7, 0], points[3, 0]],
         [points[7, 1], points[3, 1]],
         [points[7, 2], points[3, 2]], 'b')
ax.plot([points[3, 0], points[3, 0]],
         [points[3, 1], points[3, 1]],
         [points[3, 2], points[3, 2]], 'b')
ax.plot([points[2, 0], points[3, 0]],
         [points[2, 1], points[3, 1]],
         [points[2, 2], points[3, 2]], 'b')
ax.plot([points[1, 0], points[3, 0]],
         [points[1, 1], points[3, 1]],
         [points[1, 2], points[3, 2]], 'b')
ax.plot([points[1, 0], points[9, 0]],
         [points[1, 1], points[9, 1]],
         [points[1, 2], points[9, 2]], 'b')
ax.plot([points[3, 0], points[9, 0]],
         [points[3, 1], points[9, 1]],
         [points[3, 2], points[9, 2]], 'b')
ax.plot([points[5, 0], points[9, 0]],
         [points[5, 1], points[9, 1]],
         [points[5, 2], points[9, 2]], 'b')
ax.plot([points[7, 0], points[9, 0]],
         [points[7, 1], points[9, 1]],
         [points[7, 2], points[9, 2]], 'b')
ax.plot([points[9, 0], points[9, 0]],
         [points[9, 1], points[9, 1]],
         [points[9, 2], points[9, 2]], 'b')
ax.plot([points[1, 0], points[9, 0]],
         [points[1, 1], points[9, 1]],
         [points[1, 2], points[9, 2]], 'b')
ax.plot([points[2, 0], points[8, 0]],
         [points[2, 1], points[8, 1]],
         [points[2, 2], points[8, 2]], 'b')
ax.plot([points[4, 0], points[8, 0]],
         [points[4, 1], points[8, 1]],
         [points[4, 2], points[8, 2]], 'b')
ax.plot([points[6, 0], points[8, 0]],
         [points[6, 1], points[8, 1]],
         [points[6, 2], points[8, 2]], 'b')
ax.plot([points[8, 0], points[8, 0]],
         [points[8, 1], points[8, 1]],
         [points[8, 2], points[8, 2]], 'b')
ax.plot([points[2, 0], points[6, 0]],
         [points[2, 1], points[6, 1]],
         [points[2, 2], points[6, 2]], 'b')
ax.plot([points[4, 0], points[6, 0]],
         [points[4, 1], points[6, 1]],
         [points[4, 2], points[6, 2]], 'b')
ax.plot([points[6, 0], points[6, 0]],
         [points[6, 1], points[6, 1]],
         [points[6, 2], points[6, 2]], 'b')
ax.plot([points[7, 0], points[6, 0]],
         [points[7, 1], points[6, 1]],
         [points[7, 2], points[6, 2]], 'b')
ax.plot([points[8, 0], points[6, 0]],
         [points[8, 1], points[6, 1]],
         [points[8, 2], points[6, 2]], 'b')
ax.plot([points[11, 0], points[6, 0]],
         [points[11, 1], points[6, 1]],
         [points[11, 2], points[6, 2]], 'b')
ax.plot([points[13, 0], points[6, 0]],
         [points[13, 1], points[6, 1]],
         [points[13, 2], points[6, 2]], 'b')
ax.plot([points[2, 0], points[0, 0]],
         [points[2, 1], points[0, 1]],
         [points[2, 2], points[0, 2]], 'b')
ax.plot([points[4, 0], points[0, 0]],
         [points[4, 1], points[0, 1]],
         [points[4, 2], points[0, 2]], 'b')
ax.plot([points[8, 0], points[0, 0]],
         [points[8, 1], points[0, 1]],
         [points[8, 2], points[0, 2]], 'b')
ax.plot([points[10, 0], points[0, 0]],
         [points[10, 1], points[0, 1]],
         [points[10, 2], points[0, 2]], 'b')
ax.plot([points[12, 0], points[0, 0]],
         [points[12, 1], points[0, 1]],
         [points[12, 2], points[0, 2]], 'b')
ax.plot([points[1, 0], points[10, 0]],
         [points[1, 1], points[10, 1]],
         [points[1, 2], points[10, 2]], 'b')
ax.plot([points[4, 0], points[10, 0]],
         [points[4, 1], points[10, 1]],
         [points[4, 2], points[10, 2]], 'b')
ax.plot([points[5, 0], points[10, 0]],
         [points[5, 1], points[10, 1]],
         [points[5, 2], points[10, 2]], 'b')
ax.plot([points[10, 0], points[10, 0]],
         [points[10, 1], points[10, 1]],
         [points[10, 2], points[10, 2]], 'b')

ax.plot([points[1, 0], points[10, 0]],
         [points[1, 1], points[10, 1]],
         [points[1, 2], points[10, 2]], 'b')
ax.plot([points[7, 0], points[13, 0]],
         [points[7, 1], points[13, 1]],
         [points[7, 2], points[13, 2]], 'b')




ax.plot([points[4, 0], points[13, 0]],
         [points[4, 1], points[13, 1]],
         [points[4, 2], points[13, 2]], 'b')
ax.plot([points[5, 0], points[13, 0]],
         [points[5, 1], points[13, 1]],
         [points[5, 2], points[13, 2]], 'b')

ax.plot([points[6, 0], points[11, 0]],
         [points[6, 1], points[11, 1]],
         [points[6, 2], points[11, 2]], 'b')
ax.plot([points[7, 0], points[11, 0]],
         [points[7, 1], points[11, 1]],
         [points[7, 2], points[11, 2]], 'b')

ax.plot([points[2, 0], points[11, 0]],
         [points[2, 1], points[11, 1]],
         [points[2, 2], points[11, 2]], 'b')

ax.plot([points[1, 0], points[12, 0]],
         [points[1, 1], points[12, 1]],
         [points[1, 2], points[12, 2]], 'b')
ax.plot([points[2, 0], points[12, 0]],
         [points[2, 1], points[12, 1]],
         [points[2, 2], points[12, 2]], 'b')
#

ax.plot([points[2, 0], points[12, 0]],
         [points[2, 1], points[12, 1]],
         [points[2, 2], points[12, 2]], 'b')

ax.plot([points[7, 0], points[5, 0]],
         [points[7, 1], points[5, 1]],
         [points[7, 2], points[5, 2]], 'b')
ax.plot([points[4, 0], points[5, 0]],
         [points[4, 1], points[5, 1]],
         [points[4, 2], points[5, 2]], 'b')

ax.plot([points[1, 0], points[5, 0]],
         [points[1, 1], points[5, 1]],
         [points[1, 2], points[5, 2]], 'b')

ax.plot([points[1, 0], points[3, 0]],
         [points[1, 1], points[3, 1]],
         [points[1, 2], points[3, 2]], 'b')
ax.plot([points[1, 0], points[5, 0]],
         [points[1, 1], points[5, 1]],
         [points[1, 2], points[5, 2]], 'b')

ax.plot([points[1, 0], points[12, 0]],
         [points[1, 1], points[12, 1]],
         [points[1, 2], points[12, 2]], 'b')

ax.plot([points[1, 0], points[0, 0]],
         [points[1, 1], points[0, 1]],
         [points[1, 2], points[0, 2]], 'b')

ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o', s=100)

triangles = [
    [1, 5, 10], [2,  8, 6],[3,9,1], [0,12,2],[0,8,2],[3,7,9],[4,8,6],[5,7,9],
    [9,5,1],[1,10,9],[6,2,11],[7,3,11],[8,2,11],[4,0,10],[4,0,8],[10,4,8],[13,6,4],[7,5,13],[1,3,12],[14,15,16]
    ,[17,14,16],[18,6,11],[18,6,13],[19,4,13],[19,10,4],[20,0,10], [20,0,12]
]
for triangle in triangles:
    x = [points[triangle[0], 0], points[triangle[1], 0], points[triangle[2], 0]]
    y = [points[triangle[0], 1], points[triangle[1], 1], points[triangle[2], 1]]
    z = [points[triangle[0], 2], points[triangle[1], 2], points[triangle[2], 2]]

    ax.plot_trisurf(x, y, z, color='green', alpha=1)



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
plt.show()

