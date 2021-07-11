# Imported---------------------------------------------------------------------------
# ImportModules---------------------------------------
from pygame import *
import pygame
from random import *
from tkinter import *
from math import *
from sys import platform

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

# SimplyPaint.py | Sharjeel Mustafa
'''
This is a paint program. It includes pencil, marker, fountain pen,
paintbrush, spray paint, eraser, clear, shapes, stamps, force exit, and
customizable shapes and marking colours. The individuals features for this program
are its design with the drop-down menu. There is also tooltips.
The opacity, colour (RGB), and size sliders. 
The colour function displays the separate RGB colours with its 
numerical value. The width function shows the radius and an animation.
The shape tools have marker and a dragging function. The program can be
exited from a internal button. In addition, the above markers colours
can be changed. Furthermore, there the F2 key is programmed and remapped 
to the touch bar on the Macbook pro as and emergency exit. Also the 
program is designed to run smoothly on Mac and Windows. The Mac version
does not support load/save due to complications with opening windows.
'''

'''
The code below imports code that is required for save/load
'''
root = Tk()  # Starts the Tk Engine
root.wm_attributes("-topmost", 1)  # Keeps the load/save window on top
root.focus_force()  # Keeps the load/save window focused
root.withdraw()  # Hides the extra window

'''
The code below imports all the images needed for the program.
It also scales them accordingly. The images are organized by tool families
'''
# StaticImages--------------------------------------------------
Title = image.load("Images/StaticOption/Title.png")
Title = pygame.transform.scale(Title, (200, 50))
Title = pygame.transform.rotate(Title, 270)

ColourButton = image.load("Images/StaticOption/Colour.png")
ColourButton = pygame.transform.scale(ColourButton, (64, 64))

OpacityButton = image.load("Images/StaticOption/Opacity.png")
OpacityButton = pygame.transform.scale(OpacityButton, (64, 64))

WidthButton = image.load("Images/StaticOption/Width.png")
WidthButton = pygame.transform.scale(WidthButton, (64, 64))

SaveI = image.load("Images/StaticOption/Save.png")
SaveI = pygame.transform.scale(SaveI, (32, 32))

LoadI = image.load("Images/StaticOption/Load.png")
LoadI = pygame.transform.scale(LoadI, (32, 32))

# StaticOptionImages--------------------------------------------
RSlider = image.load("Images/StaticOption/ColourSliders/RSlider.png")
RSlider = pygame.transform.scale(RSlider, (20, 255))

GSlider = image.load("Images/StaticOption/ColourSliders/GSlider.png")
GSlider = pygame.transform.scale(GSlider, (20, 255))

BSlider = image.load("Images/StaticOption/ColourSliders/BSlider.png")
BSlider = pygame.transform.scale(BSlider, (20, 255))

CheckMark = image.load("Images/Shapes/CheckMark.png")
CheckMark = pygame.transform.scale(CheckMark, (16, 16))

# DrawingImages-------------------------------------------------
Drawing = image.load("Images/Drawing/Drawing.png")
Drawing = pygame.transform.scale(Drawing, (64, 64))

FountainPenI = image.load("Images/Drawing/FountainPen.png")
FountainPenI = pygame.transform.scale(FountainPenI, (64, 64))

MarkerI = image.load("Images/Drawing/Marker.png")
MarkerI = pygame.transform.scale(MarkerI, (64, 64))

PencilI = image.load("Images/Drawing/Pencil.png")
PencilI = pygame.transform.scale(PencilI, (64, 64))

# PaintingImages------------------------------------------------
Painting = image.load("Images/Painting/Painting.png")
Painting = pygame.transform.scale(Painting, (64, 64))

PaintBrushI = image.load("Images/Painting/PaintBrush.png")
PaintBrushI = pygame.transform.scale(PaintBrushI, (64, 64))

SprayPaintI = image.load("Images/Painting/SprayPaint.png")
SprayPaintI = pygame.transform.scale(SprayPaintI, (64, 64))

# ErasingImages-------------------------------------------------
Erasing = image.load("Images/Erasing/EraserFamily.png")
Erasing = pygame.transform.scale(Erasing, (64, 64))

EraserI = image.load("Images/Erasing/Eraser.png")
EraserI = pygame.transform.scale(EraserI, (64, 64))

ClearI = image.load("Images/Erasing/Clear.png")
ClearI = pygame.transform.scale(ClearI, (64, 64))

# ShapeImages---------------------------------------------------
Shapes = image.load("Images/Shapes/Shapes.png")
Shapes = pygame.transform.scale(Shapes, (64, 64))

CircleI = image.load("Images/Shapes/Circle.png")
CircleI = pygame.transform.scale(CircleI, (64, 64))

SquareI = image.load("Images/Shapes/Square.png")
SquareI = pygame.transform.scale(SquareI, (64, 64))

LineI = image.load("Images/Shapes/Line.png")
LineI = pygame.transform.scale(LineI, (64, 64))

EllipseI = image.load("Images/Shapes/Ellipse.png")
EllipseI = pygame.transform.scale(EllipseI, (64, 64))

# StampImages---------------------------------------------------
Stamps = image.load("Images/Stamps/Stamps.png")
Stamps = pygame.transform.scale(Stamps, (64, 64))

Stamp1 = image.load("Images/Stamps/Sun.png")
Stamp1I = pygame.transform.scale(Stamp1, (64, 64))

Stamp2 = image.load("Images/Stamps/Cloud.png")
Stamp2I = pygame.transform.scale(Stamp2, (64, 64))

Stamp3 = image.load("Images/Stamps/Rain.png")
Stamp3I = pygame.transform.scale(Stamp3, (64, 64))

Stamp4 = image.load("Images/Stamps/Mountain.png")
Stamp4I = pygame.transform.scale(Stamp4, (64, 64))

Stamp5 = image.load("Images/Stamps/Grass.png")
Stamp5I = pygame.transform.scale(Stamp5, (64, 64))

Stamp6 = image.load("Images/Stamps/Trees.png")
Stamp6I = pygame.transform.scale(Stamp6, (64, 64))

# SettingImages-------------------------------------------------
Settings = image.load("Images/Settings/Settings.png")
Settings = pygame.transform.scale(Settings, (64, 64))

ForceExitI = image.load("Images/Settings/ForceExit.png")
ForceExitI = pygame.transform.scale(ForceExitI, (64, 64))

font.init()
comicFont = font.SysFont("Century Gothic", 12)

# Variables-------------------------------------------------------------------------
'''
The Tooltips are stored by sentence in an array.
The specific sentences are called according to
what the tool is.
'''

