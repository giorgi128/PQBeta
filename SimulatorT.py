import matplotlib
matplotlib.use('Agg') 
import subprocess
import timeit
import shlex
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

NREPEATS = 10  #number of times to call  in order to measure average time
version = "multiq"

#build kpqueue
cmd = "make"
args = shlex.split(cmd)
subprocess.call(args)

def Run(beta):
	
    A = []
    B = []
    cntthreads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    nthreads = 1
    for nthreads in cntthreads:
        #run concurrent Dijkstra with betanthreads #threads
	
        cmd = "./build/src/bench/random          -i 10000000"+ " -p " + str(nthreads)+ \
                                                         " -b "+str(beta)+          \
                                                         " " + version  
        args = shlex.split(cmd)

        t = 0
		
        for i in range(0, NREPEATS):
		
			st = subprocess.check_output(args)
			t  += float(st)
			
        B.append(t / NREPEATS)
        A.append(nthreads)
        
        #nthreads = nthreads*2
        print version+" "+str(nthreads)+" "+str(t/NREPEATS)
#    print A
    return A, B

		
colors = ['r', 'g', 'y', 'b', 'm']

#f = open('RunTimes.txt', 'w')
plt.xlabel('number of threads')
plt.ylabel('throughput')


fig, ax = plt.subplots()

version = "linden"
A, B = Run(0)
ax.plot(A, B, '.'+'b'+'-', label="linden")

version = "klsm256"
A, B = Run(0)
ax.plot(A, B, '.'+'m'+'-', label="klsm256")

version = "multiq"
beta = 0
while beta <= 10:
        A, B = Run(beta)
        ax.plot(A, B, '.'+colors[beta / 5]+'-', label='beta='+str(1-1.0*beta/20))
        #color_patch = mpatches.Patch(color=colors[beta/5], label='beta='+str(1.0*beta/20), label='beta='+str(1.0*beta/20))
        #color_patches.append(color_patch)        
        beta += 5
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig.savefig('Throughput.jpg')

