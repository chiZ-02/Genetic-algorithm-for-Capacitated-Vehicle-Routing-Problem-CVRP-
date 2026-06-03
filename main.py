# Run this file

import random
import matplotlib.pyplot as plt
import pandas as pd

from config import DIST_FILE, DEMAND_FILE, size, carry, muR, crR, Gen, vehicleNum, nodeNum
from ga import selection, getmincost, getmingene, crossover_mutation, tru, create_initial_group


def main():
    dataDist = pd.read_excel(DIST_FILE)
    dataDemand = pd.read_excel(DEMAND_FILE)

    plt.figure()

    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    xpoint=[]
    ypoint=[]

    group=[]
    vol=dataDemand.values.tolist()[0]
    dist=dataDist.values.tolist()

    for i in range(0,Gen+1):
        xpoint.append(i)

    group=create_initial_group(size, nodeNum, vehicleNum, vol, carry)

    minc=getmincost(group, dist)
    ypoint.append(minc)

    for i in range(0,Gen):
        selected_group=selection(group, size, dist)
        new_popu=[]
        newpop1=0
        newpop2=0
        a, elite=getmingene(group, dist)
        new_popu.append(elite)
        while len(new_popu)<size:
            rate=random.uniform(0,1)
            if rate<=crR:
                newpop1,newpop2=crossover_mutation(selected_group,size,muR)
            elif rate>crR:
                a,newpop1=getmingene(selected_group, dist)
                newpop2=newpop1.copy()
                del a
            if tru(newpop1, vol, carry)==0 and tru(newpop2, vol, carry)==0:
                new_popu.append(newpop1)
                if len(new_popu)<size:
                    new_popu.append(newpop2)
        minc=getmincost(new_popu, dist)
        ypoint.append(minc)
        group=new_popu
        print(f"generation {i}")

    print(getmingene(group, dist))

    plt.scatter(xpoint, ypoint, color='r', label='Points')
    plt.plot(xpoint, ypoint, color='b', label='Line')
    plt.title('GA')
    plt.xlabel('generation')
    plt.ylabel('distances')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
