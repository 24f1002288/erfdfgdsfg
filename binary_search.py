def binary_search(l:list,elem):
    if len(l) == 0:
        return False
    mid_index = len(l)//2
    if elem == l[mid_index]:
        return True
    elif elem > l[mid_index]:
        return binary_search(l[mid_index+1:],elem)
    else:
        return binary_search(l[:mid_index],elem)
    
print(binary_search([1,4,6,9,12,15,18],18))