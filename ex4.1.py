import random

T = int(input("Give a number of instants in which are distributed the tasks: "))
N_task = int(input("Give a number of tasks: "))

print("\nCreating random outsourcing costs between 1 and 10...")
F_t = []
for i in range(0,N_task):
    F_t.append(random.randint(1,10))
    
Task = []
print("Creating the pair instances of Tasks...")
for i in range(1,N_task):
    Task.append((random.randint(1,T),F_t[i]))

print()
A = int(input("Give a cost tor hiring a worker: "))
s = int(input("Give a cost of worker's salary: "))
L = int(input("Give a cost to firing a worker: "))
print()
F_C = [0]*T
for (t,cost) in Task:               #I can have more than a task for each instant, so I execute some preprocessing 
    F_C[t-1] += cost                #and compute a sum of all freelance costs for those tasks.

Workers_Execution = {}
Freelancers_Execution = {}

def frl_cost(t_i):
    if t_i in Freelancers_Execution:
        return Freelancers_Execution[t_i]                   #I use the dictionary to avoid many recursive steps!
                                                            #It is for this reason that the running time is not growing to an exponential time.
                                                            #This exploits dynamic programming.
    elif t_i == 0:
        return 0                                            #at instant 0 I've not freelance, the cost is 0.
    else:
        wrk = wkr_cost(t_i - 1) + F_C[t_i - 1] + L          #I had a worker at t_i - 1 and now I outsource a freelance by firing the worker.
        frl = frl_cost(t_i - 1) + F_C[t_i - 1]              #I had a freelance at t_i - 1 and now I outsource another one.
        Freelancers_Execution[t_i] = min(frl, wrk)          #I store each instant minimum cost calculated in this dictionary.
        return Freelancers_Execution[t_i]
    
def wkr_cost(t_i):
    if t_i in Workers_Execution:
        return Workers_Execution[t_i]                       #I use the dictionary to avoid many recursive steps!
                                                            #It is for this reason that the running time is not growing to an exponential time.
                                                            #This exploits dynamic programming.
    elif t_i == 0:
        return A                                            #at instant 0 I'm hiring a worker, the cost is A.
    else:
        wrk = wkr_cost(t_i - 1) + s                         #I had a worker at t_i - 1 and I decide to continue to pay him.
        frl = frl_cost(t_i - 1) + A + s                     #I had a freelance at t_i - 1 and now I hire a new worker.
        Workers_Execution[t_i] = min(wrk, frl)              #I store each instant minimum cost calculated in this dictionary.
        return Workers_Execution[t_i]



def tot_cost(T):
        min_cost = min(wkr_cost(T), frl_cost(T))            #Compute the two possible minimum paths, choose the less expensive one.
        return min_cost
    
print()
print("The mininmum cost computed is: ", str(tot_cost(T)))

#print(Task)
#print(Workers_Execution)
#print(Freelancers_Execution)
