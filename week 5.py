# minimax
import math

scores = [3, 5, 2, 9, 0, 7,0,0]
treeDepth = math.ceil(math.log2(len(scores)))

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

    if curDepth == targetDepth:
        return scores[nodeIndex], 1

    left_val, left_leaves = minimax(curDepth + 1, nodeIndex * 2, not maxTurn, scores, targetDepth)
    right_val, right_leaves = minimax(curDepth + 1, nodeIndex * 2 + 1, not maxTurn, scores, targetDepth)

    best = max(left_val, right_val) if maxTurn else min(left_val, right_val)
    return best, left_leaves + right_leaves

scores += [0] * (2**treeDepth - len(scores))

value, leaves = minimax(0, 0, True, scores, treeDepth)
print("The optimal value is:", value)
print("Leaf nodes evaluated:", leaves)


# alpha beta pruning


scores = [3, 5, 2, 9, 3, 5, 2, 9] 
depth = int(math.log2(len(scores)))

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    if depth == target:
        return scores[index], 1

    leaves = 0
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            child_val, child_leaves = alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta)
            leaves += child_leaves
            value = max(value, child_val)
            alpha = max(alpha, value)
            if alpha >= beta:
                break 
        return value, leaves
    else:
        value = float('inf')
        for i in range(2):
            child_val, child_leaves = alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta)
            leaves += child_leaves
            value = min(value, child_val)
            beta = min(beta, value)
            if alpha >= beta:
                break  
        return value, leaves

value, leaves = alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf'))
print("The optimal value is:", value)
print("Leaf nodes evaluated:", leaves, "of", len(scores))


#Reorder branches


scores = [3, 5, 2, 9, 0, 7, 0, 0]
depth = int(math.log2(len(scores)))

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    if depth == target:
        return scores[index], 1

    leaves = 0
    if maxTurn:
        value = float('-inf')
        for i in [1, 0]:
            child_val, child_leaves = alphabeta(depth + 1, index * 2 + i, False,scores, target, alpha, beta)
            leaves += child_leaves
            value = max(value, child_val)
            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return value, leaves

    else:
        value = float('inf')
        for i in [1, 0]:
            child_val, child_leaves = alphabeta(depth + 1, index * 2 + i, True,scores, target, alpha, beta)
            leaves += child_leaves
            value = min(value, child_val)
            beta = min(beta, value)

            if alpha >= beta:
                break
        return value, leaves

value, leaves = alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf'))

print("The optimal value is:", value)
print("Leaf nodes evaluated:", leaves, "of", len(scores))
print("Leaf nodes pruned:", len(scores) - leaves)