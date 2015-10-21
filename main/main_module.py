__author__ = 'Geoffrey'
import PyPDF2

print('Please Provide the PDF You Would Like to Use')
FileName = input('Filename: ')
print('Please Provide the Interval Amount To Split the Document')
SplitInterval = input('Split Interval: ')


PDF_Read = PyPDF2.PdfFileReader(FileName)
pagelimit = PDF_Read.getNumPages()


if 'CQM' in FileName:
    for x in range(1,pagelimit):
        TestPrint = (PDF_Read.getPage(x))
        print(TestPrint.extractText())
elif 'Measure' in FileName:
    for x in range(1,pagelimit):
        TestPrint = (PDF_Read.getPage(x))
        print(TestPrint.extractText())
