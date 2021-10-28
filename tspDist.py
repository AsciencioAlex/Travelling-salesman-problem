#! /usr/bin/env python3
#

# Name: 
# wNumber: 
# Project name: proj02
# Assigned: Sept 23
# Due date: Oct 08
# Tested on:

def tsp_brute ( filename ):

  import numpy as np
  import platform
  from tsp import path_cost
  from Test import permutation
  from sys import exit
  


  
  
  print ( '' )
  print ( 'TSP:' )
  print ( '  Solve small traveling salesman problems by brute force.' )
#
#  Get the distance table.
#
  print ( '' )
  print ( '  Distance matrix filename is "%s"' % ( filename ) )

  distance = np.loadtxt ( filename )
#
#  Approve the distance table.
#
  dims = distance.shape

  m = dims[0]
  n = dims[1]

  if ( m != n ):
    print ( '' )
    print ( 'Fatal error!' )
    print ( '  The distance matrix must be square.' )
    print ( '  Your matrix has M = %d, N = %d', m, n )
    exit ( ' Fatal error!' )

  v = np.diagonal ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'Fatal error!' )
    print ( '  The distance matrix must have zero diagonal.' )
    print ( '  Your matrix has ||diag(D)|| = %g', test )
    exit ( 'Fatal error!' )

  test = np.linalg.norm ( distance - distance.transpose ( ) )

  if ( 0.0 < test ):
    print ( '' )
    print ( ' Fatal error!' )
    print ( '  The distance matrix must be symmetric.' )
    print ( '  Your matrix has ||D-D''|| = %g' % ( test ) )
    exit ( ' Fatal error!' )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  The city-to-city distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )
#
#  Examine every permutation.
#
  total_max = - np.inf
  total_min = np.inf
  total_ave = 0.0

  p = np.zeros ( n, dtype = np.int32 )
  more = False
  rank = 0

  p_min = np.zeros ( n, dtype = np.int32 )

  paths = 0

  while ( True ):

    p, more, rank = permutation ( n, p, more, rank )

    if ( not more ):
      break

    paths = paths + 1

    total = path_cost ( n, distance, p )

    total_ave = total_ave + total

    if ( total_max < total ):
      total_max = total

    if ( total < total_min ):
      total_min = total
      p_min = p.copy ( )

  total_ave = total_ave / paths
#
#  Report.
#
  print ( '' )
  print ( '  A minimal distance  itinerary:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )
  for i1 in range ( 0, n ):
    i2 = ( ( i1 + 1 ) % n )
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i2, p_min[i1], p_min[i2], distance[p_min[i1],p_min[i2]] ) )

  print ( '  ----    --  --  --------------' )
  print ( '  Total:          %14.6g' % ( total_min ) )

  print ( '' )
  print ( '  Number of paths checked = %d' % ( paths ) )
  print ( '' )
  print ( '  Minimum distance = %g' % ( total_min ) )
  print ( '  Average distance = %g' % ( total_ave ) )
  print ( '  Maximum distance = %g' % ( total_max ) )

  return
#
#  Terminate.
#
 
  return

def tsp_brute_test ( ):


  import numpy as np
  import platform
  import time

  start_time = time.time()

  

  filename = 'myInputFile.txt'

  print ( '' )
  print ( '  Call tsp ( %s )' % ( filename ) )
  tsp_brute ( filename )
#
#  Termination of the
#
  
  print ( '' )
 
  print ( '  ENDING PROJ02 OUTPUT.' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
 
  tsp_brute_test ( )
 
