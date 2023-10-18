import matplotlib.pyplot as plt

import numpy as np
n = 200000
datax = np.hstack([np.random.randn(n)*2-3,
                   np.random.randn(n)*2+5])
datay = np.hstack([np.random.randn(n)* 6+4,
               np.random.randn
               (n)*5-4])
xi = np.array([1,4])
xv,yv = datax,datay
pos = np.vstack([datax,datay])
plt.figure(1)
plot_pos = 131
for h in [8,5,2]:
    plt.subplot(plot_pos)
    plot_pos += 1
    Vn = h ** 2
    u = (pos - xi.reshape(-1,1))/h # u = (x - xi)/h
    ix,iy = pos[:,(abs(u)<=0.5).all(axis=0)]
    plt.xlim([-10,12])
    plt.ylim([-15,18])
    plt.title("h="+str(h))
    plt.scatter(xv,yv,s=0.01)
    plt.scatter(ix,iy)
    plt.scatter(xi[0],xi[1],c='r')
plt.show()
def px(x):
    u = (pos - x.reshape(-1,1))/ h # u = (x - xi)/h
    ix,iy = pos[:,(abs(u)<=0.5).all(axis=0)]
    k = len(ix)
    return k / (Vn * n)

w = 50
gx = gy = np.linspace(-10,10,w)
gxv,gyv = np.meshgrid(gx,gy)

fgxv = gxv.ravel()
fgyv = gyv.ravel()

plt.figure(3)
plot_pos = 321
for i in [8,5,2]:
    h = i
    fpx = np.array([px(x) for x in np.vstack([fgxv,fgyv]).T])
    fpx = fpx.reshape(w,w)
    ax = plt.subplot(plot_pos,projection='3d')
    plot_pos += 1
    ax.plot_surface(gxv,gyv,fpx,cmap='GnBu')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('h='+str(h))
    ax = plt.subplot(plot_pos)
    plot_pos += 1
    ax.contour(gxv,gyv,fpx)
plt.show()