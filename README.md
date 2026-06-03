# Capacitated Vehicle Routing Problem Genetic Algorithm

This project implements a Genetic Algorithm to solve a Capacitated Vehicle Routing Problem (CVRP). The algorithm assigns customer nodes to multiple vehicles while considering vehicle capacity constraints and attempts to minimize the total travel distance.

## Features

* Solves or optimizes a vehicle routing problem using a Genetic Algorithm
* Supports adjustable number of vehicles
* Supports vehicle capacity constraints
* Uses selection, crossover, mutation, and elite strategy
* Reads distance matrix and demand data from Excel files
* Plots the convergence curve of the best distance over generations

## File Description

### `main.py`

The main entry point of the program. It reads input data, initializes the population, runs the Genetic Algorithm, and plots the result.

### `ga.py`

Contains the main Genetic Algorithm functions, including:

* `cost()`
* `tru()`
* `selection()`
* `mutation()`
* `crossover_mutation()`
* `getmincost()`
* `getmingene()`

### `config.py`

Stores configurable parameters such as population size, generation number, vehicle number, capacity, mutation rate, crossover rate, and input file paths.

### `data/`

Stores the input Excel files. There are two files provided for testing.

## Input Data

The program requires two Excel files:

### Distance Matrix

The distance matrix should contain the distance between every pair of nodes. Node `0` represents the depot.

Example structure:

| Node |  0 |  1 |  2 |  3 |
| ---- | -: | -: | -: | -: |
| 0    |  0 | 10 | 15 | 20 |
| 1    | 10 |  0 |  8 | 12 |
| 2    | 15 |  8 |  0 |  6 |
| 3    | 20 | 12 |  6 |  0 |

### Demand Data

The demand data should contain the demand volume of each node. The first value should be `0`, representing the depot.

Example:

|  0 |  1 |  2 |  3 |
| -: | -: | -: | -: |
|  0 |  4 |  3 |  5 |


## Requirements

numpy
pandas
matplotlib
openpyxl

## How to Run

Run main.py

## Configuration

You can change the main parameters in `config.py`:

size = 100
Gen = 200
vehicleNum = 3
carry = 60
muR = 0.1
crR = 0.8
nodeNum = 71

Parameter meaning:

| Parameter    | Meaning                      |
| ------------ | ---------------------------- |
| `size`       | Population size              |
| `Gen`        | Number of generations        |
| `vehicleNum` | Number of available vehicles |
| `carry`      | Vehicle capacity             |
| `muR`        | Mutation rate                |
| `crR`        | Crossover rate               |
| `nodeNum`    | Number of customer nodes     |

## Output

The program prints the progress of each generation and displays a convergence plot showing how the best distance changes over generations.

The final result includes the best chromosome and its total distance.

## Chromosome Representation

In this project, `0` represents the depot. It is also used as a route separator between vehicles.

Example chromosome:

[0, 5, 8, 12, 0, 3, 7, 10, 0]


This represents two vehicle routes:


Vehicle 1: Depot -> 5 -> 8 -> 12 -> Depot
Vehicle 2: Depot -> 3 -> 7 -> 10 -> Depot


## Genetic Algorithm Design

The algorithm includes the following steps:

1. Generate an initial population
2. Evaluate the cost of each chromosome
3. Select parent chromosomes
4. Apply crossover and mutation
5. Check capacity constraints
6. Keep the best chromosome using elite strategy
7. Repeat for multiple generations

## Notes

* The current version is designed for Excel input files.
* Make sure the distance matrix and demand data use consistent node numbering.
* Node `0` should represent the depot.
* The total demand should not exceed the total vehicle capacity.
* The running time could be very long if total demand close to total capacity

## Future Improvements

Possible future improvements include:

* Rename some variables and functions to make it easier to understand
* Find a better strategy of creating initial group (problem mentioned in fifth Notes).
* Add a graphical user interface
* Allow users to upload input files
* Export final routes to Excel
* Visualize vehicle routes on a map
* Support different crossover and mutation methods
* Support different elite number

## License

This project is licensed under the MIT License.
