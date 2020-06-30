import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=['#377eb8', '#ff7f00', '#4daf4a',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00'])
matplotlib.rc('lines', linewidth=3)

# experiment4
f = open('plotdata/experiment4_parallel_copy', 'r')
output = f.read()
output = output.split("\n")
x_list = output[0].split(",")
results = output[1:]
eps3 = [float(res.split(",")[0]) for res in results]
epsr1 = [float(res.split(",")[1]) for res in results]
epsr2 = [float(res.split(",")[2]) for res in results]

l1=[x/eps3[0] for x in eps3]
l2=[x/epsr1[0] for x in epsr1]
l3=[x/epsr2[0] for x in epsr2]
l4=[x**2 for x in l2]


lw=3
plt.plot(x_list, l1, linestyle='solid', label=r'$\|x_T - x^*\|^2$')
plt.plot(x_list, l3, linestyle='dashed', label=r'${(\log T)^2}/{n}$')
plt.plot(x_list, l2, linestyle='dotted', label=r'${1}/{n}$')
plt.plot(x_list, l4, linestyle='dashdot', label=r'${1}/{n^2}$')

plt.yscale('log')
plt.legend(loc='lower left',fontsize=12,ncol=2)
plt.xlabel(r'Number of component functions $n$',fontsize=12)
x_list_small=x_list[::20]
plt.xticks(x_list_small,x_list_small)

# plt.title('eta=0.07')
# plt.ylim([0.001, 1])
plt.savefig('n_dependence.pdf') 
plt.show() 