# coding=utf-8
import numpy as np
import scipy as sp
import scipy.sparse


# Genererer en båndmatrise med størrelse [n,n].
def generateA(n):
    e = [1] * n
    # Sender inn data og størrelse (n)
    a = sp.sparse.spdiags([e, [x * -4 for x in e], [x * 6 for x in e], [x * -4 for x in e], e], [-2, -1, 0, 1, 2], n, n).toarray()
    # Dette er fordi arrayen ikke vil ha brøker.
    a = a.astype('object')
    # Første og de to siste linjene må lages separat.
    a[0][0:4] = [16,-9,8.0/3,-(1.0/4)]
    a[n-2][n-4:n] = [16.0/17,-(60.0/17),(72.0/17),-(28.0/17)]
    a[n-1][n-4:n] = [-(12/17.0),96.0/17,-(156.0/17),72.0/17]
    # Konverterer til en sp.array. Punktumet etter 0 er viktig så brøkene ikke blir avrundet.
    b = sp.array([[0.] * n ] * n)
    for x in range(len(a)):
        b[x] = a[x]
    # Sender ut den ferdige båndmatrisen.
    return b