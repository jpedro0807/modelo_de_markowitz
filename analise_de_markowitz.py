import numpy as np
import pandas as pd
import yfinance as yf
from plotnine import ggplot, aes, geom_point, labs
import seaborn as sns
sns.set()


sns.set()

start_date = '2014-01-01'
end_date = '2024-12-31'

<<<<<<< HEAD
assets = ['ITSA4.SA','BBAS3.SA', 'TASA4.SA','SAPR4.SA', 'PETR4.SA', 'BBDC4.SA']

df_data = yf.download(assets, start=start_date, end=end_date)

df_data = df_data.loc[:,('Close', slice(None))]

df_data.columns = assets


=======
assets = ['ITSA4.SA', 'BBAS3.SA', 'TASA4.SA', 'SAPR4.SA', 'PETR4.SA', 'BBDC4.SA']

df_data = yf.download(assets, start=start_date, end=end_date)

df_data = df_data.loc[:, ('Close', slice(None))]

df_data.columns = assets

>>>>>>> 0e7bd670c052256620f2abe09862d0878ffb93c7
df_pct_returns = df_data[assets].pct_change().dropna()

expected_return = df_pct_returns.mean()

covariance = df_pct_returns.cov()

<<<<<<< HEAD
portfolio_numbers = 100000


results = np.zeros((3,portfolio_numbers))


for i in range(portfolio_numbers):
    weights = np.random.random(len(assets))
    
    weights /= np.sum(weights)
    
    portfolio_return = np.sum(expected_return*weights)
    
    # 2) Risco do portfólio = sqrt(wᵀ · Cov · w)
    
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(covariance, weights))) 
    
=======
portfolio_numbers = 1000000

results = np.zeros((3, portfolio_numbers))

for i in range(portfolio_numbers):
    weights = np.random.random(len(assets))

    weights /= np.sum(weights)

    portfolio_return = np.sum(expected_return * weights)

    # 2) Risco do portfólio = sqrt(wᵀ · Cov · w)

    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))

>>>>>>> 0e7bd670c052256620f2abe09862d0878ffb93c7
    # 3) Sharpe = retorno / risco
    portfolio_sharpe = portfolio_return / portfolio_std_dev

    # armazena cada métrica na coluna i
    results[0, i] = portfolio_return
    results[1, i] = portfolio_std_dev
    results[2, i] = portfolio_sharpe
<<<<<<< HEAD
    


results_frame = pd.DataFrame(results.T, columns=['Retorno Esperado','Desvio Padrão','Sharpe'])
=======

results_frame = pd.DataFrame(results.T, columns=['Retorno Esperado', 'Desvio Padrão', 'Sharpe'])
>>>>>>> 0e7bd670c052256620f2abe09862d0878ffb93c7

idx_best = results_frame['Sharpe'].idxmax()

# 2) usa .loc para puxar a linha completa
best_portfolio = results_frame.loc[idx_best]

print(best_portfolio)

# Cria o gráfico de dispersão com barra para o Sharpe
<<<<<<< HEAD
(ggplot(results_frame, aes(x='Desvio Padrão', 
                           y='Retorno Esperado', 
                           color='Sharpe'))
 + geom_point()
 + labs(title="Simulação de Portfólios para os Ativos Selecionados")
)
=======
(ggplot(results_frame, aes(x='Desvio Padrão',
                           y='Retorno Esperado',
                           color='Sharpe'))
 + geom_point()
 + labs(title="Simulação de Portfólios para os Ativos Selecionados")
 )
>>>>>>> 0e7bd670c052256620f2abe09862d0878ffb93c7
