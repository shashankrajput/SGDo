import numpy as np
import random
import multiprocessing

# lamda = 1.0
G = 1.0
sF=4.0

def single_n(n):
  print(n)
  stepFactor=sF
  iters=500
  # eta = 100.0/(n*lamda*iters)
  eta = stepFactor * np.log(n*iters) / (n*iters)
  e3 = 0
  for rep in range(reps):
    e3 += randomReshuffleNonLipHess(eta, n, iters)

  eps3_i = 1.0*e3/reps
  epsr1_i = 1.0/n
  epsr2_i = 1.0*(np.log(iters*n)**2)/n
  return [eps3_i, epsr1_i, epsr2_i]

def randomReshuffleNonLipHess(eta, n, iters):
  # x = np.zeros(iters)
  # x[0] = 0
  x=0
  for i in range(1, iters+1):
    # eta=stepFactor/(i*n)
    r = np.random.permutation(np.concatenate((-np.ones(n/2), np.ones(n/2))))
    # x[i] = x[i-1]
    for j in range(0, n):
      # x[i] = (1 - eta*lamda*4)*x[i] - eta*lamda*4*r[j]
      if (x>0):
        x = (1 - eta*4.0)*x - eta*r[j]
      else:
        x = (1 - eta)*x - eta*r[j]

  return x**2

reps = 100 #1000
# stepFactor=sF
iters=500
n_beg=30
n_end=200
x_list=[]
n_range = range(n_beg,n_end,2)
pool = multiprocessing.Pool(16)
results = pool.map(single_n, n_range)
f = open('plotdata/experiment4_parallel_'+str(sF), 'w')
f.write(",".join([str(n) for n in n_range]) + "\n" + "\n".join([",".join([str(r) for r in res]) for res in results]))
