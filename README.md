# Seismic Data Analysis - Braskem Project

Este repositório contém ferramentas e notebooks para análise de dados sismológicos, com foco em ortogonalização de sensores e análise de ruídos em dados sísmicos.

## 📋 Descrição do Projeto

O projeto tem como objetivo principal:

- **Ortogonalização de Dados Sísmicos**: Análise e processamento de dados de sensores sísmicos para ortogonalização
- **Detecção e Análise de Ruídos**: Identificação de padrões anômalos e ruídos nos dados sísmicos
- **Análise de Energia Total**: Cálculo e análise da energia total dos eventos sísmicos usando componentes x, y, z
- **Classificação de Eventos**: Categorização de eventos sísmicos por nível de energia e qualidade dos dados

## 🗂️ Estrutura do Projeto

```
data_analysis/
├── README.md                              # Este arquivo
├── .gitignore                            # Arquivos ignorados pelo Git
├── analise_energia_total.ipynb            # Notebook principal de análise
├── ortogonalizacao_sensores_notebook.ipynb # Notebook de ortogonalização
├── Braskem_dados/                        # Dados de entrada (ver README específico)
│   └── Eventos/                          # Dados de eventos sísmicos
├── resultados_csv/                       # Resultados processados (ver README específico)
└── resultados_energia/                   # Resultados da análise de energia (gerado automaticamente)
```

## 🔬 Principais Análises

### 1. Análise de Energia Total
- Cálculo da energia total: **E = √(x² + y² + z²)**
- Agrupamento por `event_id` para análise de distribuição
- Identificação de eventos com alta variabilidade (possíveis ruídos)
- Classificação automática de eventos por nível de energia

### 2. Detecção de Ruídos
- **Coeficiente de Variação**: Identificação de eventos com alta dispersão
- **Análise de Percentis**: Detecção de valores extremos
- **Classificação Automática**: Eventos classificados como "ruído" ou "limpo"
- **Visualizações Comparativas**: Gráficos mostrando diferenças entre eventos

### 3. Análise Estatística
- Estatísticas descritivas por evento
- Correlações entre componentes x, y, z
- Distribuição de energia por sensor e plano
- Relatórios detalhados de qualidade dos dados

## 📊 Outputs Gerados

### Arquivos CSV de Resultado:
- `eventsA001_cut25seg_results_with_energy.csv` - Dados originais + energia calculada + classificações
- `eventsA001_energia_total_summary.csv` - Resumo estatístico da análise
- `eventos_possiveis_ruidos.csv` - Relatório específico de eventos com possível ruído

### Novas Colunas Adicionadas:
- `total_energy` - Energia total calculada
- `energy_rank` - Ranking de energia
- `energy_percentile` - Percentil de energia
- `event_energy_class` - Classificação do evento (Baixa/Média/Alta)
- `potential_noise_event` - Flag para possível ruído
- `high_energy_flag` - Flag para alta energia individual

## 🚀 Como Usar

### Pré-requisitos
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Preparação dos Dados
1. Coloque os dados de entrada nas pastas apropriadas (veja READMEs específicos)
2. Verifique se os arquivos seguem a nomenclatura esperada
3. Execute o notebook `analise_energia_total.ipynb`

### Execução
1. Abra o Jupyter Notebook:
   ```bash
   jupyter notebook analise_energia_total.ipynb
   ```
2. Execute as células sequencialmente
3. Os resultados serão salvos automaticamente na pasta `resultados_energia/`

## 📈 Visualizações Incluídas

- **Gráficos Comparativos**: Eventos com ruído vs eventos limpos
- **Scatter Plots**: Energia vs Event ID com classificação
- **Box Plots**: Comparação estatística entre categorias
- **Heatmaps**: Correlações entre componentes
- **Histogramas**: Distribuições de energia e variabilidade

## 🔧 Configuração do Ambiente

O projeto foi desenvolvido e testado com:
- Python 3.8+
- Pandas 1.x+
- NumPy 1.x+
- Matplotlib 3.x+
- Seaborn 0.11+
- Jupyter Notebook

## 📁 Estrutura de Dados Esperada

Consulte os arquivos README específicos em cada pasta:
- `Braskem_dados/Eventos/README.md` - Formato dos dados de eventos
- `resultados_csv/README.md` - Formato dos resultados processados

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é propriedade da Braskem e destinado para uso interno de análise de dados sísmicos.

## 📞 Contato

Para dúvidas sobre o projeto, entre em contato com a equipe responsável pela análise sismológica.

---

**Nota**: Os dados sísmicos originais não estão incluídos neste repositório por questões de segurança e tamanho. Consulte os READMEs específicos das pastas para saber quais arquivos são necessários.
