# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
casefoam = GetActiveSource()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# create a new 'Clip'
clip1 = Clip(Input=casefoam)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 1.3536567687988281

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [21.0, 14.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [21.0, 14.0, 0.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1515, 792]

# get layout
layout1 = GetLayout()

# Properties modified on renderView1
renderView1.CameraParallelProjection = 1

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.RGBPoints = [-37.91002655029297, 0.231373, 0.298039, 0.752941, 0.07976150512695312, 0.865003, 0.865003, 0.865003, 38.069549560546875, 0.705882, 0.0156863, 0.14902]
pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-37.91002655029297, 0.0, 0.5, 0.0, 38.069549560546875, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 9.8
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.GaussianRadius = 0.49
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 1.418034182963471
clip1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-35.36223602294922, 0.0, 0.5, 0.0, 38.069549560546875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-35.36223602294922, 0.0, 0.5, 0.0, 38.069549560546875, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'UMean', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'UMean'
uMeanLUT = GetColorTransferFunction('UMean')
uMeanLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 7.53227519999796, 0.865003, 0.865003, 0.865003, 15.06455039999592, 0.705882, 0.0156863, 0.14902]
uMeanLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'UMean'
uMeanPWF = GetOpacityTransferFunction('UMean')
uMeanPWF.Points = [0.0, 0.0, 0.5, 0.0, 15.06455039999592, 1.0, 0.5, 0.0]
uMeanPWF.ScalarRangeInitialized = 1

# reset view to fit data
renderView1.ResetCamera()

# rescale color and/or opacity maps used to exactly fit the current data range
clip1Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [21.0, 14.0, 190.53327633793214]
renderView1.CameraFocalPoint = [21.0, 14.0, -10.5]
renderView1.CameraParallelScale = 29.37027887586978
renderView1.CameraParallelProjection = 1

# save screenshot
SaveScreenshot('/home/veen/Disk/Mycase/Tree/0523_new/U_01.tiff', renderView1, ImageResolution=[3030, 1584],
    OverrideColorPalette='WhiteBackground')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [21.0, 14.0, 190.53327633793214]
renderView1.CameraFocalPoint = [21.0, 14.0, -10.5]
renderView1.CameraParallelScale = 29.37027887586978
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).