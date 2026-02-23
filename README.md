# 🫀 Análise Exploratória: Fatores de Risco para Ataques Cardíacos

## 🎯 Objetivo do Projeto
Este projeto realiza uma Análise Exploratória de Dados (EDA) detalhada sobre um conjunto de dados clínicos, com o objetivo de identificar padrões demográficos e médicos associados ao risco de ataques cardíacos. O foco principal foi ir além das contagens absolutas, investigando proporções, correlações estatísticas e possíveis vieses de seleção na amostra.

🔗 **[Acesse o Notebook interativo publicado no Kaggle](https://www.kaggle.com/code/laregou/an-lise-de-ataques-card-acos)**

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn

## 🔍 Metodologia
1. **Limpeza e Formatação de Dados:** Renomeação de variáveis clínicas para termos legíveis em português e transformação de dados categóricos numéricos (ex: 0 e 1) em descrições textuais claras.
2. **Análise Demográfica:** Investigação da distribuição de pacientes por sexo e agrupamento de faixas etárias personalizadas para garantir relevância estatística e evitar o problema de amostras pequenas (Small Sample Size).
3. **Análise Bivariada:** Cruzamento de sintomas relatados e resultados de exames com a variável alvo (Diagnóstico de Risco).
4. **Análise de Correlação:** Utilização de Matriz de Correlação e Mapas de Calor (Heatmaps) para avaliar relações lineares entre sinais vitais.

## 💡 Principais Descobertas e Insights Estatísticos

* **O Paradoxo da Dor no Peito:** Ao analisar a proporção de diagnósticos, observou-se que a "Angina Típica" (dor clássica) apresentou um índice menor de risco quando comparada com dores categorizadas como "Angina Atípica" ou "Não Anginosa" dentro deste dataset.
* **Idade e Viés de Seleção:** As faixas etárias mais jovens testadas (até 40 anos e 41-50 anos) apresentaram os maiores percentuais relativos de risco. Isso aponta para um forte viés de seleção na amostra, onde pacientes mais jovens tendem a realizar exames complexos apenas quando já apresentam sintomas graves, enquanto pacientes mais velhos (51 a 60+ anos) compõem a maior parte da base devido a exames de rotina preventiva.
* **A Matemática dos Sinais Vitais:** O Mapa de Calor confirmou a correlação negativa esperada pela biologia humana entre a idade e a frequência cardíaca máxima (-0.40).
* **A (Falta de) Influência Isolada do Colesterol:** O cruzamento estatístico e visual (Boxplot) revelou uma correlação praticamente nula (-0.09) entre os níveis de colesterol sérico e o risco de infarto. As medianas e a distribuição interquartil foram visualmente sobreponíveis entre os grupos de maior e menor risco, indicando que o colesterol, isoladamente, não foi um preditor linear forte para esta amostra clínica.

## 📂 Estrutura do Repositório
* `analise-ataques-cardiacos.ipynb`: Código completo contendo a etapa de formatação, agrupamentos e geração de todos os gráficos.
* `Heart Attack Data Set.csv`: Base de dados original (raw data) utilizada para a análise.

---
*Desenvolvido como projeto prático de portfólio para aprofundamento em Ciência de Dados e Estatística Aplicada à Saúde.*
