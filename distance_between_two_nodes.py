def solution(root, val1, val2):
    n1_a = find_node_path(root, val1)
    n2_a = find_node_path(root, val2)

    if len(n1_a) is 0 or len(n2_a) is 0:
        return -1

    for i in range(max(len(n1_a), len(n2_a))):
        if i is len(n1_a) or i is len(n2_a):
            n1_a = n1_a[i-1:]
            n2_a = n2_a[i-1:] - 1
            break

        if n1_a[i] is not n2_a[i]:
            n1_a = n1_a[i:]
            n2_a = n2_a[i:]
            break

    return len(n1_a) + len(n2_a) + 1


def find_node_path(node, val, a=[]):
    if node is None:
        return []

    a.append(node.val)

    if node.val is val:
        return a
    elif val < node.val:
        return find_node_path(node.left, val, a)
    else:
        return find_node_path(node.right, val, a)
