from itertools import combinations, permutations

import numpy as np
import streamlit as st

st.title("Fast Upgrade Game Elements")

st.header(" Find The Best path to Upgrade  ")


def func(p, q, m):
    t = 0
    for i, j in m.items():
        t = t+(i-p)/q
        q = q+j*q/100
        p = 0
    print(p, q, t)
    return t


col_a, col_b = st.columns(2)
col_a = st.number_input(" Input Current value", value=0)
col_b = st.number_input(" Input Current Rate of gain", min_value=0)
check_points = st.slider("Number of check points",
                         min_value=2, max_value=10, step=1)

if col_b:
    l = []
    for i in range(check_points):
        col1, col2 = st.columns([3, 3])
        col1 = st.number_input(
            " Required Amount", key=f"col1_{i}", min_value=5, step=5)
        col2 = st.number_input(" % increment in rate of gain",
                               key=f"col2_{i}", min_value=5, max_value=2000, step=5)
        l.append((col1, col2))

    all_perm = list(map(dict, permutations(l)))
    time_taken = list(map(lambda x: func(col_a, col_b, x), all_perm))

    st.header("Minimum Time")

    st.write(min(zip(all_perm, time_taken), key=lambda x: x[1])[0].keys())
    st.write(min(time_taken))

    st.header("Maximum Time")
    st.write(max(zip(all_perm, time_taken), key=lambda x: x[1])[0].keys())
    st.write(max(time_taken))
