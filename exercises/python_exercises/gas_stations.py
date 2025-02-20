# Gas Stations
# Hard
# There's a circular route which contains gas stations. At each station, you can fill your car with a certain amount of gas, and moving from that station to the next one consumes some fuel.

# Find the index of the gas station you would need to start at, in order to complete the circuit without running out of gas. Assume your car starts with an empty tank. If it's not possible to complete the circuit, return -1. If it's possible, assume only one solution exists.

# Example:
# Input:  gas = [2, 5, 1, 3], cost = [3, 2, 1, 4]
# Output: 1
# Explanation:

# Start at station 1: gain 5 gas (tank = 5), costs 2 gas to go to station 2 (tank = 3).
# At station 2: gain 1 gas (tank = 4), costs 1 gas to go to station 2 (tank = 3).
# At station 3: gain 3 gas (tank = 6), costs 4 gas to go to station 3 (tank = 2).
# At station 0: gain 2 gas (tank = 4), costs 3 gas to go to station 1 (tank = 1).
# We started and finished the circuit at station 1 without running out of gas.

from typing import List

def gas_stations(gas: List[int], cost: List[int]) -> int:
    # Write your code here
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank = total_tank + gas[i] - cost[i]
        current_tank = current_tank + gas[i] - cost[i]

        #if current tank is negative then reset
        if current_tank < 0:
            current_tank = 0
            start_index = i+1

    return start_index if total_tank >= 0  else -1


gas = [2, 5, 1, 3]
cost = [3, 2, 1, 4]

print(gas_stations(gas, cost))