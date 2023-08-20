import PyPDF2    # pip install pypdf2

files = ["1.pdf", "2.pdf"]
merged = PyPDF2.PdfMerger()
for x in files:
    file = open(x,'rb')
    pdf_read = PyPDF2.PdfReader(file)
    merged.append(pdf_read)
file.close()
merged.write("Merged.pdf")