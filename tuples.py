example = ("Root", ("Child A", ("Under-Child A", None, None), None), ("Child B", None, None))
exampleRoot =  ("Root", None, None)

def size(arbre) -> int:
    if arbre is None:
        return 0
    return 1 + size(arbre[1]) + size(arbre[2])

def height(arbre) -> int:
    if arbre is None or (arbre[1] is None and arbre[2] is None):
        return 0
    return 1 + max(height(arbre[1]), height(arbre[2]))

def leaves(arbre) -> int:
    if arbre is None:
        return 0
    if arbre[1] is None and arbre[2] is None:
        return 1
    return leaves(arbre[1]) + leaves(arbre[2])

def internalNodes(arbre) -> int:
    if arbre is None:
        return 0
    if arbre[1] is None and arbre[2] is None:
        return 0
    return 1 + internalNodes(arbre[1]) + internalNodes(arbre[2])

def tree_str(arbre, level=0):
    if arbre is not None:
        result = "    " * level + arbre[0] + "\n"
        if arbre[1] is not None:
            result += tree_str(arbre[1], level + 1)
        if arbre[2] is not None:
            result += tree_str(arbre[2], level + 1)
        return result
    else:
        return ""

print("Taille:", size(example))
print("Hauteur:", height(example))
print("Feuilles:", leaves(example))
print("Noeuds internes:", internalNodes(example))
print("Dessins :\n\n", tree_str(example))
print("\n\nTaille:", size(exampleRoot))
print("Hauteur:", height(exampleRoot))
print("Feuilles:", leaves(exampleRoot))
print("Noeuds internes:", internalNodes(exampleRoot))
