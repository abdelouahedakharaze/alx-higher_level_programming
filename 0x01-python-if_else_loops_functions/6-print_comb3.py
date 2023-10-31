#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            print(f"0{j},", end=" ")
        else:
            print(f"{i}{j},", end=" ")
