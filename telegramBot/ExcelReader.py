import pandas as pd  
from pandas import DataFrame

class ExcelReader:

    """
    This class its in charge of the data preprocessing
    for the data that users inputs. 
    This Data its going to be used for the PDF that we 
    generate later.
    """



    df = '' # Instance variable that stores the data frame


    def __init__(self, file_name:str):
        """ Constructor of the class
        Args:
            file_name (str): Recieves the string of the .xlsx file.
        """

        self.file_name = file_name 
        self.df = pd.read_excel(pd.ExcelFile(file_name))

    def get_df(self)->DataFrame: 
        """ Getter: DataFrame
        Returns:
            DataFrame: Gets the Data Frame.
        """

        self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]
        return self.df

    def get_file_name(self)->str:
        """Getter: File Name
        Returns:
            str: Returns the name of the .xlsx file.
        """

        return self.file_name

