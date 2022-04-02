import pandas as pd  
from pandas import DataFrame

class ExcelReader:
    df = ''

    def __init__(self, file_name:str):
        self.file_name = file_name 
        self.df = pd.read_excel(pd.ExcelFile(file_name))

    def get_df(self)->DataFrame: 
        self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]
        return self.df

    def get_file_name(self)->str:
        return self.file_name
   
        

