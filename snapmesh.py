# -*- coding: utf-8 -*-

# Libraries


# Function definitions
def headerLines(cl, loc, obj):
    h = [
        "/*--------------------------------*- C++ -*----------------------------------*|",
        "| =========                 |                                                 |",
        "| \\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |",
        "|  \\\    /   O peration     | Website:  https://openfoam.org                  |",
        "|   \\\  /    A nd           | Version:  8                                     |",
        "|    \\\/     M anipulation  |                                                 |",
        "\*---------------------------------------------------------------------------*/",
        "FoamFile", "{", "    version     2.0;", "    format      ascii;",
        "    class       {};", '    location    "{}";', "    object      {};",
        "}",
        "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //",
        ""
    ]

    h[11] = h[11].format(cl)
    h[12] = h[12].format(loc)
    h[13] = h[13].format(obj)
    return h


bl = '    '
loc = "system"
cl = "dictionary"
obj = "snappyHexMeshDict"

castellatedMesh = 'true'
snap = 'true'
addLayers = 'false'

H = 14
h = 4.8
hr = 0.5
NS = 4.5
WE = 3.6
# N = 2n+1
n = [0, 1]
d = [10, 10]
r = [0, 1, 2, 3, 4]

rr = 1.2 * hr


# X Dir (flow dir)
def DX(x):
    return (d[0] * n[0] + x * WE)


x = [DX(-3), DX(10), DX(-5), DX(15), DX(-8), DX(20)]


# Y Dir (H dir)
def DY(k):
    return (H + k * (H - h))


y = [0, DY(0.6), DY(1.0), DY(1.5)]


# Z Dir
def DZ(z):
    return (d[1] * n[1] + z * NS)


z = [DZ(1.5), DZ(2.0), DZ(3)]

# file location system/snappyHexMeshDict
f = open(loc + '/' + obj + '.header', "w")

header = headerLines(cl, loc, obj)
for l in range(len(header)):
    f.write("{}\n".format(header[l]))

f.write('// Which of the steps to run\n')
f.write('castellatedMesh ' + castellatedMesh + ';\n')
f.write('snap            ' + snap + ';\n')
f.write('addLayers       ' + addLayers + ';\n')

f.write('\n// Geometry info: H = ' + str(H) + bl + 'h = ' + str(h) + bl +
        'NS = ' + str(NS) + bl + 'WE = ' + str(WE) + bl +
        '\n// Row * Columns is ' + str(2 * n[0] + 1) + '*' +
        str(2 * n[1] + 1) + bl + 'Space Row * Columns is ' + str(d[0]) + '*' +
        str(d[1]) + 2 * '\n')

f.write('x00' + bl + '% .2f' % x[0] + ';' + 2 * bl)
f.write('x01' + bl + '% .2f' % x[1] + ';' + 2 * bl)
f.write('x10' + bl + '% .2f' % x[2] + ';' + 2 * bl)
f.write('x11' + bl + '% .2f' % x[3] + ';' + 2 * bl)
f.write('\n')
f.write('x20' + bl + '% .2f' % x[4] + ';' + 2 * bl)
f.write('x21' + bl + '% .2f' % x[5] + ';' + 2 * bl)
f.write('y00' + bl + '% .3f' % y[0] + ';' + 2 * bl)
f.write('y01' + bl + '% .2f' % y[1] + ';' + 2 * bl)
f.write('\n')
f.write('y02' + bl + '% .2f' % y[2] + ';' + 2 * bl)
f.write('y03' + bl + '% .2f' % y[3] + ';' + 2 * bl)
f.write('z00' + bl + '% .2f' % z[0] + ';' + 2 * bl)
f.write('z01' + bl + '% .2f' % -z[0] + ';' + 2 * bl)
f.write('\n')
f.write('z10' + bl + '% .2f' % z[1] + ';' + 2 * bl)
f.write('z11' + bl + '% .2f' % -z[1] + ';' + 2 * bl)
f.write('z20' + bl + '% .2f' % z[2] + ';' + 2 * bl)
f.write('z21' + bl + '% .2f' % -z[2] + ';' + 2 * bl)
f.write('\n')
f.write('r1 ' + bl + '% .0f' % r[0] + ';' + 3 * bl)
f.write('r2 ' + bl + '% .0f' % r[1] + ';' + 3 * bl)
f.write('r3 ' + bl + '% .0f' % r[2] + ';' + 3 * bl)
f.write('r4 ' + bl + '% .0f' % r[3] + ';' + 3 * bl)
f.write('\n')
f.write('h  ' + bl + '% .2f' % h + '; ' + 2 * bl)
f.write('hr ' + bl + '% .2f' % rr + '; ' + 2 * bl)
f.write('rc ' + bl + '% .0f' % r[4] + ';')

f.close()

print(obj + '.header' + ' Generation Finshed!')
