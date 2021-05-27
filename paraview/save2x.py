# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1515, 792]

# get layout
layout1 = GetLayout()

# save screenshot
SaveScreenshot('./pic.tiff', renderView1, ImageResolution=[3030, 1584],
    OverrideColorPalette='WhiteBackground')