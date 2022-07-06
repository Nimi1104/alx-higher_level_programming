#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return list(sorted(a_dictionary.items(),
                           key=lambda kv: kv[1]))[-1][0]
