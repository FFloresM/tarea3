from Union_find import List_Set, List_Set_T


lst = List_Set_T()

lst.makeSet(4)
lst.makeSet(7)

lst.Union(4, 7)

print(lst.Buscar(4))
print(lst.Buscar(7))


