# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
casefoam = FindSource('case.foam')

# create a new 'Calculator'
calculator1 = Calculator(Input=casefoam)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'TKE'
calculator1.Function = '0.5*((U_X-UMean_X)^2+(U_Y-UMean_Y)^2+(U_Z-UMean_Z)^2)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1452, 749]

# get layout
layout1 = GetLayout()

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'TKE'
tKELUT = GetColorTransferFunction('TKE')
tKELUT.RGBPoints = [5.624115562187571e-18, 0.231373, 0.298039, 0.752941, 96.15375488397606, 0.865003, 0.865003, 0.865003, 192.30750976795213, 0.705882, 0.0156863, 0.14902]
tKELUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TKE'
tKEPWF = GetOpacityTransferFunction('TKE')
tKEPWF.Points = [5.624115562187571e-18, 0.0, 0.5, 0.0, 192.30750976795213, 1.0, 0.5, 0.0]
tKEPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'TKE']
calculator1Display.LookupTable = tKELUT
calculator1Display.OSPRayScaleArray = 'TKE'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 9.8
calculator1Display.SelectScaleArray = 'TKE'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'TKE'
calculator1Display.GaussianRadius = 0.49
calculator1Display.SetScaleArray = ['POINTS', 'TKE']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'TKE']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = tKEPWF
calculator1Display.ScalarOpacityUnitDistance = 0.9917183989340451
calculator1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [5.624115562187571e-18, 0.0, 0.5, 0.0, 178.90070590096377, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [5.624115562187571e-18, 0.0, 0.5, 0.0, 178.90070590096377, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'SEP'
calculator2.Function = '(9+(2*0.1/3)^0.5)/(mag(UMean)+(2*TKE/3)^0.5)'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'SEP'
sEPLUT = GetColorTransferFunction('SEP')
sEPLUT.RGBPoints = [0.39325929906661644, 0.231373, 0.298039, 0.752941, 22.3765937278675, 0.865003, 0.865003, 0.865003, 44.35992815666838, 0.705882, 0.0156863, 0.14902]
sEPLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SEP'
sEPPWF = GetOpacityTransferFunction('SEP')
sEPPWF.Points = [0.39325929906661644, 0.0, 0.5, 0.0, 44.35992815666838, 1.0, 0.5, 0.0]
sEPPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'SEP']
calculator2Display.LookupTable = sEPLUT
calculator2Display.OSPRayScaleArray = 'SEP'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'U'
calculator2Display.ScaleFactor = 9.8
calculator2Display.SelectScaleArray = 'SEP'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'SEP'
calculator2Display.GaussianRadius = 0.49
calculator2Display.SetScaleArray = ['POINTS', 'SEP']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'SEP']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = sEPPWF
calculator2Display.ScalarOpacityUnitDistance = 0.9917183989340451
calculator2Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.39325929906661644, 0.0, 0.5, 0.0, 44.35992815666838, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.39325929906661644, 0.0, 0.5, 0.0, 44.35992815666838, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [21.0, 14.0, 212.95981173352172]
renderView1.CameraFocalPoint = [21.0, 14.0, 0.0]
renderView1.CameraParallelScale = 55.11805511808268

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

# find source
calculator2 = FindSource('Calculator2')

# create a new 'Calculator'
calculator3 = Calculator(Input=calculator2)
calculator3.Function = ''

# find source
casefoam = FindSource('case.foam')

# find source
calculator1 = FindSource('Calculator1')

# Properties modified on calculator3
calculator3.ResultArrayName = 'I'
calculator3.Function = 'sqrt(2*TKE/3)/mag(UMean)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1515, 792]

# get layout
layout1 = GetLayout()

# show data in view
calculator3Display = Show(calculator3, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'I'
iLUT = GetColorTransferFunction('I')

# get opacity transfer function/opacity map for 'I'
iPWF = GetOpacityTransferFunction('I')

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'I']
calculator3Display.LookupTable = iLUT
calculator3Display.OSPRayScaleArray = 'I'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'U'
calculator3Display.ScaleFactor = 35.35999984741211
calculator3Display.SelectScaleArray = 'I'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'I'
calculator3Display.GaussianRadius = 1.7679999923706056
calculator3Display.SetScaleArray = ['POINTS', 'I']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'I']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityFunction = iPWF
calculator3Display.ScalarOpacityUnitDistance = 2.579284001385729
calculator3Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 452.91867600828385, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 452.91867600828385, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [95.20000076293945, 20.399982393681057, 666.0706318385227]
renderView1.CameraFocalPoint = [95.20000076293945, 20.399982393681057, -34.0]
renderView1.CameraParallelScale = 84.52722443385242
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
