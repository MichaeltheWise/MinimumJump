# -*- coding: utf-8 -*-
"""
Created on Mon May 3 2021

@author: Michael Lin
"""
# Given a list of possible jumps, calculate the minimum number of jumps needed to reach the end
import collections


def minimumJumpGreedy(jump_list):
    """
    Using Greedy algorithm to get the minimum jump possible
    :param jump_list: list of possible jumps
    :return: Minimum jump to reach the end
    """
    # If less than 2 elements, just return
    if len(jump_list) <= 1:
        return 0

    curr_range, max_range, jump = 0, 0, 0
    for i in range(len(jump_list)):
        curr_range = max(curr_range, i + jump_list[i])

        # If reach the end of the current jump range
        # update the maximum jump range with what we can achieve between previous starting point and max jump point
        # Then we continue on with the new starting point and new max jump point
        if i == max_range:
            jump += 1
            max_range = curr_range

        # If it goes over the range, just return right away
        if max_range >= len(jump_list) - 1:
            return jump


def minimumJumpDP(jump_list):
    """
    Using Dynamic Programming to get the minimum jump possible
    :param jump_list: list of possible jumps
    :return: Minimum jump to reach the end
    """
    # Intuitive DP method
    minimum_jump_list = [float('inf')] * len(jump_list)
    minimum_jump_list[0] = 0

    # Calculate the minimum possible jump to reach that point at each location
    for i in range(1, len(jump_list)):
        for j in range(i):
            if jump_list[j] + j >= i:
                minimum_jump_list[i] = min(minimum_jump_list[i], minimum_jump_list[j] + 1)
    return minimum_jump_list[-1]


def minimumJumpGreedyWithDP(jump_list):
    """
    Using similar Greedy idea but using Dynamic Programming for distance mapping
    :param jump_list: list of possible jumps
    :return: Minimum jump to reach the end
    """
    curr_range = 0
    jump = 0
    dist_map = collections.defaultdict(int)

    # Similar to what we are doing with Greedy
    # Trying to find the maximum distance we can achieve within each jump interval
    # With one step, we can reach 3
    # Within that range, try to find the maximum range we can reach
    # then update the possible second jump max distance
    for index, num in enumerate(jump_list):
        if index > curr_range:
            jump += 1
            curr_range = dist_map[jump]
        dist_map[jump + 1] = max(dist_map[jump + 1], index + num)
    return jump


def minimumCoverage(spray_range):
    """
    Calculate minimum number of fountain/sprinkler/tap that needs to cover the region
    :param spray_range: spray range/radius
    :return: Minimum number of fountain/sprinkler/tap needed
    """
    jump_list = [0] * len(spray_range)
    for index, radius in enumerate(spray_range):
        if radius == 0:
            continue
        left = max(0, index - radius)
        right = min(len(spray_range), index + radius)
        # Need to format it into this format to match the jump list format
        # At each point, we need to figure out the max possible jump range
        jump_list[left] = max(jump_list[left], right - left)
    print("Jump range: {}".format(jump_list))

    # After transformation, we can use one of the three ways listed to calculate
    return minimumJumpGreedy(jump_list)


def main():
    jump_list = [3, 2, 1, 1, 4]
    print("Greedy: {}".format(minimumJumpGreedy(jump_list)))
    print("DP Method 1: {}".format(minimumJumpDP(jump_list)))
    print("DP Method 2: {}".format(minimumJumpGreedyWithDP(jump_list)))

    # If given fountains or sprinklers or taps
    # need to transform it into a list similar to jump list
    # Input will be:
    # 1. The ground that needs to be covered
    # 2. The fountain/sprinkler/tap's spray range/radius
    print("\nMinimum coverage questions")
    spray_range1 = [3, 4, 1, 1, 0, 0]
    print("Spray range1: {}".format(spray_range1))
    print("Minimum coverage1: {}".format(minimumCoverage(spray_range1)))

    spray_range2 = [1, 2, 1, 0, 2, 1, 0, 1]
    print("\nSpray range2: {}".format(spray_range2))
    print("Minimum coverage2: {}".format(minimumCoverage(spray_range2)))

    spray_range3 = [4, 0, 0, 0, 0, 0, 0, 0, 4]
    print("\nSpray range3: {}".format(spray_range3))
    print("Minimum coverage3: {}".format(minimumCoverage(spray_range3)))

    spray_range4 = [4, 0, 0, 0, 4, 0, 0, 0, 4]
    print("\nSpray range4: {}".format(spray_range4))
    print("Minimum coverage4: {}".format(minimumCoverage(spray_range4)))


if __name__ == '__main__':
    main()
