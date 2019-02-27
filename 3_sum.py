# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:04:58 2019

@author: manik
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
         n=len(A)
         # checking whether there are atleast 3 elements
         if n<3:
             return None
         final=0
         A.sort()
         import sys
         mini=sys.maxsize
         for i in range(n-2):
             j=i+1
             k=n-1
             while(j<k):
                 s=A[i]+A[j]+A[k]
                 diff=abs(s-B)
                 if diff==0:
                     return s
                 #checking  between current sum and minimal sum
                 if diff<mini:
                     mini=diff
                     final=s
                 #if sum is less than target value will be incresed else decreased    
                 if s<=B:
                     j=j+1
                 else:
                     k=k-1
         return final