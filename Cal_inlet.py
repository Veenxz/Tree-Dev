import math
from datetime import datetime

# Print Head
print(
      '\n',
      '* * * * * Welcome to use Fluid Characteristics Calculator * * * * *\n',
      '*                   Beijing Forestry University                   *\n',
      '*                          Author: Veenxz                         *\n',
      12*'* ', datetime.now().strftime('%Y-%m-%d %H:%M:%S '), 12*'* ', '\n',
      sep='')

# user define 1
z_f = 0.01
h = 2.0
u_h = 10.0
yplus = 1.0
basex = 0.5

print(
      34*'- ', '\n',
      '-  ', 'User defined friction hight is ', z_f, ' [m]\n',
      '-  ', 'User defined reference hight is ', h, ' [m]\n',
      '-  ', 'User defined reference velocity is ', u_h, ' [m/s]\n',
      '-  ', 'User defined base Y+ is ', yplus, ' [ ]\n',
      '-  ', 'User defined base mesh size is ', basex, ' [m]\n',
      34*'- ', '\n',
      sep='')

# define constant
cmu = 0.09
mu = 1.78938e-05
rho = 1.225
kappa = 0.41
l = h
u = u_h

print(
      34*'* ', '\n',
      '*  ', 'User defined Cmu is ', cmu, ' [ ]\n',
      '*  ', 'User defined reference hight is ', mu, ' [m]\n',
      '*  ', 'User defined density is ', rho, ' [m/s]\n',
      '*  ', 'User defined kappa is ', kappa, ' []\n',
      '*  ', 'User defined reference length is ', l, ' [m]\n',
      '*  ', 'User defined reference velocity is ', u_h, ' [m/s]\n',
      34*'* ', '\n',
      sep='')

print(
      '\n',
      '- - - - - - - - - - - - - - - Results - - - - - - - - - - - - - - -\n',
      sep='')

# Inlet Profile
u_f = u_h * kappa / (math.log(h / z_f + 1))

print('Inlet Profile is','u = ' + str("%.6f" % (u_f / kappa)) + '*log(z/' + str(z_f) + '+1)',
      '[m/s]\n')

# turbulence characteristics calculator
re = rho * u * l / mu
intensity = 0.16 * pow(re, -1 / 8)
length_scale = 0.07 * l / pow(cmu, 3 / 4)
tke = 3 * pow(intensity * u, 2) / 2
tdr = pow(tke, 3 / 2) / length_scale
mut = cmu * pow(3 / 2, 1 / 2) * u * intensity * length_scale
tvr = mut / mu
tdrr = rho * tke / (mu * tvr)
lmin = pow(pow(mu/rho,3)/tdr,1/4)
tmin = lmin/u_h

print(
    "Re =",
    "%.2f" % re,
    '[]',
    "\nI =",
    "%.6f" % (intensity * 100),
    '%',
    "\nLength_scale =",
    "%.6f" % length_scale,
    '[m]',
    "\nTKE =",
    "%.6f" % tke,
    '[m2/s2]',
    "\nTDR =",
    "%.6f" % tdr,
    '[m2/s3]',
    "\nmut =",
    "%.6f" % mut,
    '[]',
    "\nTVR =",
    "%.6f" % tvr,
    '[]',
    "\ntdrr =",
    "%.6f" % tdrr,
    '[1/s]',
    "\nlmin =",
    "%.6f" % lmin,
    '[m]',
    "\ntmin =",
    "%.6f" % tmin,
    '[s]\n',
)

# deltas calculator
cf = 0.026 / pow(re, 1 / 7)
tauwall = cf * rho * pow(u, 2) / 2
ufric = pow(tauwall / rho, 1 / 2)
FLH = yplus * mu / (ufric * rho)

print('When Yplus =', yplus, ', First Layer Hight is', "%.4e" % FLH, '[m]')

# time step calculator
tmax = basex / u
tmin = 0.3 * tmax
tr = 0.35 * tmax

print('Recommend time step is', "%.2e" % tr, '[s]')
print('Allowed time step range is', "%.2e" % tmax, '[s]', 'to', "%.2e" % tmin,
      '[s]')
