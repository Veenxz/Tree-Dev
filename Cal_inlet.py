import math

# user define 1
z_f = 0.01
h = 4
u_h = 5
yplus = 5.0
basex = 1.0

# define constant
cmu = 0.09
mu = 1.78938e-05
rho = 1.225
kappa = 0.41
l = h
u = u_h

u_f = u_h * kappa / (math.log(h / z_f + 1))

print('u = ' + str("%.6f" % (u_f / kappa)) + '*log(z/' + str(z_f) + '+1)',
      '[m/s]')

# turbulence characteristics calculator
re = rho * u * l / mu
intensity = 0.16 * pow(re, -1 / 8)
length_scale = 0.07 * l / pow(cmu, 3 / 4)
tke = 3 * pow(intensity * u, 2) / 2
tdr = pow(tke, 3 / 2) / length_scale
mut = cmu * pow(3 / 2, 1 / 2) * u * intensity * length_scale
tvr = mut / mu
tdrr = rho * tke / (mu * tvr)

print(
    "Re =",
    "%.2f" % re,
    '[]',
    "\nI =",
    "%.6f" % (intensity * 100),
    '%',
    "\nlength_scale =",
    "%.6f" % length_scale,
    '[m]',
    "\ntke =",
    "%.6f" % tke,
    '[m2/s2]',
    "\ntdr =",
    "%.6f" % tdr,
    '[m2/s3]',
    "\nmut =",
    "%.6f" % mut,
    '[]',
    "\ntvr =",
    "%.6f" % tvr,
    '[]',
    "\ntdrr =",
    "%.6f" % tdrr,
    '[1/s]',
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
