##Regressao linear
N = len(x)

xy = x*y
sumxy = xy.sum()
sumx = x.sum()
sumy = y.sum()

xx = np.square(x)
sumxx = xx.sum()
yy = np.square(y)
sumyy = yy.sum()


m = (N*sumxy - sumx*sumy)/(N*sumxx - (sumx)**2)
b = (sumxx*sumy - sumx*sumxy)/(N*sumxx - (sumx)**2)
r_num = (N * sumxy - sumx * sumy)**2
r_den  = (N * sumxx - (sumx)**2) * (N * sumyy - (sumy)**2)
r2 = r_num/r_den

m_erro = np.abs(m) * np.sqrt(((1/r2) - 1) / (N - 2))
b_erro = m_erro * np.sqrt(sumxx/N)


plt.plot(x, y, "X")
plt.plot(x, m*x+b, label="Reta Regressão T/M")


plt.xlabel("s (m)")
plt.ylabel("t (s)")
plt.grid()

print("m +/- m_erro = {:0.8f} +/- {:0.8f}".format(m,m_erro))
print("b +/- b_erro = {:0.8f} +/- {:0.8f}".format(b,b_erro))
print("r2 = {:0.8f}".format(r2))
