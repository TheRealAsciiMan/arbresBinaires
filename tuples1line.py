example = ("Root", ("Child A", ("Under-Child A", None, None), None), ("Child B", None, None))
exampleRoot = ("Root", None, None)

def size(arbre) -> int: return 0 if arbre is None else 1 + size(arbre[1]) + size(arbre[2])
def height(arbre) -> int: return 0 if arbre is None or (arbre[1] is None and arbre[2] is None) else 1 + max(height(arbre[1]), height(arbre[2]))
def leaves(arbre) -> int: return 0 if arbre is None else 1 if arbre[1] is None and arbre[2] is None else leaves(arbre[1]) + leaves(arbre[2])
def internalNodes(arbre) -> int: return 0 if arbre is None or (arbre[1] is None and arbre[2] is None) else 1 + internalNodes(arbre[1]) + internalNodes(arbre[2])

tree_str = lambda arbre, level=0: "    " * level + arbre[0] + "\n" + (tree_str(arbre[1], level + 1) if arbre[1] is not None else "") + (tree_str(arbre[2], level + 1) if arbre[2] is not None else "") if arbre is not None else ""



print("Taille:", size(example))
print("Hauteur:", height(example))
print("Feuilles:", leaves(example))
print("Noeuds internes:", internalNodes(example))
print("Dessins :\n", tree_str(example))
print("\nTaille:", size(exampleRoot))
print("Hauteur:", height(exampleRoot))
print("Feuilles:", leaves(exampleRoot))
print("Noeuds internes:", internalNodes(exampleRoot))
