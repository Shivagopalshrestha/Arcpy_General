# NOT WORKING - PROBLEM SPECIFICALLY WITH SQL STATEMENT AND RASTER FORMAT... COULDN'T FORMULATE VALID SQL STATEMENT IN DESKTOP VERION EITHER... RESEARCH LATER


# Script written for Raster Calculator to create a new raster from an existing raster by filtering out ranges of desired values.

# Import System Modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Environment Settings
env.workspace = "P:/Studies/137708_COPitkin_ErosionHazard/Working/GIS/PitkinData.gdb"

# Set local variables
inRaster = "REM_IDW_AverageFINAL_HeightAboveWS"
inSQLclause = "-4 < VALUE < 10"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractByAttributes
attExtract = ExtractByAttributes(inRaster, inSQLclause) 

# Save the output 
attExtract.save("P:/Studies/137708_COPitkin_ErosionHazard/Working/GIS/PitkinData.gdb/REM_heightAboveWS_clipRange")

print (arcpy.GetMessages())
