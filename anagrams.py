# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:07:36 2019

@author: manik
"""

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
           result=[]
           a=list(range(len(A)))           
           for i in a:
             temp=[]
             temp.append(i+1)
             for j in range(i+1,len(A)):                
                if(sorted(A[i])==sorted(A[j])):
                 a.remove(j)
                 temp.append(j+1)
             result.append(temp)         
           return result 