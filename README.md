# Multi-Armed Bandit

## 1. Overview

This project involves solving the multi-armed bandit problem using the epsilon-greedy algorithm. The multi-armed bandit problem deals with a decision maker iteratively selecting an arm from multiple choices, each with an unknown probability distribution of rewards. As the algorithm iterates and chooses different arms, the decision maker learns more about the rewards from choosing certain arms. This is known as the exploration phase. Following the exploration phase, the decision maker will select an arm with the highest expected award, known as the exploitation phase. The multi-armed bandit problem was solved using the epsilon-greedy algorithm.

## 2. Algorithm

The epsilon-greedy algorithm involves the epsilon parameter, ε, which is used to determine the likeliness for the algorithm to explore the choices of the problem. After choosing a random number, if the number is below ε, the algorithm will choose a random action. Otherwise, the algorithm will choose the arm with the current highest expected award. The algorithm continues this process on all data points in the data. Following the building of this model, we are able to use the testing data to produce a success rate by exploiting the most successful arm discovered by the algorithm.

## 3. Dataset

The dataset included in this repo, but not limited to, is time series data representing a library's WIFI channel occupancy. The dataset has eleven columns representing the eleven channels, while the rows represent the signal strength at each time. For the purposes of this dataset, our goal is to choose a WIFI channel whose signal strength meets a specified threshold which is given by the user.

## 4. Usage

The program can be executed with the line:  
`python tester.py FILENAME EPSILON TRAIN% THR`

- `tester.py` is the name of the python program
- `FILENAME` is the name of the input data file, csv format
- `EPSILON` is the ε value for the epsilon-greedy algorithm
- `TRAIN%` is the percentage of the dataset that will be used for training purposes
 - accepts integer values from 0-50, where the value is 50(%)
- `THR` represents the success threshold, used to determine whether choices are considered successes
