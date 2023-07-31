from pdf2docx import converter

pdf_file = 'coding.pdf'
docx_file = 'coding.docx'
cv = converter(pdf_file)
cv.converter(docx_file)
cv.close()