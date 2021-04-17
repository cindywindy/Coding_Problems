# Given a binary search tree, write a function to find the kth smallest element in the tree.
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
    self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
#find the smallest by finding the leftmost node
        return self.left