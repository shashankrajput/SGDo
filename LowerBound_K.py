import numpy as np
import random
import multiprocessing

G = 1.0
sF=4.0

def parallelOptimization_K(K):
  stepFactor=sF
  n = 500
  print(K)
  eta = stepFactor * np.log(n*K) / (n*K)
  e3 = 0;
  for rep in range(reps):
    e3 += randomReshuffleNonLipHess(eta, n, K)

  eps3_i = 1.0*e3/reps
  epsr1_i = 1.0/K**2
  epsr2_i = 1.0*(np.log(K*n)**2)/K**2
  return [eps3_i, epsr1_i, epsr2_i]

def randomReshuffleNonLipHess(eta, n, K):
  x=0
  for i in range(1, K+1):
    r = np.random.permutation(np.concatenate((-np.ones(np.int(n/2)), np.ones(np.int(n/2)))))
    for j in range(0, n):
      if (x>0):
        x = (1 - eta*4.0)*x - eta*r[j]
      else:
        x = (1 - eta)*x - eta*r[j]
  return x**2


reps = 1000
K_beg=30
K_end=200
x_list=[]
l1=[];l2=[];l3=[]
pool = multiprocessing.Pool(16)
K_range = range(K_beg,K_end)
results = pool.map(parallelOptimization_K, K_range)

f = open('plotdata/experiment_K_parallel_'+str(sF), 'w') # Replace with desired output file name
f.write(",".join([str(K) for K in K_range]) + "\n" + "\n".join([",".join([str(r) for r in res]) for res in results]))
