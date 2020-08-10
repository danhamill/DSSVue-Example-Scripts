
from hec.script import Plot, MessageBox
from hec.heclib.dss import HecDss, DSSPathname
import java
import sys

filename =""
print( len(sys.argv))

#  relative filename to VSCode workspace directory
# , assuming running in vscode with .vscode/tasks.json and scripts/go.bat
if len(sys.argv) == 2:
  filename=sys.argv[1]+"/data/sample.dss"
  print("filename = ",filename)
  


#  Open the file and get the data
try :
  dssFile = HecDss.open(filename)
  airTemp = dssFile.get("/GREEN RIVER/OAKVILLE/AIRTEMP/01MAY1992/1HOUR/OBS/")
  outflow = dssFile.get("/GREEN RIVER/OAKVILLE/FLOW-RES OUT/01MAY1992/1HOUR/OBS/")
  dssFile.done()
except java.lang.Exception, e :
  #  Take care of any missing data or errors
   MessageBox.showError(e.getMessage(), "Error reading data")

#  Initialize the plot and add data
plot = Plot.newPlot("Oakville")
plot.addData(airTemp)
plot.addData(outflow)

#  Create plot
plot.setSize(600,600)
plot.setLocation(100,100)
plot.showPlot()

#  Change the plot
outCurve = plot.getCurve(outflow)
outCurve.setLineColor("darkgreen")

#  Save the plot and close
plot.saveToPng("C:/temp/Oakville.png")
#plot.close()  #  Do this if you only want the plot as a .png and not on screen
