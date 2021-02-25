import sys
sys.setrecursionlimit(10**6)

preorderList = []
postorderList = []

class Tree:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.left = None
        self.right = None

def preorder_traverse(node):
    preorderList.append(node.number)
    if node.left:
        preorder_traverse(node.left)
    if node.right:
        preorder_traverse(node.right)

def postorder_traverse(node):
    if node.left:
        postorder_traverse(node.left)
    if node.right:
        postorder_traverse(node.right)
    postorderList.append(node.number)

def solution(nodeinfo):
    # nodeinfo_with_index = [info + [idx + 1] for idx, info in enumerate(nodeinfo)]
    # nodeinfo_with_index = sorted(list({node[1] for node in nodeinfo_with_index}), reverse=True)
    # answer = nodeinfo_with_index

    # levels = sorted(list({node[1] for node in nodeinfo}), reverse=True)
    # answer = levels
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1), nodeinfo)), key= lambda x: (-x[1][1], x[1][0]))
    # print('nodes : ', nodes)
    root_node = None
    for node in nodes:
        if not root_node:
            root_node = Tree(node[1][0], node[1][1], node[0])
        else:
            x = node[1][0]
            curr_node = root_node
            while True:
                if x < curr_node.x:
                    if curr_node.left:
                        curr_node = curr_node.left
                        continue
                    else:
                        curr_node.left = Tree(node[1][0], node[1][1], node[0])
                        break
                if x > curr_node.x:
                    if curr_node.right:
                        curr_node = curr_node.right
                        continue
                    else:
                        curr_node.right = Tree(node[1][0], node[1][1], node[0])
                        break
                break

    preorder_traverse(root_node)
    postorder_traverse(root_node)

    answer = [preorderList, postorderList]

    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = solution(nodeinfo)
print(result)
