import matplotlib
matplotlib.use('Agg')
import subprocess
import timeit
import shlex
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

NREPEATS = 10  #number of times to call Dijkstra in order to measure average time
version = "multiq"

#build kpqueue
cmd = "make"
args = shlex.split(cmd)
subprocess.call(args)

def Run(beta):
	
    A = []
    B = []
    cntthreads = [1,2,4,8,16,64]
    nthreads = 1
    seed = 0
    for nthreads in cntthreads:
        seed+=1
        #run concurrent Dijkstra with betanthreads #threads
	
        cmd = "./build/src/bench/shortest_paths       -n " + str(nthreads)+ \
                                                         " -b "+str(beta)+          \
                                                         " -s "+str(seed)+" " + version  
        args = shlex.split(cmd)

        t = 0
		
        for i in range(0, NREPEATS):
		
			st = subprocess.check_output(args)
			t  += float(st)
			
        B.append(t / NREPEATS)
        A.append(nthreads)

        #nthreads = nthreads*2

#    print A
    return A, B

		
#f = open('RunTimes.txt', 'w')                                                                                                                                                       
#plt.xlabel('number of threads')
#plt.ylabel('DijkstraRunTime')

#colors = ['r', 'g', 'y', 'b', 'm']

beta = 0
#fig, ax = plt.subplots()

while beta <= 20:
        
    A, B = Run(beta)
    print "beta="+str((20.0-beta)/20.0)
    print "1thread "+str(B[0])
    for i in range(1,6): 
        print str(A[i])+"thread "+"relaxations="+str(B[i])
    #ax.plot(A, B, '.'+colors[beta / 5]+'-', label='beta='+str(1-1.0*beta/20))
    #color_patch = mpatches.Patch(color=colors[beta/5], label='beta='+str(1.0*beta/20), label='beta='+str(1.0*beta/20))                                                          
    #color_patches.append(color_patch)                                                                                                                                           
    beta += 5
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#fig.savefig('DijkstraLJ.jpg')

		










