def mse(y,t):
    return (y-t)**2
def mse_prime(y,t):
    return -2*(t-y)
t=5**(1/8)
w=1
step=0.00001
for i in range(1,10000000):
    w-=step*mse_prime(w,t)
print(w)
