#!/usr/bin/env python

# test1.py

for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=k) and (j!=k) and (i!=j):
				print i,j,k