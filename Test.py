#! /usr/bin/env python
#
def permutation ( n, p, more, rank ):

  if ( not more ):

    for i in range ( 0, n ):
      p[i] = i
    more = True
    rank = 1

  else:

    n2 = n
    m2 = rank
    s = n

    while ( True ):

      q = ( m2 % n2 )
      t = ( m2 % ( 2 * n2 ) )

      if ( q != 0 ):
        break

      if ( t == 0 ):
        s = s - 1

      m2 = ( m2 // n2 )
      n2 = n2 - 1

      if ( n2 == 0 ):
        for i in range ( 0, n ):
          p[i] = i
        more = False
        rank = 1
        break

    if ( n2 != 0 ):

      if ( q == t ):
        s = s - q
      else:
        s = s + q - n2

      t      = p[s-1]
      p[s-1] = p[s]
      p[s]   = t

      rank = rank + 1

  return p, more, rank

def permutation_test ( ):

  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM0_NEXT3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_NEXT3 generates permutations in order.' )
  print ( '' )

  n = 4
  p = np.zeros ( n )
  more = False
  rank = 0
 
  while ( True ):

    p, more, rank = permutation ( n, p, more, rank )

    if ( not more ):
      break

    print ( '  %3d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_NEXT3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_next3_test ( )
  timestamp ( )

