import numpy as np
import random
import multiprocessing

G = 1.0
sF=4.0

def parallelOptimization_n(n):
  print(n)
  stepFactor=sF
  K=500
  eta = stepFactor * np.log(n*K) / (n*K)
  e3 = 0
  for rep in range(reps):
    e3 += randomReshuffleNonLipHess(eta, n, K)

  eps3_i = 1.0*e3/reps
  epsr1_i = 1.0/n
  epsr2_i = 1.0*(np.log(K*n)**2)/n
  return [eps3_i, epsr1_i, epsr2_i]

def randomReshuffleNonLipHess(eta, n, K):
  x=0
  for i in range(1, K+1):
    r = np.random.permutation(np.concatenate((-np.ones(n/2), np.ones(n/2))))
    for j in range(0, n):
      if (x>0):
        x = (1 - eta*4.0)*x - eta*r[j]
      else:
        x = (1 - eta)*x - eta*r[j]

  return x**2

reps = 1000
n_beg=30
n_end=200
x_list=[]
n_range = range(n_beg,n_end,2)
pool = multiprocessing.Pool(16)
results = pool.map(parallelOptimization_n, n_range)
f = open('plotdata/experiment_K_parallel_'+str(sF), 'w') # Replace with desired output file name
f.write(",".join([str(n) for n in n_range]) + "\n" + "\n".join([",".join([str(r) for r in res]) for res in results]))
