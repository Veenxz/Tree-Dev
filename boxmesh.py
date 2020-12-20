# -*- coding: utf-8 -*-

# Libraries

# Function definitions
def headerLines(cl, loc, obj, con="convertToMeters 1;"):
    h = [
        "/*--------------------------------*- C++ -*----------------------------------*|",
        "| =========                 |                                                 |",
        "| \\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |",
        "|  \\\    /   O peration     | Website:  https://openfoam.org                  |",
        "|   \\\  /    A nd           | Version:  7                                     |",
        "|    \\\/     M anipulation  |                                                 |",
        "\*---------------------------------------------------------------------------*/",
        "FoamFile", "{", "    version     2.0;", "    format      ascii;",
        "    class       {};", '    location    "{}";', "    object      {};",
        "}",
        "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //",
        "", "{}", ""
    ]

    h[11] = h[11].format(cl)
    h[12] = h[12].format(loc)
    h[13] = h[13].format(obj)
    h[17] = h[17].format(con)
    return h

# Define 
H = 4
deltax = 0.2
ls = [-1.5, 1.5, -2.5, 6, 0, 2.5]

bl = '    '
loc = "system"
cl = "dictionary"
obj = "blockMeshDict"
nt = "nx ny nz".split(" ")
lt = "xmin xmax ymin ymax zmin zmax".split(" ")
ct = "$xmin $xmax $ymin $ymax $zmin $zmax".split(" ")

ll = []
for i in ls:
    ll.append(H * i)


f = open(loc+'/'+obj, "w")

header = headerLines(cl, loc, obj)
for l in range(len(header)):
    f.write("{}\n".format(header[l]))

f.write("//coord\n")
for i in range(6):
    f.write(lt[i] + bl + str(ll[i]) + ';\n')

for i in range(3):
    l = -ll[2 * i] + ll[2 * i + 1]
    n = l / deltax
    f.write(nt[i] + bl + str(int(n)) + ';\n')

#vertices
f.write("\nvertices\n")
f.write("(\n")
f.write(bl + '( ' + ct[0] + ' ' + ct[2] + ' ' + ct[4] + ' )\n')
f.write(bl + '( ' + ct[1] + ' ' + ct[2] + ' ' + ct[4] + ' )\n')
f.write(bl + '( ' + ct[1] + ' ' + ct[3] + ' ' + ct[4] + ' )\n')
f.write(bl + '( ' + ct[0] + ' ' + ct[3] + ' ' + ct[4] + ' )\n')
f.write(bl + '( ' + ct[0] + ' ' + ct[2] + ' ' + ct[5] + ' )\n')
f.write(bl + '( ' + ct[1] + ' ' + ct[2] + ' ' + ct[5] + ' )\n')
f.write(bl + '( ' + ct[1] + ' ' + ct[3] + ' ' + ct[5] + ' )\n')
f.write(bl + '( ' + ct[0] + ' ' + ct[3] + ' ' + ct[5] + ' )\n')
f.write(");\n")

# blocks
f.write("\nblocks\n")
f.write("(\n")
f.write(bl + 'hex (0 1 2 3 4 5 6 7) ' + '( ' + '$' + nt[0] + ' $' + nt[1] +
        ' $' + nt[2] + ' )' + ' simpleGrading (1 1 1)')
f.write("\n);\n")

# edges
f.write("\nedges\n")
f.write("(\n")
f.write(");\n")

# patches
f.write("\npatches\n")
f.write("(\n")
f.write(bl + 'patch inlet\n' + bl + '(\n' + 2 * bl + '(1 5 4 0)\n' + bl +
        ')\n\n')
f.write(bl + 'patch outlet\n' + bl + '(\n' + 2 * bl + '(3 7 6 2)\n' + bl +
        ')\n\n')
f.write(bl + 'wall land\n' + bl + '(\n' + 2 * bl + '(0 3 2 1)\n' + bl +
        ')\n\n')
f.write(bl + 'wall symmetry\n' + bl + '(\n' + 2 * bl + '(2 6 5 1)\n' + 2 * bl +
        '(0 4 7 3)\n' + 2 * bl + '(4 5 6 7)\n' + bl + ')\n\n')
f.write(");\n")

# mergePatchPairs
f.write("\nmergePatchPairs\n")
f.write("(\n")
f.write(");\n")

# footer
f.write(
    '// ************************************************************************* //'
)

f.close()

print(obj + ' Generation Finshed!')
