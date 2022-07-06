

def edit_distance(s1, s2, m, n):
    if m==0: return n
    if n==0: return m

    if s1[m-1] == s2[n-1]:
        return edit_distance(s1,s2,m-1,n-1)
    else:
        return 1 + min(edit_distance(s1,s2,m-1,n), edit_distance(s1,s2,m,n-1), edit_distance(s1,s2,m-1,n-1))

print(edit_distance("CAT", "CUT", 3, 3))


