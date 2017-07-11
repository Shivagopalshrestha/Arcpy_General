HowTo:  Create sequential numbers in a field using Python in the Field Calculator


Article ID:  https://dragons8mycat.wordpress.com/2013/08/15/gis-tips-arcgis-create-sequential-numbers-in-the-attribute-table-without-using-fid/
38517 

Software:
 ArcGIS – ArcEditor 10 ArcGIS – ArcInfo 10 ArcGIS – ArcView 10 


Summary

	Instructions provided describe how to create sequential numbers in a field using Python in the Field Calculator.

Procedure

	The code in this article generates sequential numbers for unsorted data based on the OID or FID order. If your data is sorted on a field, the generated numbers will not be sequential.

	1.Create a new short integer field.
	2.Set the Parser to Python.
	3.Select Show Codeblock.
	4.Paste the following into the Pre-Logic Script Code: 

rec=0 
def autoIncrement(): 
 global rec 
 pStart = 1  
 pInterval = 1 
 if (rec == 0):  
  rec = pStart  
 else:  
  rec += pInterval  
 return rec

5.Paste the following code in the smaller box below the Pre-Logic Script Code: 

autoIncrement()

6.Click OK.
