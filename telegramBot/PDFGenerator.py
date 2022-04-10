import pandas as pd
from pandas import DataFrame
from fpdf import FPDF 
from data_preprocessing import ExcelReader

class PDFGenerator(FPDF): 
    # TODO: Documentar el codigo.
    # This instance variables store the relative position of template
    relative_position_y = 75
    relative_position_x = 18

    def header(self):
        self.image('bisel/img/header.jpeg',5,0,200)

    def footer(self):
        self.image('bisel/img/footer.jpeg',5,220,200)
        


    def create_template(self, city, email, telf, emb,sample_date,test):
        
        self.set_font('Arial', 'B', 10)
       
        self.set_text_color(16,44,84)

        # Template: Ciudad, Telefono, Email 
        self.text(self.relative_position_x+10,self.relative_position_y, "Ciudad ")
        self.text(self.relative_position_x+23,self.relative_position_y, city)
        
        self.text(self.relative_position_x+10,self.relative_position_y+6, "Email: ")
        self.text(self.relative_position_x+23,self.relative_position_y+6, email)
        
        self.text(self.relative_position_x+10,self.relative_position_y+12,"Telefono: ")
        self.text(self.relative_position_x+27,self.relative_position_y+12, telf)

        # Template: Nombre, Cedula, Edad

        # rectangulo
        self.set_text_color(0,0,0)
        self.rect(self.relative_position_x+7, self.relative_position_y+25, self.relative_position_y+82,40)
        self.rect(self.relative_position_x+10, self.relative_position_y+63.5, 153,0)
    
        self.text(self.relative_position_x+10, self.relative_position_y+30, "EMBARACIÓN: ")
        self.text(self.relative_position_x+38, self.relative_position_y+30, emb)


        self.text(self.relative_position_x+10, self.relative_position_y+36, "NOMBRE: ")
        self.text(self.relative_position_x+10, self.relative_position_y+42, "FECHA DE TOMA DE MUESTRA: ")
        self.text(self.relative_position_x+66, self.relative_position_y+42, sample_date)


        self.text(self.relative_position_x+10, self.relative_position_y+56, "MÉDICO: Dr. Elvis E. Mendoza Mestanza ")
        
        self.text(self.relative_position_x+10, self.relative_position_y+61, "ANÁLISIS: ")
        self.text(self.relative_position_x+30, self.relative_position_y+61, test)



        # self.text(self.relative_position_x+95, self.relative_position_y+30, "MATRÍCULA: ")
        # self.text(self.relative_position_x+119, self.relative_position_y+30, matr)


        self.text(self.relative_position_x+95, self.relative_position_y+36, "CÉDULA: ")
        self.text(self.relative_position_x+95, self.relative_position_y+42, "FECHA DE NACIMIENTO: ")
        self.text(self.relative_position_x+95, self.relative_position_y+61, "REGISTRO SANITARIO: 8385-DME-0420 ")

        self.text(self.relative_position_x+20, self.relative_position_y+80, "DETERMINACIÓN DE ANTICUERPOS PARA SARS-COV-2 (COVID-19) ")
        self.text(self.relative_position_x+20, self.relative_position_y+84.5, "TÉCNICA: ")
        self.set_font('Arial','',10)
        self.text(self.relative_position_x+40, self.relative_position_y+84.5, "Determinación de Anticuerpos IgG - IgM inmunocromatográfica.")

        self.set_font('Arial','B',13)
        self.text(self.relative_position_x+70, self.relative_position_y+108, "RESULTADOS")

        self.set_font('Arial','B',10)
        self.text(self.relative_position_x+20, self.relative_position_y+120, "ANTICUERPOS IgG")
        self.text(self.relative_position_x+20, self.relative_position_y+126, "ANTICUERPOS IgM")
        





    def populate_pdf(self, df,city, email, telf, emb,sample_date,test):
        df = df.get_df()
        for name, last_name, identification , date_birth, status in zip(df['Nombre'], df['Apellido'], df['Cedula'], df['Nacimiento'], df['Estado']):
        # data tokenize
            full_name = name + " " + last_name
            ID = str(identification)
            birth = str(date_birth)
            st = str(status)
            
            # populate pdf 
            self.add_page()
            self.create_template(city, email, telf, emb,sample_date,test)
           
            self.set_text_color(0,0,0)
            self.set_font('Arial','', 10)
            

           
            #self.create_template('Manta', 'stev@email.com', '0987868186')
            self.text(self.relative_position_x+28, self.relative_position_y+36, full_name)
            self.text(self.relative_position_x+114, self.relative_position_y+36, ID)
            self.text(self.relative_position_x+140, self.relative_position_y+42, birth)
            self.text(self.relative_position_x+120, self.relative_position_y+120, st)
            self.text(self.relative_position_x+120, self.relative_position_y+126, st)

        