import numpy as np
import random
import multiprocessing

# lamda = 1.0
G = 1.0
sF=4.0

def single_iteration(iters):
  stepFactor=sF
  n = 500
  print(iters)
  # eta = 100.0/(n*lamda*iters)
  eta = stepFactor * np.log(n*iters) / (n*iters)
  e1 = 0; e2 = 0; e3 = 0; e4 = 0; e5 = 0; e6 = 0; e7 = 0; e8 = 0; e9 = 0
  for rep in range(reps):
    e3 += randomReshuffleNonLipHess(eta, n, iters)

  eps3_i = 1.0*e3/reps
  epsr1_i = 1.0/iters**2
  epsr2_i = 1.0*(np.log(iters*n)**2)/iters**2
  # print(eps1)
  return [eps3_i, epsr1_i, epsr2_i]

def randomReshuffleNonLipHess(eta, n, iters):
  # x = np.zeros(iters)
  # x[0] = 0
  x=0
  for i in range(1, iters+1):
    # eta=stepFactor/(i*n)
    r = np.random.permutation(np.concatenate((-np.ones(np.int(n/2)), np.ones(np.int(n/2)))))
    # x[i] = x[i-1]
    for j in range(0, n):
      # x[i] = (1 - eta*lamda*4)*x[i] - eta*lamda*4*r[j]
      if (x>0):
        x = (1 - eta*4.0)*x - eta*r[j]
      else:
        x = (1 - eta)*x - eta*r[j]

  # return x[-1]**2
  return x**2


reps = 100 #1000
it_beg=30
it_end=200
x_list=[]
l1=[];l2=[];l3=[]
pool = multiprocessing.Pool(16)
iter_range = range(it_beg,it_end)
results = pool.map(single_iteration, iter_range)

f = open('plotdata/experiment3_parallel_'+str(sF), 'w')
f.write(",".join([str(iter) for iter in iter_range]) + "\n" + "\n".join([",".join([str(r) for r in res]) for res in results]))
