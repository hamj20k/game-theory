# -*- coding: utf-8 -*-
"""BRdynamics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mQvbdWTAu31Y8vl-zy0dGKOw9FIm8NIv
"""

import numpy as np

def best_response(M, opponent_action):
    """
    Finds the best response action for a given player based on the opponent's action.
    """
    return np.argmax(M[:, opponent_action])

def BRdynamics(M1, M2, a1, a2, T):
    """
    Simulates best response dynamics for a 2-player matrix game.

    Parameters:
    M1, M2: np.array
        Reward matrices for players 1 and 2.
    a1, a2: int
        Initial actions for players 1 and 2 (0-indexed).
    T: int
        Number of stages to simulate.

    Returns:
    A1, A2: list
        Histories of actions for players 1 and 2, respectively.
    """
    A1 = [a1]  # Player 1's action history
    A2 = [a2]  # Player 2's action history

    for t in range(T):
        # Player 1 best response to Player 2's last action
        a1 = best_response(M1, A2[-1])
        A1.append(a1)

        # Player 2 best response to Player 1's last action
        a2 = best_response(M2, A1[-1])
        A2.append(a2)

    return A1, A2

# Example usage
M1 = np.array([[3, 1], [5, 2]])  # Player 1's payoff matrix
M2 = np.array([[2, 4], [1, 3]])  # Player 2's payoff matrix
a1, a2 = 0, 1  # Initial actions
T = 10  # Number of stages

A1, A2 = BRdynamics(M1, M2, a1, a2, T)
print("Player 1 action history:", A1)
print("Player 2 action history:", A2)