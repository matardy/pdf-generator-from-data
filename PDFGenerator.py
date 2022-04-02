from fpdf import FPDF 
from data_preprocessing import ExcelReader

class PDFGenerator(FPDF): 
    relative_positivon_y = 75
    relative_positivon_x = 18

    def header(self):
        self.image('bisel/img/header.jpeg',5,0,200)

    def footer(self):
        self.image('bisel/img/footer.jpeg',5,220,200)
        # Page number


    def create_template(self, city, email, telf):
        
        self.set_font('Arial', 'B', 10)
        #self.add_page()
        self.set_text_color(16,44,84)

        # Template: Ciudad, Telefono, Email 
        self.text(self.relative_positivon_x,self.relative_positivon_y, "Ciudad:  ")
        self.text(self.relative_positivon_x+18,self.relative_positivon_y, city)
        
        self.text(self.relative_positivon_x,self.relative_positivon_y+6, "Email: ")
        self.text(self.relative_positivon_x+18,self.relative_positivon_y+6, email)
        
        self.text(self.relative_positivon_x,self.relative_positivon_y+12,"Telefono: ")
        self.text(self.relative_positivon_x+18,self.relative_positivon_y+12, telf)

        # Template: Nombre, Cedula, Edad

        # rectangulo
        self.rect(self.relative_positivon_x+7, self.relative_positivon_y+25, self.relative_positivon_y+82,25)
        self.rect(self.relative_positivon_x+10, self.relative_positivon_y+48, 150,0)
    
        self.text(self.relative_positivon_x+10, self.relative_positivon_y+30, "Nombre: ")
        self.text(self.relative_positivon_x+120, self.relative_positivon_y+30, "Cedula: ")
        self.text(self.relative_positivon_x+120, self.relative_positivon_y+36, "Edad: ")
    
    def populate_pdf(self):
        df = ExcelReader('data.xlsx').get_df()
        
        for name, last_name, identification , date_birth in zip(df['Nombre'], df['Apellido'], df['Cedula'], df['Nacimiento']):
        # data tokenize
            full_name = name + " " + last_name
            ID = str(identification)
            birth = date_birth.strftime("%m/%d/%Y") 
            
            # populate pdf 
            self.add_page()
            self.create_template('Manta', 'stev@email.com', '0987868186')
           
            self.set_text_color(0,0,0)
            self.set_font('Arial','', 10)
            

           
            #self.create_template('Manta', 'stev@email.com', '0987868186')
            self.text(self.relative_positivon_x+27, self.relative_positivon_y+30, full_name)
            self.text(self.relative_positivon_x+140, self.relative_positivon_y+30, ID)
            self.text(self.relative_positivon_x+140, self.relative_positivon_y+36, birth)


        