ToolTips = [
    "Left click to draw.",
    "Left click to erase.",
    "Left click to set marker.",
    "Shift/Left click to draw shape.",
    "Keep holding Left click and move to drag.",
    "Left click to place stamp.",

    "The size and color are adjustable.",
    "The size and opacity are adjustable.",
    "The size, colour and opacity are adjustable.",
    "The size is adjustable.",

    "The canvas will be cleared (filled white).",
    "Left click to exit program.",
    "Left click to set current color as point 1 color.",
    "Left click to set current color as point 2 color.",
    "Click the checkbox on the right to toggle fill.",
]

'''
The code below determines which operating system the program runs on
and makes adjustments to keep the program running smoothly
'''

if platform in ["win32", "win64"]:
    FullScreen = False
    display.set_caption("Simply Paint")
    comicFont = font.SysFont("Century Gothic", 12)
else:
    FullScreen = True
    comicFont = font.SysFont("Century Gothic", 20)

OBSwitch = False  # OptionButton switch: Used to determine whether the option interface should be visible
InitialFrame = True  # This determines if the program is running for the first time.
ToolActive = True  # This determines if the mouse is touching the canvas

ShiftKey = False  # This is toggled by the press of the Shift-key

ShapeFill = False  # These two variables determine if the shape is filled or unfilled
FillToggle = 0

# The below are stored information on size and colour for the option button
OptionButton = Rect(10, 10, 80, 80)
OptionInterface = Rect(10, 10, 80, 630)
OptionColor = (0, 0, 255)

# The below store information on the RGB sliders and colour values
RedInput = Rect((1380, 825, 20, 10))
GreenInput = Rect((1400, 825, 20, 10))
BlueInput = Rect((1420, 825, 20, 10))
Color = (0, 0, 0)
Red = 0
Green = 0
Blue = 0

# The below store information (size and position) of Width and Opacity sliders
WidthInput = Rect((1385, 790, 50, 10))
OpacityInput = Rect((1385, 790, 50, 10))

# The below stores the information of what items the program will start with
StaticOption = "Colour"
CanvasOption = "Null"
ToolFamily = "Drawing"
Tool = "Pencil"

# The below stores the "theme" colour values
H1 = (255, 0, 0)  # Highlight color one (Inital Marker)
H2 = (0, 255, 0)  # Highlight color two (Secondary Marker)
BC = (100, 100, 100)  # Border Color
HC = (70, 70, 70)  # Highlighted Color
PC = (0, 0, 0)  # Pressed Color

Size = 20  # Width of drawing head
Alpha = 40  # Opacity

Mx, My = 0, 0  # Initial value of Mouse x,y

# The below stores information on the draw line tool
LinePos = 0  # Determines which part of the code line will progress to
LineP1 = (0, 0)  # Determines initial line point
LineP2 = (0, 0)  # Determines final line point

EllipsePos = 0 # Determines which part of the code ellipse will progress to
RectanglePos = 0 # Determines which part of the code rect will progress to

# The below determins wether to let the object drag with the mouse
StampDrag = False
LineDrag = False

# InitialSetup----------------------------------------------------------------------
'''
This section of the code sets up the canvas subsurface, visual elements,
and the display size depending on the operating system. Python runs faster full screen on mac.
Key are also initialized here and are given a variable.
The F2 key is remapped on the mac as a force quit.
'''
if FullScreen == True:
    screen = display.set_mode((0, 0), FULLSCREEN)
    screen.fill((200, 200, 200))
else:
    screen = display.set_mode((1440, 900))

screen.fill((100, 100, 100))
rect = pygame.Rect(10, 110, 1360, 780)
CanvasSurface = screen.subsurface(rect)
CanvasSurface.fill((255, 255, 255))

