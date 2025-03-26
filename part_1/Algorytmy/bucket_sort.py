# Złozoność czasowa: 
#  - optymistyczna: O(n)
#  - pesymistyczna: O(n log(n))  
# Złozoność pamięciowa: O(n)

def bucket_sort(T):
    n=len(T) 
    if n==0:
        return T
    max_val=max(T)
    min_val=min(T)
    if max_val==min_val:
        return T
    size=(max_val-min_val)/n
    buckets=[[] for i in range(n)]  # we create as many buckets as there are elements in the array
    for i in range(n):
        j=int((T[i]-min_val)/size)
        if j!=n:
            buckets[j].append(T[i])
        else:
            buckets[n-1].append(T[i])
    for i in range(n):
        buckets[i]=sorted(buckets[i]) # we sort buckets, usually with the insertion sort or quicksort, here i used the python function
    idx=0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[idx]=buckets[i][j]  #we put values to the main array in rhe right order
            idx+=1
    return T 