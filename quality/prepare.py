import pandas as pd
    
class Prepare:
    
    def __init__(self, data, _config):
        self.data = data
        self.configs = _config
        self.len_cols = max(list(self.configs["id"]))
        self.colunas = list(self.configs['nome_original'])
        self.colunas_new = list(self.configs['nome'])  

    def select_cols(self):
        self.data = self.data.loc[:, self.colunas] 
        
    def rename_cols(self):
        for i in range(self.len_cols):
            self.data.rename(columns={self.colunas[i]:self.colunas_new[i]}, inplace = True)
        
    def data_type(self):
        for col in self.colunas_new:
            tipo = self.configs.loc[self.configs['nome'] == col]['tipo'].item()
            if tipo == "int":
                self.data[col] = self.data[col].astype(int)
            elif tipo == "float":
                self.data[col] = self.data[col].replace(",", ".", regex=True)
                self.data[col] = self.data[col].astype(float)
            elif tipo == "date":
                self.data[col] = pd.to_datetime(self.data[col]).dt.strftime('%Y-%m-%d')
            elif tipo == "str":
                self.data[col] = self.data[col].astype(str)

    def return_data(self):
        return self.data