from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=1, end=2)
    cv.close()

convert_pdf_to_docx('/Users/yuhyeonseung/Downloads/test.pdf', '/Users/yuhyeonseung/Downloads/test.pdfoutput.docx')
