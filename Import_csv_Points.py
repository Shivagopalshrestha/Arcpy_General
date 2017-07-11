# WORKING 1.25.2017
# Script for automating import of  CSV format into shapefiles.  CSV format must only have one row of column names!!!!!!!!!!
# CSV Must be cleaned and formated with X, Y, and  Z column headings OR script updated below
# Script developed by Daniel Aragon at Michael Baker Intl, (720)514-1100

import os
import arcpy

# Environment Settings: Workspace, and two output workspaces depending on type of modeling result
arcpy.env.workspace = r"C:\Users\Daniel.Aragon\Downloads\COGCC_spills"
outworkspace =  r"C:\Users\Daniel.Aragon\Downloads\COGCC_spills"
arcpy.env.overwriteOutput = True

# Define coordinate system
CSV_coordinate_system = r"C:\Users\Daniel.Aragon\AppData\Roaming\ESRI\Desktop10.4\ArcMap\Coordinate Systems\NAD 1983 UTM Zone 13N.prj"


# For each csv in file, generate a point file and polygon file of results

for csv_file in arcpy.ListFiles("*.csv"):

    # define file names  and pathways for temporary features
    file_name = (os.path.splitext(csv_file)[0])
    temp1 = os.path.join("in_memory", file_name + "_temp1")
    temp2 = os.path.join("in_memory", file_name + "_temp2")
    temp2a = "temp2a"
  
    
    # define file names and pathways for output files 
    output1 = os.path.join(outworkspace, file_name + "_pt.shp")   

    # define local variables from the CSV headings
    CSV_x = "well_utm_x"
    CSV_y = "well_utm_y"
    CSV_z = "well_elevation"

    # make the event layer
    arcpy.MakeXYEventLayer_management(csv_file, CSV_x, CSV_y, temp1, CSV_coordinate_system, CSV_z)
    # save to temporary shapefile
    arcpy.CopyFeatures_management(temp1, temp2)
    # make feature layer for select by attribute tool
    arcpy.MakeFeatureLayer_management(temp2, temp2a)

    # save only selected features to shapefile
    arcpy.CopyFeatures_management(temp2a, output1)



    # delete in_memory objects (temps)
    arcpy.Delete_management("in_memory")




