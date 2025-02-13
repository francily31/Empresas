import yfinance as yf
import pandas as pd

# Lista das empresas desejadas
empresas = ["GOLL4.SA", "MRVE3.SA", "ABEV3.SA", 
            "SUZB3.SA", "LREN3.SA", "ELET3.SA", 
            "PETR4.SA", "BRFS3.SA", "VALE3.SA"]

# Inicio e fim dos dados
start_date = "2022-01-01"
end_date = "2024-11-10"

dados_completos = pd.DataFrame()

for empresa in empresas:
    data = yf.download(empresa, start=start_date, end=end_date)
    
    data = data.reset_index()
    
    data.insert(1, 'Empresa', empresa)  
    data['Ano'] = pd.to_datetime(data['Date']).dt.year  
    data['Date'] = pd.to_datetime(data['Date']).dt.date  
    
    data = data.rename(columns={
        "Date": "Data",
        "Open": "Abertura",
        "High": "Alta",
        "Low": "Baixa",
        "Close": "Fechamento",
        "Adj Close": "Fechamento Ajustado",
        "Volume": "Volume"
    })
    
    data = data[['Data', 'Ano', 'Empresa', 'Abertura', 'Alta', 'Baixa', 'Fechamento', 'Volume', 'Fechamento Ajustado']]
    
    dados_completos = pd.concat([dados_completos, data], ignore_index=True)

dados_completos.to_csv("Empresas.csv", index=False)

print("Arquivo único 'Empresas.csv' gerado com sucesso!")
