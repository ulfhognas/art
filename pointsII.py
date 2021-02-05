import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.0005)
dt = np.sin(2*t*np.pi)
fseq = []
jumps = np.arange(0.03, 1, 0.03)
jumps = np.append(jumps, np.arange(1, 0, -0.03))
last = 1
for i in jumps:
    fseq = np.append(fseq, np.arange(last, last+1, i))
    last = fseq[-1]+i
placement = (np.sin(fseq)/2+0.5)*len(fseq)
placement = np.around(placement)
placement = placement.astype(int)
placement2 = (np.sin(fseq+np.pi/4)/2+0.5)*len(fseq)
placement2 = np.around(placement2)
placement2 = placement2.astype(int)

i = 0

for f in fseq:
    x = dt*np.cos(-2*np.pi*f*t)
    y = dt*np.sin(-2*np.pi*f*t)

    r = np.linspace(start=0, stop=255, num=len(fseq)+1)
    g = np.linspace(start=0, stop=145, num=len(fseq)+1)
    b = np.linspace(start=64, stop=164, num=len(fseq)+1)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_facecolor((r[placement[i]]/256,g[placement[i]]/256,
                       b[placement[i]]/256))
    ax1.scatter(x, y, s = 800,
                color = (r[placement2[i]]/256,g[placement2[i]]/256,
                         b[placement2[i]]/256))
    ax1.scatter(x, y, s = 200, color = 'white')
    ax1.scatter(x, y, c = dt)
    name = str(int(f*20)).zfill(6) + '.png'
    plt.savefig(name)
    plt.cla()
    i += 1
