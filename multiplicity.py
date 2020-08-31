# Worker routines to compute stat mech functions

import math
import matplotlib.pyplot as plt
import stirling
from types import *

def multiplicity (N, s):

# Assume N even, -N/2 <= s <= N/s

  if (N % 2 != 0) :
    raise Exception ("N must be even.")

  Nup = N / 2 + s
  Ndown = N / 2 - s

  val =  math.factorial (N) / (math.factorial (Nup) * math.factorial (Ndown) )

  return val


def entropy (N, s):

  if (N % 2 != 0) :
    raise Exception ("N must be even.")

  Nup = N / 2 + s
  Ndown = N / 2 - s

  val = stirling.logfact (N) - stirling.logfact (Nup) - stirling.logfact (Ndown)

  return val


# Multiplicity of combined spin system; assume N1 < N2, N even
# Further require s <= (N2 - N1) / 2

def totalmultiplicity (N1, N2, s):

  totalmult = 0
  multlist = []
  s1list   = []
  s2list   = []
  oldterm  = 0
  first    = True

  if ((isinstance (N1, int) == False) or (isinstance (N2, int) == False) ) :
    raise Exception ("N1 and N2 must be integers.")

  if (N2 < N1) :
    raise Exception ("N1 must be <= N2.")

  if (s > (N2 - N1) / 2 ):
    raise Exception ("Spin excess s <= (N2 - N1) / 2")

# We assume N1, N2 even, but we have to convert to integer for factorial
  for s1 in range (int (-N1/2), int (N1/2 ) + 1 ) :

    s2 = s - s1
    term = multiplicity (N1, s1) * multiplicity (N2, s2)
    if (term < oldterm) and (first == True) :
      print ("Maximum multiplicity at s1/N1 = ", s1list[-1], "s2/N2 = ", s2list[-1], " mult = ", multlist[-1])
      first = False
    multlist.append (term)
    s1list.append (s1 / N1)
    s2list.append (s2 / N2)
    oldterm    = term
    totalmult += term

  plt.xlabel('$s_1 / N_1$', fontsize=30)
  plt.ylabel('Multiplicity', fontsize=30)
  plt.grid(b=True, which='major', color='DarkTurquoise', alpha=0.4, linestyle=':', linewidth=2)
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='beige', alpha=0.2, linestyle='-', linewidth=2)
  plt.tick_params(axis='both', which='major', labelsize=10)
  plt.tick_params(axis='both', which='minor', labelsize=8)

  plt.plot (s1list, multlist, linewidth=3)
  plt.show()

  return totalmult

# Log10 Multiplicity of combined spin system; assume N1 < N2, N even
# Further require s <= (N2 - N1) / 2

def totalentropy (N1, N2, s):

  totalmult = 0
  multlist = []
  s1list   = []
  s2list   = []
  oldterm = 0
  first    = True

  if ((isinstance (N1, int) == False) or (isinstance (N2, int) == False) ) :
    raise Exception ("N1 and N2 must be integers.")

  if (N2 < N1) :
    raise Exception ("N1 must be <= N2.")

  if (s > (N2 - N1) / 2 ):
    raise Exception ("Spin excess s <= (N2 - N1) / 2")

# We assume N1, N2 even, but we have to convert to integer for factorial
  for s1 in range (int (-N1/2), int (N1/2 ) + 1 ) :

    term = entropy (N1, s1) + entropy (N2, s - s1)
    if (term < oldterm) and (first == True) :
      print ("Maximum multiplicity at s1/N1 = ", s1list[-1], "s2/N2 = ", s2list[-1], " mult = ", multlist[-1])
      first = False
    multlist.append (term)
    s1list.append (s1 / N1)
    s2list.append ( (s - s1) / N2)
    oldterm = term
    totalmult += term

  plt.plot (s1list, multlist)
  plt.show()

  return totalmult


def gaussentropy (N, s):

  import math
  pi = math.pi

# Simply take the log of multiplicity in the Stirling/Gaussian large N limit,
#  g (N, s) \simeq (2 / pi N)^(1./2.) * 2**N * exp (-2 s^2/N)   

  logg0 = (N + 0.5) * math.log (2.) - 0.5 * math.log (pi * N) 
  val = logg0 - 2 * s**2. / N

  return val


