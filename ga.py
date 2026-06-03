# Genetic algorithm functions

import random
import numpy as np


def cost(dna, dist):
    cost=0
    pos1=0
    pos2=0
    posnum=0
    for i in dna:
        posnum+=1
        if posnum==1:
            pos1=i
        elif posnum==2:
            pos2=i
            cost+=dist[pos1][pos2]
            posnum=1
            pos1=i
            pos2=0
    return cost


def tru(os, vol, carry):
    jud=0
    tot_vol=0
    for i in os:
        if i != 0:
            tot_vol+=vol[i]
            if tot_vol>carry:
                jud=1
        if i==0:
            tot_vol=0
    return jud


def selection(pop, size, dist):
    new_pop=[]
    while len(new_pop)<size:
        sele1=random.randint(0,size-1)
        sele2=random.randint(0,size-1)
        tst1=pop[sele1]
        tst2=pop[sele2]
        fitness1=cost(tst1, dist)
        fitness2=cost(tst2, dist)
        if fitness1>fitness2:
            new_pop.append(tst2)
        if fitness1<fitness2:
            new_pop.append(tst1)
        if fitness1==fitness2:
            new_pop.append(tst1)
    return new_pop


def getmincost(popu, dist):
    allfit=[]
    for i in popu:
        sinfit=cost(i, dist)
        allfit.append(sinfit)
    mincost=min(allfit)
    return mincost


def getmingene(popu, dist):
     allfit = []
     inde=0
     memo=[]
     for i in popu:
         sinfit = cost(i, dist)
         allfit.append(sinfit)
         compo=[sinfit,inde]
         memo.append(compo)
         inde+=1
     mincost = min(allfit)
     memopos=allfit.index(mincost)
     mingenepos=memo[memopos][1]
     mingene=popu[mingenepos]
     return mincost,mingene


def mutation(son):
    mutpos1=random.randint(1,len(son)-2)
    mutpos2=random.randint(1,len(son)-2)
    while son[mutpos1]==0 or son[mutpos2]==0 or mutpos1 == mutpos2:
        mutpos1=random.randint(1,len(son)-2)
        mutpos2=random.randint(1,len(son)-2)
    mutgene1=son[mutpos1]
    mutgene2=son[mutpos2]
    son[mutpos1]=mutgene2
    son[mutpos2]=mutgene1
    return son


def crossover_mutation(popu,sze,mR):
    fatherpos=0
    motherpos=0
    while fatherpos==motherpos:
        fatherpos=random.randint(0,sze-1)
        motherpos=random.randint(0,sze-1)
    fath=popu[fatherpos]
    moth=popu[motherpos]
    father=fath.copy()
    mother=moth.copy()
    crogene1=0
    crogene2=0
    son1=father
    son2=mother
    while crogene1==0 or crogene2==0:
        cropoint=random.randint(1,len(father)-2)
        crogene1=father[cropoint]
        crogene2=mother[cropoint]
    if crogene1!=crogene2:
        replfath=father.index(crogene2)
        father[replfath]=crogene1
        son1=father
        replmoth=mother.index(crogene1)
        mother[replmoth]=crogene2
        son2=mother
        son1[cropoint]=crogene2
        son2[cropoint]=crogene1
    if crogene1==crogene2:
        son1[cropoint]=crogene2
        son2[cropoint]=crogene1
    if random.uniform(0,1) <= mR:
        son1=mutation(son1)
        son2=mutation(son2)
    return son1,son2


def create_initial_group(size, nodeNum, vehicleNum, vol, carry):
    group=[]
    while len(group)<size:
        lst=list(range(1, nodeNum + 1))
        np.random.shuffle(lst)
        zeroCount=vehicleNum - 1
        max_demand=max(vol)
        min_nodes_per_vehicle=int(carry // max_demand)

        insePos=[]
        lastPos=min_nodes_per_vehicle

        for z in range(zeroCount):
            remaining_zeros=zeroCount-z

            minPos=lastPos
            maxPos=len(lst)-min_nodes_per_vehicle*remaining_zeros

            if minPos>=maxPos:
                break

            pos=random.randint(minPos, maxPos)
            insePos.append(pos)

            lastPos=pos+min_nodes_per_vehicle

        if len(insePos)!=zeroCount:
            continue

        insePos.sort(reverse=True)

        for pos in insePos:
            lst.insert(pos, 0)

        lst.insert(0, 0)
        lst.append(0)

        if tru(lst, vol, carry)==0:
            group.append(lst)
            print(lst)
    return group
