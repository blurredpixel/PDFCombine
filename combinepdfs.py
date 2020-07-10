import os, PyPDF2
print("If PDFs are in the current path with the program, enter a single period '.' ")
path = input("Enter Path to PDFs (C:\\users\\...)")
os.chdir(path)

filename=input("Output file name (omit .PDF)?")

files=[file for file in os.listdir('.') if file.endswith('.pdf')]

pdfwriter=PyPDF2.PdfFileWriter()
for file in files:
    print(file)
    pdffile=open(file,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffile)
    for num in range(pdfreader.numPages):
        pageobj=pdfreader.getPage(num)
        pdfwriter.addPage(pageobj)
    output=open(filename+'.pdf','wb')
    pdfwriter.write(output)
    output.close()
