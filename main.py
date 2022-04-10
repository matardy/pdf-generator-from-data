# Documentation here: https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html

from  telegramBot.telegramBotHandler import city



def main():

    print(city)
    file_name = str(os.popen('ls | grep .xlsx').read())
    file_name = file_name.rstrip('\n')
    df = ExcelReader(str(file_name))
    pdf = PDFGenerator()
    pdf.populate_pdf(df,'Manta', 'info@biselmed.com', '0987868186', 'SOFIA R', 'P-04-00616', '05/06/2021', 'Prueba Rápida Covid-19')
    print("Generating pdf..")
    pdf.output('/Users/gutembergmendoza/Stev/Python/PDF_generator/telegramBot/Certificates.pdf', 'F')

    

    



if __name__ == '__main__':
    main()