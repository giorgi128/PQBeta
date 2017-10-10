import matplotlib
matplotlib.use('Agg') 
import subprocess
import math
import timeit
import shlex
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

NREPEATS = 20  #number of times to call in order to measure average time
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
	arrt = []	
        for i in range(0, NREPEATS):
		
			st = subprocess.check_output(args)
			ar = st.split(" ")
			t += float(ar[0]) #add mean
			arrt.append(float(ar[0]))
        #B.append(t / NREPEATS)
        #A.append(nthreads)

        nthreads = nthreads*2

#    print A
     
    mn=t/NREPEATS
    sd=0.0
    for i in arrt:
        sd+=(mn-i)*(mn-i)
    sd=math.sqrt(sd/NREPEATS)
    ilen=1.96*sd/math.sqrt(NREPEATS)
    return mn, ilen
#colors = ['r', 'g', 'y', 'b', 'm']

#f = open('RunTimes.txt', 'w')

beta = 0
#color_patches = []

#A = []
#B = []

#fig, ax = plt.subplots()
#ax.set_xlabel('beta')
#ax.set_ylabel('log(mean)')
while beta <= 20:
        
        mn, ilen  = Run(beta)
        
        print ' mn='+str(mn)+' ilen='+str(ilen) 
        beta += 2







