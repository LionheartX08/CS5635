# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Arrow'
arrows = [Arrow() for i in range(16)]
rotation = 0
renderView1 = GetActiveViewOrCreate('RenderView')
for arrow in arrows:
    # set active source
    SetActiveSource(arrow)
    # show data in view
    arrow1Display = Show(arrow, renderView1, 'GeometryRepresentation')
    Hide(arrow, renderView1)

    shrink = Shrink(Input=arrow)
    extractEdges = ExtractEdges(Input=arrow)
    SetActiveSource(shrink)
    shrinkDisplay = Show(shrink, renderView1)
    SetActiveSource(extractEdges)
    edgesDisplay = Show(extractEdges, renderView1)

# trace defaults for the display properties.
    arrow1Display.Representation = 'Surface'
    arrow1Display.ColorArrayName = [None, '']
    arrow1Display.SelectTCoordArray = 'None'
    arrow1Display.SelectNormalArray = 'None'
    arrow1Display.SelectTangentArray = 'None'
    arrow1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    arrow1Display.SelectOrientationVectors = 'None'
    arrow1Display.ScaleFactor = 0.1
    arrow1Display.SelectScaleArray = 'None'
    arrow1Display.GlyphType = 'Arrow'
    arrow1Display.GlyphTableIndexArray = 'None'
    arrow1Display.GaussianRadius = 0.005
    arrow1Display.SetScaleArray = [None, '']
    arrow1Display.ScaleTransferFunction = 'PiecewiseFunction'
    arrow1Display.OpacityArray = [None, '']
    arrow1Display.OpacityTransferFunction = 'PiecewiseFunction'
    arrow1Display.DataAxesGrid = 'GridAxesRepresentation'
    arrow1Display.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
    renderView1.ResetCamera()

# Properties modified on arrow1
    arrow.TipResolution = 12

# show data in view
    arrow1Display = Show(arrow, renderView1, 'GeometryRepresentation')

# reset view to fit data
    renderView1.ResetCamera()

# get the material library
    materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
    renderView1.Update()

# Properties modified on arrow1Display
    arrow1Display.Orientation = [0.0, 0.0, rotation]

# Properties modified on arrow1Display.PolarAxes
    arrow1Display.PolarAxes.Orientation = [0.0, 0.0, rotation]
    rotation += 22.5

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1496, 796)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.Update()

#--------------------------------------------
# uncomment the following to render all views
SaveScreenshot('arrows.png', renderView1)
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).