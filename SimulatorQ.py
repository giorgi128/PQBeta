import subprocess
import timeit
import shlex
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

NREPEATS = 1  #number of times to call in order to measure average time
version = "multiq"

#build kpqueue
cmd = "make"
args = shlex.split(cmd)
subprocess.call(args)

def Run(beta):
	
    A = []
    B = []

    nthreads = 8
    while nthreads <= 8:
        #run concurrent Dijkstra with betanthreads #threads
	
        cmd = "./build/src/bench/random          -i 10000000"+ " -p " + str(nthreads)+ \
                                                         " -b "+str(beta)+          \
                                                         " " + version  
        args = shlex.split(cmd)

        t = 0
		
        for i in range(0, NREPEATS):
		
			st = subprocess.check_output(args)
			ar = st.split(" ")
			t += float(ar[0]) #add mean
			
        #B.append(t / NREPEATS)
        #A.append(nthreads)

        nthreads = nthreads*2

#    print A
    return t/NREPEATS

		
#colors = ['r', 'g', 'y', 'b', 'm']

#f = open('RunTimes.txt', 'w')
plt.xlabel('beta')
plt.ylabel('mean')

beta = 0
color_patches = []

A = []
B = []

fig, ax = plt.subplots()

while beta <= 20:
        tt  = Run(beta)
        A.append(1-1.0*beta/20)
        B.append(tt)
        beta += 5

ax.plot(A, B, '.'+'r'+'-', label='8 threads')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig.savefig('mean.jpg')






