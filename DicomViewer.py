import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pydicom.data import get_testdata_files
import pydicom

base=input("enter folder path:")

Fname=input("enter folder name: ")
Pname=input("enter pdf name to save")

var1=os.listdir(base+'/'+Fname)
var2=len(var1)

with PdfPages(base+'/'+Pname+'.pdf') as exportPDF:

        for i in range(0,var2):
              filename=pydicom.data.data_manager.get_files(base,Fname)[i]
              ds = pydicom.dcmread(filename)
              plt.title(filename,fontsize=10)
              plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
              exportPDF.savefig()
              plt.close()
print(Pname+".pdf File Created Successfully!!!!!!")

