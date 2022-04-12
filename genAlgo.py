import math
from random import randint


# Generate random population with 2D Array
def generatePopulation(chess_size, pop_size):
    pop = []
    for i in range (0,pop_size):
        temp = []
        for j in range(0,chess_size):
            temp.append(randint(0,chess_size-1))
        pop.append(temp)
    return pop

# Calculate attack value 
def calc_att(sample):
    attack = 0
    for i in range(len(sample)):
        for j in range(i+1,len(sample)):
            if sample[i] == sample[j]:
                attack+=1
            elif (abs(i-j) == abs(sample[j]-sample[i])):
                attack+=1
    return attack

# Make an array that containing attack value from each individual in population
def fittest_score(pop):
    fit=[]
    for i in range(len(pop)):
        fit.append(calc_att(pop[i]))
    return fit

# Making parent for crossing in the new generation
def choose_parent(pop,fit):
    sorted_pop = []
    parent=[]
    smallest_att=min(fit)

    # Sorting the pop by it fittest value from best selection to bad one, so that make it easier to choose parent
    while(len(sorted_pop)<len(pop)):
        for idx,i in enumerate(fit) :
            if (i == smallest_att)and(len(sorted_pop)<len(pop)):
                sorted_pop.append(pop[idx])
        smallest_att+=1
    # Then pick the parent by this patern [1]x[2];[2]x[3];[3]x[4];...
    for i in range(math.ceil(len(sorted_pop)/2)):
        parent.append(sorted_pop[i])
        parent.append(sorted_pop[i+1])
    return parent

def crossover(parent):
    child = []

    # Alternating point Crossover
    for i in range(0,(len(parent)),2):
        temp1 = []
        temp2 = []
        for j in range(len(parent[0])):
            if (randint(0,1)==1):       # 50% chance for each genetic code to crossover
                temp1.append(parent[i][j])
                temp2.append(parent[i+1][j])
            else:
                temp1.append(parent[i+1][j])
                temp2.append(parent[i][j])
        child.append(temp1)
        child.append(temp2)
    return child

# each crossed child have a chance to mutated with probabilty of 0-100% 
def mutation(child,m_rate,chess_size):

    mutated_child = []
    for i in range(len(child)):
        temp = []
        for j in range(len(child[i])):
            if (randint(0,100)<m_rate):
                temp.append(randint(0,chess_size-1))
            else:
                temp.append(child[i][j])
        mutated_child.append(temp)

    return mutated_child

# Procedure to remove excess population after choosing parent crossing
def odd_population():
    #Detecting even total population 
    if (len(pop) != pop_size):
        mx_idx = fit_score.index(max(fit_score))
        pop.pop(mx_idx)
        fit_score.pop(mx_idx)

# Finding the solution within the population
def solution(fit_score,pop):
    for idx, i in enumerate (fit_score):
        if i == 0:
            return pop[idx]

# After find the solution we convert it into chessboard           
def draw_chess(answer):
    for i in range(len(answer)):
        temp = []
        for j in range(len(answer)):
            if i == answer[j]:
                temp.append("X")
            else:
                temp.append("O")
        print(temp)

#Setting Section
chess_size = 6
pop_size = 5
mutation_rate = 10
max_gen = None

pop = generatePopulation(chess_size,pop_size)
# pop=[[0, 0, 3, 3, 2], [3, 1, 3, 2, 4], [1, 1, 1, 0, 4], [3, 0, 3, 2, 4], [1, 3, 0, 0, 4]]
res = None
gen = 0
while(res==None):
    if gen == max_gen:
        break
   
    fit_score = fittest_score(pop)
    odd_population()
    print("\nGeneration ", gen," = ",pop)
    print(fit_score)

    res = solution(fit_score,pop)
    if res!=None:
        # print("Final Generation = ",pop)
        print("Chess Position = ",res)
        # print("generation = ",gen)
        draw_chess(res)
        break

    # Genettic breeding section
    parent = choose_parent(pop,fit_score)
    print("parent = ",parent)
    child = crossover(parent)
    print("Child = ",child)
    pop = mutation(child,mutation_rate,chess_size)
    print("Mutated = ",pop)
    gen+=1












