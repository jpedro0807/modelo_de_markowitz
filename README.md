# Índice de Markowitz: Simulação de Portfólios

<!-- Badges -->

![Last Commit](https://img.shields.io/github/last-commit/jpedro0807/modelo_de_markowitz?style=flat-square)
![Python 100.0%](https://img.shields.io/badge/Python-100%25-blue?style=flat-square\&logo=python)


## Descrição

Este repositório faz parte do meu portfólio e apresenta uma **simulação de portfólios** baseada no **Índice de Markowitz** (teoria de média-variância). O script em Python busca dados históricos de ativos da B3, calcula retornos esperados, matriz de covariância, e gera milhares de combinações aleatórias de pesos para identificar o portfólio com maior índice de Sharpe.

## Tecnologias Utilizadas

* **Linguagem**: Python 3
* **Bibliotecas**:

  * `numpy`
  * `pandas`
  * `yfinance`
  * `plotnine`
  * `seaborn`

## Estrutura do Projeto

```
/ (raiz do projeto)
├── markowitz.py            # Script principal de simulação
├── requirements.txt        # Dependências do Python
└── README.md               # Guia de uso e documentação
```

## Como Executar

1. **Instalar dependências**:

   ```bash
   pip install -r requirements.txt
   ```
2. **Rodar a simulação**:

   ```bash
   python markowitz.py
   ```

   * O script irá:

     1. Baixar preços de fechamento dos ativos configurados (ex.: ITSA4.SA, BBAS3.SA, ...).
     2. Calcular retornos diários e estatísticas (retorno esperado, covariância).
     3. Simular 1.000.000 de portfólios com pesos aleatórios.
     4. Identificar e imprimir o portfólio de melhor Sharpe.
     5. Gerar gráfico de dispersão (`Retorno Esperado` vs `Desvio Padrão`) mapeado pelo Sharpe.

## Funcionalidades

* **Coleta de Dados**: download automático de preços históricos via `yfinance`.
* **Cálculo Estatístico**: retornos diários, retorno médio, desvio padrão e matriz de covariância.
* **Simulação Monte Carlo**: geração de diversos portfólios com pesos aleatórios.
* **Otimização**: seleção do portfólio com maior índice de Sharpe (retorno/risco).
* **Visualização**: gráfico interativo feito com `plotnine` + `seaborn`.

## Built with the tools and technologies:

![Built with: Python](https://img.shields.io/badge/Built%20with-Python-lightgrey?style=flat-square\&logo=python\&logoColor=black)

## Contato

* **Nome**: João Pedro Barbosa da Silva
* **Email**: [jpedro080@hotmail.com](mailto:jpedro080@hotmail.com)
* **LinkedIn**: [https://www.linkedin.com/in/jpedro0807/](https://www.linkedin.com/in/jpedro0807/)

> Este projeto demonstra conhecimentos em análise quantitativa de investimentos, uso de bibliotecas financeiras em Python e visualização de dados para suporte à decisão de portfólio.
