import matplotlib.pyplot as plot
import numpy as np

signal = np.array([0,1,2,1,3,4,0,2,0,5,0,3,2,3,4,1,9,5,7,3,6,2,4,4,2,2,1,5,1,4,3,2,3,2,6,5,6,8,2,2,2,2,2,9,5,4,7,8,1,5,4,8,7,9,8])

ss = signal.shape[0]
filter_c = np.array([4,3,2,3,2,6,5,6,8,2,2,2,2,2,9])
L = len(filter_c)
k = int( L/2)

res = np.zeros( ss )

maxv = [-1, 0]

F2 = np.sqrt( sum(filter_c ** 2) )

for i in range( k, signal.shape[0] - k  ):

    soma = 0
    norT = 0
    
    for n in range( -k, k + 1 ):
        F = filter_c[ n + k ]
        
        T =  signal[ n - i ]
    
        soma += F * T
        norT += T**2

    res[ss - i] = soma / ( F2 * np.sqrt( norT ) )
    
    if( res[i] >= maxv[1] ):
        maxv = [i, res[i]]

print( filter_c )
print( signal[ maxv[0] - k : maxv[0] + k + 1 ] )

signal[ maxv[0] - k : maxv[0] + k + 1 ]  *= 2

plot.plot( res * 10 )
plot.plot( signal )
plot.show()
