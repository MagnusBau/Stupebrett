import scipy as sp
import scipy.sparse


def generateA(n):
    e = [1] * n
    a = sp.sparse.spdiags([e, [x * -4 for x in e], [x * 6 for x in e], [x * -4 for x in e], e], [-2, -1, 0, 1, 2], n, n).toarray()
    a = a.astype('object')
    a[0][0:4] = [16,-9,8.0/3,-(1.0/4)]
    a[n-2][n-4:n] = [16.0/17,-(60.0/17),(72.0/17),-(28.0/17)]
    a[n-1][n-4:n] = [-(12/17.0),96.0/17,-(156.0/17),72.0/17]
    return a

