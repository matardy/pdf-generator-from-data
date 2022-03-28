# Documentation here: https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html

from fpdf import FPDF 
import pandas as pd

def main():
    # xlsx to dataframe 
    xlsx_file = pd.ExcelFile('data.xlsx')
    df = pd.read_excel(xlsx_file)
    columns = df.columns
    
   # pdf generation : here its a blank page
    pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    pdf.set_font('Arial','', 10)

    # iterate through dataset, and put every row in a different page. 

    for name, last_name, identification , date_birth in zip(df['Nombre'], df['Apellido'], df['Cedula'], df['Nacimiento']):
        # data tokenize
        full_name = name + " " + last_name
        ID = str(identification)
        birth = date_birth.strftime("%m/%d/%Y") 
        
        # populate pdf 
        pdf.add_page()
        pdf.text(10,100, full_name)
        pdf.text(100,100, birth)
        pdf.text(160,100, ID)

        

    # pdf output.
    pdf.output('foo.pdf', 'F') 

   
        


    



if __name__ == '__main__':
    main()