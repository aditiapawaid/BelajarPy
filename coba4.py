from matplotlib import pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes()
# ax.grid()
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x, np.sin(x))

# Menambahkan title dan label ke dalam plot
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
ax.set_title('Plot SEDERHANA') # Menambahkan Title
ax.set_xlabel('Label x') # Memberikan label x
ax.set_ylabel('Label y'); # Memberikan label y

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.set_title('Plot dengan Multiple Lines')
ax.set_xlabel('Label x')
ax.set_ylabel('Label y')
plt.show()