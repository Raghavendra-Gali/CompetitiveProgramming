def is_balanced(tree_root):

    # Determine if the tree is superbalanced
    if tree_root==None:
        return True
    l=heigth(tree_root.left)
    r=heigth(tree_root.right)
    
    if abs(l-r)<=1 and is_balanced(tree_root.left) and is_balanced(tree_root.right):
        return True
    return False
    
def heigth(node):
    if node==None:
        return 0
    return 1+max(heigth(node.left),heigth(node.right))
