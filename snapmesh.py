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


bl = '    '
loc = "system"
cl = "dictionary"
obj = "snappyHexMeshDict"
