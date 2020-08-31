# Define factorial using Stirling approximation
import math

def fact_stirling (n) :

   pi = math.pi
   e = math.exp (1.)

   a = 1. / 12.
   b = 1. / 288.
   c = 139. / 51840.
   d = 571 / 2488320.

   correction = 1 + a  / n + b / n**2. - c / n**3. - d / n**4.
   return (2. * pi * n)**(1./2.) * (n / e)**n * correction

# Define log factorial using Stirling approximation

def logfact (n) :

   pi = math.pi
   e = math.exp (1.)

   a = 1. / 12.
   b = 1. / 288.
   c = 139. / 51840.
   d = 571 / 2488320.

# Stirling approximation diverges as n -> 0; set this by hand.

   if (n > 1) :
     correction = 1 + a  / n + b / n**2. - c / n**3. - d / n**4.
     logcorr    = math.log (correction)
     val = 0.5 * math.log (2. * pi * n) + n * math.log (n / e) + logcorr
   else :
     val = 0

   return val
