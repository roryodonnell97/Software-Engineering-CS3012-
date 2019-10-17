
# A binary tree node 
class Node: 
    # Constructor to create a new binary node 
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
        self.xAncestor = False
        self.yAncestor = False
        self.count = 0


# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false 
def findPath( root, path, k): 
  
    # Baes Case 
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True

    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove 
    # root from path and return False 
       
    path.pop() 
    return False



# function which checks if there is two paths from the root node to k
def check_for_two_paths( root, path, k):

    if root is None: 
        return None
    
    if (root.left is None or root.right is None):
        return None

    if ((findPath(root.left, path, k)) and
            (findPath(root.right, path, k))): 
        return root     



# function which checks if tree is DAG and if is DAG returns a root which has two paths too desired node (k)
def is_tree_DAG( root, path, k):

    if root is None: 
        return 
    
    if (root.left is None or root.right is None):
        return 

    if(check_for_two_paths( root, path, k) == root):
        return root

    if(root.left != None):
        return is_tree_DAG( root.left, path, k)

    if(root.right != None):
        return is_tree_DAG( root.right, path, k)

    return None    



# Returns LCA if node n1 , n2 are present in the given 
# binary tree otherwise return -1 
def findLCA(root, n1, n2): 
  
    # To store paths to n1 and n2 fromthe root 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 



def find_LCA_DAG(root, n1, n2):

    path1_1 = [] 
    path2_1 = [] 

    # return either None or a node with a path to n1 for node1 or n2 for node2
    node1 = is_tree_DAG( root, path1_1, n1)
    node2 = is_tree_DAG( root, path2, n2)


    # if no DAG found then find LCA regular way
    if(node1 is None and node2 is None):
        return findLCA(root, n1, n2)

    path1_1 = []
    path1_2 = []
    path2_1 = []
    path2_2 = []

    if(node1 is None):
        findPath(root, path1_1, n1)
    else
        findPath(root, path1_1, node1)
        findPath(node1.left, path1_1, n1)

        findPath(root, path1_2, node1)
        findPath(node1.right, path1_2, n1)

    if(node2 is None):
        findPath(root, path2_1, n2)  
    else
        findPath(root, path2_1, node2)
        findPath(node2.left, path2_1, n2)

        findPath(root, path2_2, node2)
        findPath(node2.right, path2_2, n2) 
  
    i = 0 
    while(i < len(path1) and i < len(path2)):  

# function which uses is_tree_DAG(root,path,k) for nodes n1 n2 given in LCA query. 
# If not DAG, find LCA normal way
# else Compare paths to nodes and find LCA between paths (should be n1 or n2 k found in either paths, whichever is first(higher))