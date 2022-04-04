# Documentation here: https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html

from classes.data_preprocessing import ExcelReader
from classes.PDFGenerator import PDFGenerator


def main():


    df = ExcelReader('data.xlsx')
    pdf = PDFGenerator()
    pdf.populate_pdf(df,'Manta', 'info@biselmed.com', '0987868186', 'SOFIA R', 'P-04-00616', '05/06/2021', 'Prueba Rápida Covid-19')
    pdf.output('Certificates.pdf', 'F')

        


    



if __name__ == '__main__':
    main()