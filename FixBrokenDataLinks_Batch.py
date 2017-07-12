# FIX BROKEN DATA LINKS IN A NUMER OF .MXDS 
# Useful for when project file names are changed, or project files are imported from another drive/server/etc.
# Data links in arcmap documents are broken when such changes occur. This script updates

import os, arcpy

# http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-mapping/updatingandfixingdatasources.htm
# http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-mapping/mapdocument-class.htm
# https://gis.stackexchange.com/questions/72329/getting-the-name-of-the-mxd-using-python


#arcpy.env.workspace = r"C:\Users\Daniel.Aragon\Desktop\TEMP\WeirGulch_Working_dja\temp"
workspace = r"C:\Users\Daniel.Aragon\Desktop\TEMP\WeirGulch_Working_dja\temp\Maps_backup"
arcpy.env.workspace = workspace

# Define the old (outdated) and new (updated) file paths where data resides
oldpath1 = r"R:\Weir Gulch MDP & FHAD"
oldpath2 = r"P:\UZ\U\UDFCD\124372"
newpath = r"R:\144519_Weir Gulch MDP & FHAD"

# Create list of mxds in workspace
mxdlist = arcpy.ListFiles("*.mxd")
print (mxdlist)

# Loop through mxdlist and update file paths within those map documents
for mapdoc in mxdlist:
	print (mapdoc)
	filePath = os.path.join(workspace, mapdoc)
	mxd = arcpy.mapping.MapDocument(filePath)
	mxd.findAndReplaceWorkspacePaths(oldpath1, newpath)
	mxd.findAndReplaceWorkspacePaths(oldpath2, newpath)
	mxd.save()
	del mxd


