from scipy.interpolate import lagrange
x = np.array([0,1,2])
y = x**3
poly = lagrange(x,y)
