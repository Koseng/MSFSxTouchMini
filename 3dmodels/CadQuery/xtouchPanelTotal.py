import cadquery as cq

# Number of generated columns
xCount = 8

topTextSize = 6
topTexts = ["BARO", "MODE", "RANGE", "SPEED","HDG", "ALT", "VS", "COM"]  # Encoder Texts

# There needs to be a non empty text in the last shown colum.
# So in column 4 or column 8 needs to be some text, depending on xCount
# Otherwise there is no rendering 
textSizes = [5,6,6]
texts = [["STD", "", "", "", "", "", "", ""],          # Below Encoder Texts
         ["FD", "", "PBRK", "AICE","NAV", "", "FLC", "FLDEC"],          # Button Row 1
         ["AP1", "AP2", "LS", "APPR","YD", "", "GEAR", "FLINC"]]   # Button Row 2

textHeight = 0.6
font = "Arial" #"Courier", "Arial"

yCount = 2
cRadius = 13.25
bLength = 13
bWidth = 10.5
xSpacing = 18.3
ySpacing = 10
xPadding = 9
yPadding = 10
xButtonArea = xCount*bLength + (xCount-1)*xSpacing
yButtonArea = yCount*bWidth + (yCount-1)*ySpacing
totalLength = xButtonArea + 2*xPadding
totalWidth = yButtonArea + 3*yPadding + 2*cRadius
height = 0.6

# Create basic box
r = cq.Workplane("XY").box(totalLength, totalWidth, height).edges("|Z").fillet(2)

xDist = xSpacing + bLength 
yDist = ySpacing + bWidth

# Encoder circles
yCircles = totalWidth/2 - yPadding - cRadius
r = r.center(0, yCircles)
# Create point table 4x1 and cut circles
r = r.rarray(xDist,yDist,xCount,1).circle(cRadius).cutThruAll()

# Create Top Texts 
yTopTexts = cRadius+4.5
r = r.faces(">Z[1]").workplane().center(-(xButtonArea-bLength)/2, yTopTexts)
#r = r.text("HEIKO", topTextSize, textHeight, cut=False, combine=True, font=font)
for col in range(xCount):
    if col > 0:
        r = r.center(xSpacing+bLength,0)
    if topTexts[col]:
        r = r.text(topTexts[col], topTextSize, textHeight, cut=False, combine=True, font=font)

# Button rectangles
yButtonCenter = totalWidth/2 - yPadding - bWidth - ySpacing/2
r = r.center(-(xButtonArea-bLength)/2, -yCircles-yTopTexts-yButtonCenter)
# Create point table 4x2 and cut rectangles
r = r.rarray(xDist,yDist,xCount,yCount).rect(bLength, bWidth).cutThruAll()

# Create texts
r = r.faces(">Z[1]").workplane().center(-(xButtonArea-bLength)/2, yButtonArea/2+(12-max(textSizes)))
for row in range(yCount+1): 
    for col in range(xCount): 
        if col > 0:
            r = r.center(xSpacing+bLength,0)
        if texts[row][col]:
            r = r.text(texts[row][col], textSizes[row], textHeight, cut=False, combine=True, font=font)
    # Move back xOffset and move yOffset
    if row < yCount:
        r = r.center(-xButtonArea+bLength, -bWidth-yPadding)
    
# Render the solid
show_object(r)
# Export
cq.exporters.export(r,'xtouchTotal.stl')
#cq.exporters.export(r, 'xtouch.svg')