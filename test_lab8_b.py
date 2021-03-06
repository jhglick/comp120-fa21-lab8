# File: test_lab8_b.py
# Author: John Glick    
# Date: 
# Description: Program that tests the correctness of 
#       the longest_increasing_subsequence funcion.

import sys

# import the module containing psa1 solution
import longest_increasing_subsequence

#inputs = ["", "a", "ab", "abcd", "ababc", "ababcdeabcd", "abcabcdgabxy"]
#correct_answers = ["", "a", "ab", "abcd", "abc", "abcde", "abcdg"]
inputs = ["", "a", "ab", "ba", "arbmncABdea", "welcome"]
correct_answers = ["", "a", "ab", "b", "abcde", "elo"]

if __name__ == "__main__":
    # Try all test problems
    num_tested = 0
    num_correct = 0
    for i in range(len(inputs)):
        print(f"Test # {i}")
        ans = longest_increasing_subsequence.longest_increasing_subsequence(inputs[i])
        num_tested += 1
        print(f"   Input = '{inputs[i]}'")
        print(f"   Your answer = '{ans}'")
        print(f"   Correct answer = '{correct_answers[i]}'")
        if ans == correct_answers[i]:
            print("   Correct")
            num_correct += 1
        else:
            print("   Incorrect")
        print()
    if num_correct == num_tested:
        print("All correct.  Nice job")
    else:
        print("Not all correct.  Keep working on it")