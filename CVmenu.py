import CVbuildDataDB as cvbuild
import CVcheckfiles as cvcf
import CVuptodateDB as cvup

menu = {}
menu['1']="Download last CV files and Update DB" 
menu['2']="Download last CV files"
menu['3']="Download all CV files"
menu['4']="Insert all values in the DB from all known files"
menu['0']="EXIT"

options=menu.keys()
for entry in options: 
   print(entry, menu[entry])

selection=input("Please Select: ") 
if selection =='1': 
   cvup.uptodate()
elif selection == '2': 
   cvcf.downloadCVfiles("uptodate")
elif selection == '3':
   cvcf.downloadCVfiles("begin")
elif selection == '4': 
   cvbuild.data()
elif selection == '0':
       print("Program terminated")
else: 
   print ("Unknown Option Selected!") 