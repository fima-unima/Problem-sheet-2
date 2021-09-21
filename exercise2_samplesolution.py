import numpy as np 
import matplotlib.pyplot as plt 

T = 5  # Time horizon
N = 100000  # Choose appropriate step size

def brownian_mot(N,T):  # Function to simulate a Brownian motion
    mu, sigma = 0, np.sqrt(1/N) # Mean and standard deviation 
    s = np.random.normal(mu, sigma, N*T) # N*T normal distributed random numbers 
    B = np.zeros(N*T+1)  # Vector creation
    for i in range(N*T):
        B[i+1]=B[i]+s[i] # Increments of BM on each time step
    return B   # Return the Brownian motion

def pth_variation(p,N,T):  # Function to approximate a pth-variation process, given p and N and T
    B = brownian_mot(N,T)  # use the Brownian motion function
    V = np.zeros(N*T+1)  # Vector creation
    for i in range(N*T):
        V[i+1]=V[i]+(abs(B[i+1]-B[i]))**p  # Definition of the pth-Variation
    return V

x = np.linspace(0, T, N*T+1)   # X-axis discretization
for i in range(3):  # Do the 3 plots
    p = i+1    # also try p=1.5+i*0.5, p=1.7+i*0.3 or p=1.9+i*0.1 -> you might need to take larger N
    plt.plot(x,pth_variation(p,N,T), label ="p=" + str(p))
plt.title("pth-variations of a Brownian motion")
plt.xlabel('t') # Labeling x-axis
plt.ylim(-1,2*T) # fix the scaling of the y-axis, because otherwise Python will zoom out way too much because of the larger values that the 1th variation attains
plt.legend(loc='best') # Legend at the position where Python finds it the best
plt.show()