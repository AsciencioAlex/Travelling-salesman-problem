
# Name: 
# wNumber: 
# Project name: proj02
# Assigned: Sept 23
# Due date: Oct 08
# Tested on:

import pickle
import time

start_time = time.time()

def path_cost ( n, dist, p ):


  c = 0.0
  i1 = n - 1
  for i2 in range ( 0, n ):
    c = c + dist [ p[i1], p[i2] ]
    i1 = i2

  return c

def path_cost_test ( ):

  import numpy as np
  import platform

  n = 11

  dist = np.array ( [\
[ 0.0,  3.0,  4.0,  2.0,  9.0, 2.0, 3.0, 1.0, 7.0, 8.0, 6.0],
[ 3.0,  0.0,  4.0,  6.0,  3.0, 4.0, 7.0, 4.0, 0.0, 5.0, 6.0],
[ 4.0,  4.0,  0.0,  5.0,  8.0, 9.0, 5.0, 0.0, 4.0, 2.0, 2.0],
[ 2.0,  6.0,  5.0,  0.0,  6.0, 7.0, 6.0, 3.0, 5.0, 4.0, 3.0],
[ 0.0,  3.0,  4.0,  2.0,  9.0, 5.0, 8.0, 4.0, 2.0, 4.0, 7.0],
[ 3.0,  0.0,  4.0,  6.0,  3.0, 5.0, 8.0, 4.0, 0.0, 3.0, 4.0],
[ 4.0,  4.0,  0.0,  5.0,  8.0, 4.0, 3.0, 7.0, 6.0, 4.0, 5.0],
[ 2.0,  6.0,  5.0,  0.0,  6.0, 2.0, 4.0, 8.0, 9.0, 5.0, 6.0],
[ 0.0,  3.0,  4.0,  2.0,  9.0, 6.0, 3.0, 5.0, 0.0, 3.0, 8.0],
[ 3.0,  0.0,  4.0,  6.0,  3.0, 4.0, 9.0, 6.0, 9.0, 5.0, 5.0],
[ 4.0,  4.0,  0.0,  5.0,  8.0, 6.0, 4.0, 7.0, 9.0, 0.0, 3.0]
 ] )

  p = np.array ( [ 0, 3, 2, 1, 4, 5, 6, 8, 9, 7, 10 ] )



  print ( '' )
  print ( '  Number of cities n = %d' % ( n ) )
  print ( '' )
  print ( '  Distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( dist[i,j] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Optimum path:' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( p[i] ), end = '' )
  print ( '' )

  c = path_cost ( n, dist, p )

  print ( '' )
  print ( '  Cost of this path is %g' % ( c ) )
#
#  Terminate.
#
  print("--- %s seconds ---" % (time.time() - start_time))
  print ( '  ENDING PROJ02 OUTPUT' )
  return

if ( __name__ == '__main__' ):
  #from timestamp import timestamp
  #timestamp ( )
  path_cost_test ( )
  print("--- %s seconds ---" % (time.time() - start_time))
  #timestamp ( )