RunIntro = True
RunProgram = True
while RunProgram:
    for evt in event.get():
        if evt.type == QUIT:
            RunProgram = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F2]:
        RunProgram = False
    if keys[pygame.K_ESCAPE]:
        RunProgram = False
    if keys[pygame.K_LSHIFT]:
        ShiftKey = True

    # RefreshInformation------------------------------------------------------------
    '''
    This section refreshes information such as the mouse position
    '''
    InitialMx, InitialMy = Mx, My
    Mx, My = mouse.get_pos()
    Mb = mouse.get_pressed()
    # RefreshScreen -----------------------------------------------------------------
    '''
    This section refreshed the visual elements except the canvas
    '''
    screen.fill((100, 100, 100))
    ToolBar1 = draw.rect(screen, (220, 220, 220), (0, 0, 1440, 100))
    ToolBar2 = draw.rect(screen, (150, 150, 150), (1440, 0, -60, 900))
    Canvas = draw.rect(screen, (255, 255, 255), (10, 110, 1360, 780))
    draw.line(screen, (150, 150, 150), (805, 0), (805, 100), 8)

    draw.rect(screen, (100, 100, 100), (1375, 155, 500, 210), 4)
    screen.blit(Title, (1385, 160))
    '''
    The canvas is copied at the end of the program and is pasted once
    all the visual elements have refreshed. This starts working
    once the program has ran one loop.
    '''
    if InitialFrame == False:
        screen.blit(Frame, (10, 110))

    # StaticInterface---------------------------------------------------------------

    '''
    This section of the code is made modular since it is used many times.
    It creates a box that changed colour depending on if it is clicked on or
    if the mouse is resting on top.
    It than triggers its corresponding tool.
    '''
    Save = draw.rect(screen, (220, 220, 220), (1390, 10, 40, 40))
    draw.rect(screen, BC, (1390, 10, 40, 40), 4)
    screen.blit(SaveI, (1394, 14))
    if Save.collidepoint(Mx, My):
        draw.rect(screen, HC, (1390, 10, 40, 40), 4)
    if Save.collidepoint(Mx, My) and Mb[0] == 1:
        draw.rect(screen, PC, (1390, 10, 40, 40), 4)
        CanvasOption = "Save"

    Load = draw.rect(screen, (220, 220, 220), (1390, 60, 40, 40))
    draw.rect(screen, BC, (1390, 60, 40, 40), 4)
    screen.blit(LoadI, (1394, 64))
    if Load.collidepoint(Mx, My):
        draw.rect(screen, HC, (1390, 60, 40, 40), 4)
    if Load.collidepoint(Mx, My) and Mb[0] == 1:
        draw.rect(screen, PC, (1390, 60, 40, 40), 4)
        CanvasOption = "Load"

    # ----------------------------------------------------------

    # OpacityButton--------------------------
    '''
    The imported imaged from above are pasted into the button.
    '''
    screen.blit(OpacityButton, (828, 18))
    Opacity = draw.rect(screen, BC, (820, 10, 80, 80), 4)

    if Opacity.collidepoint(Mx, My):
        draw.rect(screen, HC, (820, 10, 80, 80), 4)
    if Opacity.collidepoint(Mx, My) and Mb[0] == 1:
        draw.rect(screen, PC, (820, 10, 80, 80), 4)
        StaticOption = "Opacity"

    # ColourButton--------------------------

    screen.blit(ColourButton, (918, 18))
    Colour = draw.rect(screen, BC, (910, 10, 80, 80), 4)

    if Colour.collidepoint(Mx, My):
        draw.rect(screen, HC, (910, 10, 80, 80), 4)
    if Colour.collidepoint(Mx, My) and Mb[0] == 1:
        draw.rect(screen, PC, (910, 10, 80, 80), 4)
        StaticOption = "Colour"

    # WidthButton--------------------------

    screen.blit(WidthButton, (1008, 18))
    Width = draw.rect(screen, BC, (1000, 10, 80, 80), 4)

    if Width.collidepoint(Mx, My):
        draw.rect(screen, HC, (1000, 10, 80, 80), 4)
    if Width.collidepoint(Mx, My) and Mb[0] == 1:
        draw.rect(screen, PC, (1000, 10, 80, 80), 4)
        StaticOption = "Width"

    Information = draw.rect(screen, BC, (1090, 10, 280, 80), 4)

    # CanvasOptions---------------------------------------------------------------------

    '''
    This checks to see if Load or Save is clicked, if not it will set itself as null.
    If Load/Save is clicked and the button is still pressed that it will activate the function.
    
    The load function opens a window and asks the user to enter the file name or click the file.
    png and bmp files are supported.
    
    The save function opens a window, asks for a name, and save it at the desired location
    as a bmp image.
    '''

    if CanvasOption == "Load" and Mb[0] == 1:
        FileName = askopenfilename(filetypes=[
            ("Picture files", "*.png;*.bmp")])
        LoadedImage = image.load(FileName)
        screen.blit(LoadedImage, (10, 110))

    elif CanvasOption == "Save" and Mb[0] == 1:
        FileName = asksaveasfilename()
        image.save(CanvasSurface, FileName + ".bmp")
    else:
        CanvasOption = "Null"

    # StaticItems-----------------------------------------------------------------------

    # Colour----------------------------------------------------
    if StaticOption == "Colour":

        '''
        The visual elements and slider posistions are imported and place on screen.
        '''

        RedSurface = draw.rect(screen, (0, 0, 0), (1380, 580, 20, 255))
        GreenSurface = draw.rect(screen, (0, 0, 0), (1400, 580, 20, 255))
        BlueSurface = draw.rect(screen, (0, 0, 0), (1420, 580, 20, 255))

        screen.blit(RSlider, (1380, 580))
        screen.blit(GSlider, (1400, 580))
        screen.blit(BSlider, (1420, 580))

        draw.rect(screen, (200, 200, 200), (1380, 580, 59, 255), 2)

        draw.rect(screen, (200, 200, 200), RedInput, 2)
        draw.rect(screen, (200, 200, 200), GreenInput, 2)
        draw.rect(screen, (200, 200, 200), BlueInput, 2)

        '''
        To determine the colour it used the position and size of the slider.
        If the mouse is touching the slider (which is about 255px) than using
        the difference in its top and mouse position will give a value for
        the colour. This code is modular so it is reused for the next sliders.
        '''
        # Red-------------------------------
        if RedSurface.collidepoint(Mx, My) and Mb[0] == 1:
            SliderR = True
        else:
            SliderR = False

        if SliderR == True and 580 < My < 835:
            RedInput = Rect((1380, My, 20, 10))
            Red = 255 - (My - 580)

        # Green-----------------------------
        if GreenSurface.collidepoint(Mx, My) and Mb[0] == 1:
            SliderG = True
        else:
            SliderG = False

        if SliderG == True and 580 < My < 835:
            GreenInput = Rect((1400, My, 20, 10))
            Green = 255 - (My - 580)

        # Blue------------------------------
        if BlueSurface.collidepoint(Mx, My) and Mb[0] == 1:
            SliderB = True
        else:
            SliderB = False

        if SliderB == True and 580 < My < 835:
            BlueInput = Rect((1420, My, 20, 10))
            Blue = 255 - (My - 580)

        # ColorIndicator--------------------
        '''
        This combines the above values and gives a colour output/square
        '''
        Color = (Red, Green, Blue)
        draw.rect(screen, Color, (1390, 850, 40, 40))
        draw.rect(screen, BC, (1390, 850, 40, 40), 4)

        # RedIndicator----------------------
        '''
        This uses the above colour value and make a output/square
        that shows the red level. The level is also converted into text
        and displayed as text. This code is reused for outputting
        values into strings
        '''
        draw.rect(screen, (Red, 0, 0), (1390, 400, 40, 40))
        draw.rect(screen, BC, (1390, 400, 40, 40), 4)
        RedVal = (Red / 255) * 100
        RedVal = round(RedVal)
        RedVal = str(RedVal)
        RedTxt = comicFont.render(RedVal + "%", True, (220, 220, 220))
        screen.blit(RedTxt, (1410 - RedTxt.get_width() / 2, 452 - RedTxt.get_height() / 2))

        # GreenIndicator--------------------
        draw.rect(screen, (0, Green, 0), (1390, 460, 40, 40))
        draw.rect(screen, BC, (1390, 460, 40, 40), 4)
        GreenVal = (Green / 255) * 100
        GreenVal = round(GreenVal)
        GreenVal = str(GreenVal)
        GreenTxt = comicFont.render(GreenVal + "%", True, (220, 220, 220))
        screen.blit(GreenTxt, (1410 - GreenTxt.get_width() / 2, 512 - GreenTxt.get_height() / 2))

        # BlueIndicator---------------------
        draw.rect(screen, (0, 0, Blue), (1390, 520, 40, 40))
        draw.rect(screen, BC, (1390, 520, 40, 40), 4)
        BlueVal = (Blue / 255) * 100
        BlueVal = round(BlueVal)
        BlueVal = str(BlueVal)
        BlueTxt = comicFont.render(BlueVal + "%", True, (220, 220, 220))
        screen.blit(BlueTxt, (1410 - BlueTxt.get_width() / 2, 572 - BlueTxt.get_height() / 2))

    # Opacity---------------------------------------------------
    if StaticOption == "Opacity":
        OpacitySlider = draw.rect(screen, (150, 150, 150), (1380, 590, 60, 250))
        draw.polygon(screen, Color, ((1385, 590), (1435, 590), (1410, 840)))
        draw.polygon(screen, BC, ((1385, 590), (1435, 590), (1410, 840)), 4)
        draw.rect(screen, (255, 255, 255), OpacityInput, 2)

        if OpacitySlider.collidepoint(Mx, My) and Mb[0] == 1:
            SliderO = True
        else:
            SliderO = False

        if SliderO == True and 590 < My < 840:
            OpacityInput = Rect((1385, My, 50, 10))
            Alpha = 250 - (My - 590)

        # OpacityIndicator------------------
        '''
        This code draws a square with the opacity level and then
        blits it ontop to give an output for the opacity.
        '''
        Opacity = Surface((80, 80), SRCALPHA)
        draw.rect(Opacity, (Red, Green, Blue, Alpha), (40, 40, -40, -40))
        screen.blit(Opacity, (1390, 850))
        draw.rect(screen, BC, (1390, 850, 40, 40), 4)

    # Width-----------------------------------------------------
    if StaticOption == "Width":
        WidthSlider = draw.rect(screen, (150, 150, 150), (1380, 500, 60, 300))
        draw.polygon(screen, Color, ((1385, 510), (1435, 510), (1410, 810)))
        draw.polygon(screen, BC, ((1385, 510), (1435, 510), (1410, 810)), 4)
        draw.rect(screen, (255, 255, 255), WidthInput, 2)

        if WidthSlider.collidepoint(Mx, My) and Mb[0] == 1:
            SliderT = True
        else:
            SliderT = False

        if SliderT == True and 510 < My < 810:
            WidthInput = Rect((1385, My, 50, 10))
            Size = 300 - (My - 500)

        # WidthIndicator--------------------
        '''
        This code is similarly to the specific colour output code.
        However it also has an animation showing  the actual size until
        it hits size 30. Than it shows a numarical value.
        '''
        if Size >= 30:
            WVal = str(Size)
            if Color == (0, 0, 0):
                draw.circle(screen, BC, (1410, 860), 34)
                draw.circle(screen, Color, (1410, 860), 30)
                WTxt = comicFont.render(WVal + "px", True, (200, 200, 200))
                screen.blit(WTxt, (1410 - WTxt.get_width() / 2, 860 - WTxt.get_height() / 2))
            else:
                draw.circle(screen, BC, (1410, 860), 34)
                draw.circle(screen, Color, (1410, 860), 30)
                WTxt = comicFont.render(WVal + "px", True, (0, 0, 0))
                screen.blit(WTxt, (1410 - WTxt.get_width() / 2, 860 - WTxt.get_height() / 2))
        else:
            draw.circle(screen, BC, (1410, 860), Size + 4)
            draw.circle(screen, Color, (1410, 860), Size)

    # ToolFamilies------------------------------------------------------------------
    '''
    The code in this segment is the exact same as the static option code above.
    It is arranged by the Tool family.
    
    * The code is arranged so that all the static option function and code is done in 
    the upper half. The Tools selection and functions are done in the middle. 
    The option interface is done at the end of the program.
    
    This is because before the option interface drops down onto the canvas
    it needs to save the canvas and than paste it once the visual elements
    have been refreshed. So all the changes that had to be made to the canvas
    had to be done before the canvas was saved. So all the tools and static options
    are arranged this way for this reason.
    '''
    # DrawingFamily-----------------------------------------
    if ToolFamily == "Drawing":

        screen.blit(Drawing, (18, 18))

        screen.blit(PencilI, (108, 18))
        Pencil = draw.rect(screen, BC, (100, 10, 80, 80), 4)
        if Pencil.collidepoint(Mx, My):
            draw.rect(screen, HC, (100, 10, 80, 80), 4)
        if Pencil.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (100, 10, 80, 80), 4)
            Tool = "Pencil"

        screen.blit(MarkerI, (198, 18))
        Marker = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if Marker.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if Marker.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            Tool = "Marker"

        screen.blit(FountainPenI, (288, 18))
        FountainPen = draw.rect(screen, BC, (280, 10, 80, 80), 4)
        if FountainPen.collidepoint(Mx, My):
            draw.rect(screen, HC, (280, 10, 80, 80), 4)
        if FountainPen.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (280, 10, 80, 80), 4)
            Tool = "FountainPen"

    # PaintFamily-------------------------------------------
    elif ToolFamily == "Paint":

        screen.blit(Painting, (18, 18))

        screen.blit(PaintBrushI, (108, 18))
        PaintBrush = draw.rect(screen, BC, (100, 10, 80, 80), 4)
        if PaintBrush.collidepoint(Mx, My):
            draw.rect(screen, HC, (100, 10, 80, 80), 4)
        if PaintBrush.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (100, 10, 80, 80), 4)
            Tool = "PaintBrush"

        screen.blit(SprayPaintI, (198, 18))
        SprayPaint = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if SprayPaint.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if SprayPaint.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            Tool = "SprayPaint"

    # ShapeFamily-------------------------------------------
    elif ToolFamily == "Shapes":
        screen.blit(Shapes, (18, 18))

        screen.blit(SquareI, (108, 18))
        SquareShape = draw.rect(screen, BC, (100, 10, 80, 80), 4)
        if SquareShape.collidepoint(Mx, My):
            draw.rect(screen, HC, (100, 10, 80, 80), 4)
        if SquareShape.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (100, 10, 80, 80), 4)
            Tool = "Square"

        screen.blit(CircleI, (198, 18))
        CircleShape = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if CircleShape.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if CircleShape.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            Tool = "Circle"

        screen.blit(LineI, (288, 18))
        LineShape = draw.rect(screen, BC, (280, 10, 80, 80), 4)
        if LineShape.collidepoint(Mx, My):
            draw.rect(screen, HC, (280, 10, 80, 80), 4)
        if LineShape.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (280, 10, 80, 80), 4)
            Tool = "Line"

        screen.blit(EllipseI, (378, 18))
        EllipseShape = draw.rect(screen, BC, (370, 10, 80, 80), 4)
        if EllipseShape.collidepoint(Mx, My):
            draw.rect(screen, HC, (370, 10, 80, 80), 2)
        if EllipseShape.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (370, 10, 80, 80), 2)
            Tool = "Ellipse"

        if Tool != "Line":
            FillShape = draw.rect(screen, BC, (1400, 110, 20, 20), 4)
            if FillShape.collidepoint(Mx, My):
                draw.rect(screen, HC, (1400, 110, 20, 20), 4)
            if FillShape.collidepoint(Mx, My) and Mb[0] == 1:
                draw.rect(screen, PC, (1400, 110, 20, 20), 4)
                FillToggle = FillToggle + 1
                time.delay(200)

            if FillToggle == 1:
                screen.blit(CheckMark, (1402, 112))
                ShapeFill = True
            elif FillToggle == 2:
                FillToggle = 0
                ShapeFill = False

    # EraserFamily------------------------------------------
    elif ToolFamily == "Eraser":
        screen.blit(Erasing, (18, 18))

        screen.blit(EraserI, (108, 18))
        Eraser = draw.rect(screen, (100, 100, 100), (100, 10, 80, 80), 4)
        if Eraser.collidepoint(Mx, My):
            draw.rect(screen, (0, 0, 0), (100, 10, 80, 80), 4)
        if Eraser.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, (0, 0, 0), (100, 10, 80, 80), 4)
            Tool = "Eraser"

        screen.blit(ClearI, (198, 18))
        Clear = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if Clear.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if Clear.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            Tool = "Clear"

    # StampFamily-------------------------------------------
    elif ToolFamily == "Stamps":
        screen.blit(Stamps, (18, 18))

        screen.blit(Stamp1I, (108, 18))
        S1 = draw.rect(screen, BC, (100, 10, 80, 80), 4)
        if S1.collidepoint(Mx, My):
            draw.rect(screen, HC, (100, 10, 80, 80), 4)
        if S1.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (100, 10, 80, 80), 4)
            Tool = "Stamp1"

        screen.blit(Stamp2I, (198, 18))
        S2 = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if S2.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if S2.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            Tool = "Stamp2"

        screen.blit(Stamp3I, (288, 18))
        S3 = draw.rect(screen, BC, (280, 10, 80, 80), 4)
        if S3.collidepoint(Mx, My):
            draw.rect(screen, HC, (280, 10, 80, 80), 4)
        if S3.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (280, 10, 80, 80), 4)
            Tool = "Stamp3"

        screen.blit(Stamp4I, (378, 18))
        S4 = draw.rect(screen, BC, (370, 10, 80, 80), 4)
        if S4.collidepoint(Mx, My):
            draw.rect(screen, HC, (370, 10, 80, 80), 4)
        if S4.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (370, 10, 80, 80), 4)
            Tool = "Stamp4"

        screen.blit(Stamp5I, (468, 18))
        S5 = draw.rect(screen, BC, (460, 10, 80, 80), 4)
        if S5.collidepoint(Mx, My):
            draw.rect(screen, HC, (460, 10, 80, 80), 4)
        if S5.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (460, 10, 80, 80), 4)
            Tool = "Stamp5"

        screen.blit(Stamp6I, (558, 18))
        S6 = draw.rect(screen, BC, (550, 10, 80, 80), 4)
        if S6.collidepoint(Mx, My):
            draw.rect(screen, HC, (550, 10, 80, 80), 4)
        if S6.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (550, 10, 80, 80), 4)
            Tool = "Stamp6"

    # Settings----------------------------------------------
    elif ToolFamily == "Settings":

        screen.blit(Settings, (18, 18))

        screen.blit(ForceExitI, (108, 18))
        ForceExit = draw.rect(screen, BC, (100, 10, 80, 80), 4)
        if ForceExit.collidepoint(Mx, My):
            draw.rect(screen, HC, (100, 10, 80, 80), 4)
        if ForceExit.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (100, 10, 80, 80), 4)
            Tool = "ForceExit"

        draw.rect(screen, H1, (190, 10, 80, 80))
        ColorPreference1 = draw.rect(screen, BC, (190, 10, 80, 80), 4)
        if ColorPreference1.collidepoint(Mx, My):
            draw.rect(screen, HC, (190, 10, 80, 80), 4)
        if ColorPreference1.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (190, 10, 80, 80), 4)
            H1 = Color

        draw.rect(screen, H2, (280, 10, 80, 80))
        ColorPreference2 = draw.rect(screen, BC, (280, 10, 80, 80), 4)
        if ColorPreference2.collidepoint(Mx, My):
            draw.rect(screen, HC, (280, 10, 80, 80), 4)
        if ColorPreference2.collidepoint(Mx, My) and Mb[0] == 1:
            draw.rect(screen, PC, (280, 10, 80, 80), 4)
            H2 = Color

    # ToolTips----------------------------------------------------------------------
    '''
    This section of the code displays tool tips. It first checks for the tool.
    Than it uses the corresponding sentences from the array. Those sentences are
    displayed onscreen.
    '''
    # DrawingFamily-ToolTips--------------------------
    if Tool == "Pencil":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[6], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    elif Tool == "Marker":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[8], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    elif Tool == "FountainPen":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[6], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    # PaintingFamily-ToolTips-------------------------
    elif Tool == "PaintBrush":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[8], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    elif Tool == "SprayPaint":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[6], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    # ErasingFamily-ToolTips--------------------------
    elif Tool == "Eraser":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[7], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    elif Tool == "Clear":
        ITxt = comicFont.render(ToolTips[10], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))

    # ShapesFamily-ToolTips----------------------------
    elif Tool == "Square":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[8], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))
        ITxt = comicFont.render(ToolTips[4], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 34))
        ITxt = comicFont.render(ToolTips[14], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 44))

    elif Tool == "Circle":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[8], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))
        ITxt = comicFont.render(ToolTips[4], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 34))
        ITxt = comicFont.render(ToolTips[14], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 44))

    elif Tool == "Line":
        ITxt = comicFont.render(ToolTips[2], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[6], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))
        ITxt = comicFont.render(ToolTips[3], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 34))

    elif Tool == "Ellipse":
        ITxt = comicFont.render(ToolTips[2], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[3], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))
        ITxt = comicFont.render(ToolTips[6], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 34))
        ITxt = comicFont.render(ToolTips[14], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 44))

    # StampsFamily-ToolTips---------------------------
    elif Tool == "Stamp1" or "Stamp2" or "Stamp3" or "Stamp4""Stamp5" or "Stamp6":
        #  All stamps behave the same
        ITxt = comicFont.render(ToolTips[5], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[4], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))
        ITxt = comicFont.render(ToolTips[9], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 34))

    # SettingsFamily-ToolTips-------------------------
    elif Tool == "ForceExit":
        ITxt = comicFont.render(ToolTips[0], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 14))
        ITxt = comicFont.render(ToolTips[3], True, BC)
        screen.blit(ITxt, (1230 - ITxt.get_width() / 2, 24))

    # ToolActive--------------------------------------------------------------------
    '''
    This checks too see if the mouse is touching the canvas. If it is than tools
    are active/can draw.
    '''
    if Canvas.collidepoint(Mx, My):
        ToolActive = True
    else:
        ToolActive = False

    # Tools-------------------------------------------------------------------------
    if ToolActive == True and OBSwitch == False:
        '''
        This makes sure that tools are active and the option interface is not active.
        '''
        # Pencil------------------------------------------------
        if Tool == "Pencil" and Mb[0] == 1:
            '''
            The below code looks at all the possible points between the gap made
            by the mouse movement. The possible points in the gap are than used to generate
            the according tool head (the size,color,and/or opacity) in all those points.
            It makes sure to take the hypotenuse so it takes the shortest and "smoothest"
            path. This code is used in multiple tools.
            '''
            DistanceX = Mx - InitialMx
            DistanceY = My - InitialMy
            Distance = sqrt((DistanceX ** 2) + (DistanceY ** 2))

            for i in range(round(Distance)):
                Xvalue = (InitialMx + round(((i / Distance) * DistanceX))) - round(Size / 2)
                Yvalue = (InitialMy + round(((i / Distance) * DistanceY))) - round(Size / 2)

                draw.rect(screen, Color, (Xvalue, Yvalue, Size, Size))

        # Marker------------------------------------------------
        elif Tool == "Marker" and Mb[0] == 1:

            DistanceX = Mx - InitialMx
            DistanceY = My - InitialMy
            Distance = sqrt((DistanceX ** 2) + (DistanceY ** 2))

            for i in range(round(Distance)):
                Xvalue = InitialMx + round(((i / Distance) * DistanceX))
                Yvalue = InitialMy + round(((i / Distance) * DistanceY))
                '''
                This code for opacity is used multiple times. It makes a surface and generates
                the tool head (with color, opacity, and size values). This is than blited onto the
                screen. 
      
                *  The tool head position is altered depending on its size so it appears at the
                middle of the mouse.
                '''
                MarkerHead = Surface((100, 100), SRCALPHA)
                draw.rect(MarkerHead, (Red, Green, Blue, Alpha), (Size, Size, -Size, -Size))

                if Mx != InitialMx or My != InitialMy:
                    screen.blit(MarkerHead, (Xvalue - round(Size / 4), Yvalue - round(Size / 4)))

        # FountainPen-------------------------------------------
        elif Tool == "FountainPen" and Mb[0] == 1:

            if Mb[0] == 1:
                '''
                This code generates multiple "thin" lines which are than stacked on
                each other depending on the size. Ex Size = 6 than 6 lines will be stacked on top
                of each other.
                '''
                PenSize = Size
                PenStroke = 0
                while PenSize != 0:
                    PenSize = PenSize - 1
                    PenStroke = PenStroke + 1
                    draw.aaline(screen, Color, (InitialMx + PenStroke, InitialMy + PenStroke),
                                (Mx + PenStroke, My + PenStroke))

        # PaintBrush--------------------------------------------
        elif Tool == "PaintBrush" and Mb[0] == 1:

            DistanceX = Mx - InitialMx
            DistanceY = My - InitialMy
            Distance = sqrt((DistanceX ** 2) + (DistanceY ** 2))

            for i in range(round(Distance)):
                Xvalue = InitialMx + round(((i / Distance) * DistanceX))
                Yvalue = InitialMy + round(((i / Distance) * DistanceY))

                '''
                This uses the size and creates multiple circles that are descending in radius.
                This creates an effect that the center has a lower opacity than the outer edge.
                The opacity stays the same but the fact that multiple circles that are getting
                smaller are stacked on each other it makes tool head darker towards the center.
                '''
                PaintRadius = Size / 10
                PaintRadius = round(PaintRadius)
                PaintRadius = PaintRadius * 10
                while PaintRadius != 0:
                    PaintRadius = PaintRadius - 5
                    PaintOpacity = Surface((PaintRadius * 2, PaintRadius * 2), SRCALPHA)
                    draw.circle(PaintOpacity, (Red, Green, Blue, Alpha), (PaintRadius, PaintRadius), PaintRadius)

                    if Mx != InitialMx or My != InitialMy:
                        screen.blit(PaintOpacity, (Xvalue - PaintRadius, Yvalue - PaintRadius))

        # SprayPaint--------------------------------------------
        elif Tool == "SprayPaint" and Mb[0] == 1:
            '''
            This generates many small circles in a larger circle.
            Because it checks to see if the X,Y is larger than the size.
            If it is it stops the loop. This gives it a "circle" appearance.
            '''
            SprayPaintX = randint(-Size, Size)
            SprayPaintY = randint(-Size, Size)

            if (SprayPaintX ** 2) + (SprayPaintY ** 2) <= Size ** 2:
                draw.circle(screen, Color, (Mx + SprayPaintX, My + SprayPaintY), 1)

        # Eraser------------------------------------------------
        elif Tool == "Eraser" and Mb[0] == 1:

            '''
            This is the same as the marker tool but the colour is fixed to white.
            '''
            DistanceX = Mx - InitialMx
            DistanceY = My - InitialMy
            Distance = sqrt((DistanceX ** 2) + (DistanceY ** 2))

            for i in range(round(Distance)):
                Xvalue = InitialMx + round(((i / Distance) * DistanceX))
                Yvalue = InitialMy + round(((i / Distance) * DistanceY))

                EraserT = Surface((Size * 2, Size * 2), SRCALPHA)
                draw.rect(EraserT, (255, 255, 255, Alpha), (Size, Size, -Size, -Size))

                if Mx != InitialMx or My != InitialMy:
                    screen.blit(EraserT, (Xvalue - round(Size / 2), Yvalue - round(Size / 2)))

        # Clear-------------------------------------------------
        elif Tool == "Clear":
            #  This fills the canvas white
            CanvasSurface.fill((255, 255, 255))

        # ForceExit---------------------------------------------
        elif Tool == "ForceExit":
            RunProgram = False

        # CircleTool--------------------------------------------
        elif Tool == "Circle":
            '''
            This is very similar to the marker tool but it draws circles instead.
            It will adjust the radius to either fill the circle or not.
            It also keeps Refreshing the canvas while the circle is clicked.
            So it lets the user drag.
            
            * All dragging code follows a similar code structure. That the shape/object
            while clicked is being refreshed at the mouse position. The background keeps
            refreshing giving a dragging effect.
            '''
            if Mb[0] == 1:
                if ShapeFill == True:
                    CircleT = Surface((Size * 2, Size * 2), SRCALPHA)
                    draw.circle(CircleT, (Red, Green, Blue, Alpha), (Size, Size), Size)
                    screen.blit(PreCircle, (10, 110))
                    screen.blit(CircleT, (Mx - Size, My - Size))

                else:
                    CircleT = Surface((Size * 2, Size * 2), SRCALPHA)
                    draw.circle(CircleT, (Red, Green, Blue, Alpha), (Size, Size), Size, 1)
                    screen.blit(PreCircle, (10, 110))
                    screen.blit(CircleT, (Mx - Size, My - Size))
            else:
                PreCircle = CanvasSurface.copy()

        # LineTool----------------------------------------------
        elif Tool == "Line":

            '''
            This function sets down two points and draws a line between them.
            The points are triggered by the shift key. So it gives the user
            enough time to set the points at 2 different locations.It would than draw a line
            between the 2 points.
            '''

            if ShiftKey == True:
                LinePos = LinePos + 1
                if LinePos == 1:
                    LineP1 = (Mx, My)
                    P1X = Mx  # Point 1 X value
                    P1Y = My  # Point 1 Y value

                    LineSave = CanvasSurface.copy()
                    draw.circle(screen, (255, 0, 0), (Mx, My), 4)
                    ShiftKey = False
                    time.delay(200)  # Adds delay so that the user has better control
                elif LinePos == 2:
                    LineP2 = (Mx, My)
                    P2X = Mx  # Point 2 X value
                    P2Y = My  # Point 2 Y value

                    draw.circle(screen, (0, 255, 0), (Mx, My), 4)
                    ShiftKey = False
                    time.delay(200)
                else:
                    screen.blit(LineSave, (10, 110))
                    draw.line(screen, Color, LineP1, LineP2, Size)
                    LineP1 = (0, 0)
                    LineP2 = (0, 0)

                    LinePos = 0
                    time.delay(200)
                    ShiftKey = False

            if Mb[0] == 1 and LineP1 != (0, 0) and LineP2 != (0, 0):
                screen.blit(LineSave, (10, 110))
                draw.line(screen, Color, LineP1, LineP2, Size)
                Object = draw.line(screen, Color, LineP1, LineP2, Size)
                LineDrag = True
                LineP1 = (0, 0)
                LineP2 = (0, 0)
                LinePos = 0
                time.delay(200)
                ShiftKey = False

            # This uses the same dragging function as stated above
            if LineDrag == True:
                if Mb[0] == 1:
                    YDistance = P2Y - P1Y
                    XDistance = P2X - P1X
                    screen.blit(LineSave, (10, 110))
                    draw.line(screen, Color, (Mx, My), (Mx + XDistance, My + YDistance), Size)

        # SquareTool--------------------------------------------
        elif Tool == "Square":

            '''
            This function uses the  same principle of the line tool. It stores 2 points and than creates a
            rectangle using the two points. A very similar setup to the line tool.
            '''
            # RectangleTool---------------------
            if ShiftKey == True:
                RectanglePos = RectanglePos + 1

                if RectanglePos == 1:
                    RectangleP1x = Mx
                    RectangleP1y = My
                    RectangleSave = CanvasSurface.copy()
                    draw.line(screen, H1, (Mx, My), (Mx + 10, My))
                    draw.line(screen, H1, (Mx, My), (Mx, My + 10))
                    ShiftKey = False
                    time.delay(200)

                elif RectanglePos == 2:
                    RectangleP2x = Mx
                    RectangleP2y = My
                    draw.line(screen, H2, (Mx, My), (Mx - 10, My))
                    draw.line(screen, H2, (Mx, My), (Mx, My - 10))
                    ShiftKey = False
                    time.delay(200)

                else:
                    RectangleX = abs(RectangleP2x - RectangleP1x)
                    RectangleY = abs(RectangleP2y - RectangleP1y)
                    screen.blit(RectangleSave, (10, 110))

                    if ShapeFill == True:
                        draw.rect(screen, Color, (RectangleP1x, RectangleP1y, RectangleX, RectangleY))

                    else:
                        draw.rect(screen, Color, (RectangleP1x, RectangleP1y, RectangleX, RectangleY), Size)

                    RectanglePos = 0
                    time.delay(200)
                    ShiftKey = False

            if Mb[0] == 1 and RectanglePos == 2:
                RectangleX = abs(RectangleP2x - RectangleP1x)
                RectangleY = abs(RectangleP2y - RectangleP1y)
                screen.blit(RectangleSave, (10, 110))

                if ShapeFill == True:
                    draw.rect(screen, Color, (RectangleP1x, RectangleP1y, RectangleX, RectangleY))
                else:
                    draw.rect(screen, Color, (RectangleP1x, RectangleP1y, RectangleX, RectangleY), Size)

                RectanglePos = 0
                time.delay(200)
                ShiftKey = False

            # SquareTool-------------------------
                '''
                This function is the same as the circle tool except it is making a square.
                '''
            elif Mb[0] == 1:
                if ShapeFill == True:
                    SquareT = Surface((Size * 2, Size * 2), SRCALPHA)
                    draw.rect(SquareT, (Red, Green, Blue, Alpha), (Size, Size, -Size, -Size))
                    screen.blit(PreSquare, (10, 110))
                    screen.blit(SquareT, (Mx - Size, My - Size))
                else:
                    SquareT = Surface((Size * 2, Size * 2), SRCALPHA)
                    draw.rect(SquareT, (Red, Green, Blue, Alpha), (Size + 1, Size + 1, -Size, -Size), 1)
                    screen.blit(PreSquare, (10, 110))
                    screen.blit(SquareT, (Mx - round(Size / 2), My - round(Size / 2)))
            else:
                PreSquare = CanvasSurface.copy()

        # EllipseTool-------------------------------------------
        elif Tool == "Ellipse":

            '''
            This function behaves same as the rectangle and line tool. It uses the ellipse
            command to create ovals/ellipses.
            '''
            if ShiftKey == True:
                EllipsePos = EllipsePos + 1

                if EllipsePos == 1:
                    EllipseP1x = Mx
                    EllipseP1y = My
                    EllipseSave = CanvasSurface.copy()
                    draw.line(screen, H1, (Mx, My), (Mx + 10, My))
                    draw.line(screen, H1, (Mx, My), (Mx, My + 10))
                    ShiftKey = False
                    time.delay(200)

                elif EllipsePos == 2:
                    EllipseP2x = Mx
                    EllipseP2y = My
                    draw.line(screen, H2, (Mx, My), (Mx - 10, My))
                    draw.line(screen, H2, (Mx, My), (Mx, My - 10))
                    ShiftKey = False
                    time.delay(200)

                else:
                    EllipseX = abs(EllipseP2x - EllipseP1x)
                    EllipseY = abs(EllipseP2y - EllipseP1y)
                    screen.blit(EllipseSave, (10, 110))

                    if ShapeFill == True:
                        draw.ellipse(screen, Color, (EllipseP1x, EllipseP1y, EllipseX, EllipseY))
                    else:
                        draw.ellipse(screen, Color, (EllipseP1x, EllipseP1y, EllipseX, EllipseY), 4)
                    EllipsePos = 0
                    time.delay(200)
                    ShiftKey = False

            if Mb[0] == 1 and EllipsePos == 2:
                EllipseX = abs(EllipseP2x - EllipseP1x)
                EllipseY = abs(EllipseP2y - EllipseP1y)
                screen.blit(EllipseSave, (10, 110))

                if ShapeFill == True:
                    draw.ellipse(screen, Color, (EllipseP1x, EllipseP1y, EllipseX, EllipseY))
                else:
                    draw.ellipse(screen, Color, (EllipseP1x, EllipseP1y, EllipseX, EllipseY), 4)
                EllipsePos = 0
                time.delay(200)
                ShiftKey = False
        # StampTool---------------------------------------------

        '''
        This tool scales the stamp to the size value. It also uses the dragging effect.
        It than blits it onto the canvas.
        '''
        if Mb[0] == 1:
            if Tool == "Stamp1":
                Stamp1T = pygame.transform.smoothscale(Stamp1, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp1T, (Mx - round(Size / 2), My - round(Size / 2)))

            elif Tool == "Stamp2":
                Stamp2T = pygame.transform.smoothscale(Stamp2, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp2T, (Mx - round(Size / 2), My - round(Size / 2)))

            elif Tool == "Stamp3":
                Stamp3T = pygame.transform.smoothscale(Stamp3, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp3T, (Mx - round(Size / 2), My - round(Size / 2)))

            elif Tool == "Stamp4":
                Stamp4T = pygame.transform.smoothscale(Stamp4, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp4T, (Mx - round(Size / 2), My - round(Size / 2)))

            elif Tool == "Stamp5":
                Stamp5T = pygame.transform.smoothscale(Stamp5, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp5T, (Mx - round(Size / 2), My - round(Size / 2)))

            elif Tool == "Stamp6":
                Stamp6T = pygame.transform.smoothscale(Stamp6, (Size, Size))
                screen.blit(PreStamp, (10, 110))
                screen.blit(Stamp6T, (Mx - round(Size / 2), My - round(Size / 2)))
        else:
            PreStamp = CanvasSurface.copy()

    # OptionInterface---------------------------------------------------------------
    # SaveCanvas------------------------------------------------

    # SaveCanvasForRefresh------------------
    InitialFrame = False
    Frame = CanvasSurface.copy()
    #  This function is explained at the start.

    # OptionButton----------------------------------------------
    draw.rect(screen, BC, OptionButton, 4)
    if OptionButton.collidepoint(Mx, My):
        draw.rect(screen, HC, OptionButton, 4)

    if OptionButton.collidepoint(Mx, My) and Mb[0] == 1:
        OBSwitch = True
    '''
    This uses the same button commands as the above functions.
    However if OBSwitch is triggered. It will deactivate Tools
    and generate a drop down menu. This menu has buttons in it.
    Once a button has been selected and/or the mouse is away from
    the drop down, it would  update the settings/values. Than the
    entire screen refreshes so the interface would be removed.
    '''
    # GenerateOptionInterface-----------------------------------
    if OptionInterface.collidepoint(Mx, My) and OBSwitch == True:
        draw.rect(screen, (220, 220, 220), OptionInterface)
        draw.rect(screen, PC, OptionButton, 4)

        if ToolFamily == "Drawing":
            screen.blit(Drawing, (18, 18))
        elif ToolFamily == "Paint":
            screen.blit(Painting, (18, 18))
        elif ToolFamily == "Erasing":
            screen.blit(Erasing, (18, 18))
        elif ToolFamily == "Shapes":
            screen.blit(Shapes, (18, 18))
        elif ToolFamily == "Stamps":
            screen.blit(Stamps, (18, 18))
        else:
            screen.blit(Settings, (18, 18))

        # Option1---------------------------
        B1 = draw.rect(screen, (220, 220, 220), (10, 100, 80, 80))
        screen.blit(Drawing, (18, 108))

        if B1.collidepoint(Mx, My):
            B1 = draw.rect(screen, PC, (10, 100, 80, 80), 4)
        if B1.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Drawing"
        # Option2---------------------------
        B2 = draw.rect(screen, (220, 220, 220), (10, 190, 80, 80))
        screen.blit(Painting, (18, 198))

        if B2.collidepoint(Mx, My):
            draw.rect(screen, PC, (10, 190, 80, 80), 4)
        if B2.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Paint"
        # Option3---------------------------
        B3 = draw.rect(screen, (220, 220, 220), (10, 280, 80, 80))
        screen.blit(Erasing, (18, 288))

        if B3.collidepoint(Mx, My):
            draw.rect(screen, PC, (10, 280, 80, 80), 4)
        if B3.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Eraser"
        # Option4---------------------------
        B4 = draw.rect(screen, (220, 220, 220), (10, 370, 80, 80))
        screen.blit(Shapes, (18, 378))

        if B4.collidepoint(Mx, My):
            draw.rect(screen, PC, (10, 370, 80, 80), 4)
        if B4.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Shapes"
        # Option5---------------------------
        B5 = draw.rect(screen, (220, 220, 220), (10, 460, 80, 80))
        screen.blit(Stamps, (18, 468))

        if B5.collidepoint(Mx, My):
            draw.rect(screen, PC, (10, 460, 80, 80), 4)
        if B5.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Stamps"
        # Option6---------------------------
        B6 = draw.rect(screen, (220, 220, 220), (10, 550, 80, 80))
        screen.blit(Settings, (18, 558))

        if B6.collidepoint(Mx, My):
            draw.rect(screen, PC, (10, 550, 80, 80), 4)
        if B6.collidepoint(Mx, My) and Mb[0] == 1:
            OBSwitch = False
            time.delay(100)
            ToolFamily = "Settings"

        draw.rect(screen, PC, OptionInterface, 4)
    else:
        OBSwitch = False
        # If the option button is not triggered it will keep option interface off.

    # End---------------------------------------------------------------------------

    '''
    The code below just ends the program appropriately.
    '''
    display.flip()
font.quit()
del comicFont
quit()
