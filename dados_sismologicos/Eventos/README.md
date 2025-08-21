# Pasta de Eventos Sísmicos

Esta pasta deve conter os dados de eventos sísmicos em formato CSV para análise.

## 📋 Arquivos Esperados

### Arquivos de Eventos Principais:
```
eventsA001_cut25seg.csv
eventsA001_cut25seg_coords.csv
eventsA002_cut25seg.csv
eventsA002_cut25seg_coords.csv
eventsA003_cut25seg.csv
eventsA003_cut25seg_coords.csv
eventsD001_cut25seg.csv
eventsD001_cut25seg_coords.csv
eventsE001_cut25seg.csv
eventsE001_cut25seg_coords.csv
eventsF001_cut25seg.csv
eventsF001_cut25seg_coords.csv
eventsNDA_cut25seg.csv
eventsNDA_cut25seg_coords.csv
eventsNDA0_cut25seg.csv
eventsNDA1_cut25seg.csv
```

### Arquivos de Análise:
```
Feature Analysis.ipynb           # Notebook de análise de features
feature_correlations.csv        # Correlações entre features
```

### Arquivo Excel (Opcional):
```
eventsA001_cut25seg.xlsx        # Versão Excel dos dados
```

## 📊 Formato dos Dados Esperado

### Arquivo Principal de Eventos (`events*.csv`):
Cada arquivo CSV deve conter as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `event_id` | int | Identificador único do evento sísmico |
| `plane` | string | Plano sísmico (ex: Plano_E, Plano_G, Plano_H) |
| `max_magnitude` | float | Magnitude máxima registrada |
| `sensor` | string | Identificador do sensor (ex: SC.MAC11.00, BR.ESM09) |
| `x_amplitude` | float | Amplitude na direção X |
| `y_amplitude` | float | Amplitude na direção Y |
| `z_amplitude` | float | Amplitude na direção Z |
| `source_file` | string | Arquivo fonte dos dados |

### Exemplo de Dados:
```csv
event_id,plane,max_magnitude,sensor,x_amplitude,y_amplitude,z_amplitude,source_file
71355,Plano_E,8.221685819782874e-06,SC.MAC11.00,5.311947914910374e-06,4.619219562237287e-06,4.247603760279728e-06,eventsA001_cut25seg.csv
71355,Plano_G,4.619101879705084e-06,BR.ESM09,3.3824204760572643e-06,1.8428907226242277e-06,2.5493308303766977e-06,eventsA001_cut25seg.csv
```

### Arquivo de Coordenadas (`*_coords.csv`):
Contém informações de localização dos eventos (formato específico conforme necessário).

## 🔧 Requisitos de Formato

### Dados Numéricos:
- **Amplitudes**: Podem estar em notação científica (ex: 1.23e-06)
- **Event IDs**: Números inteiros únicos
- **Valores nulos**: Não são permitidos nas colunas de amplitude

### Codificação:
- **Encoding**: UTF-8
- **Separador**: Vírgula (,)
- **Decimal**: Ponto (.)

### Nomenclatura:
- Mantenha a convenção de nomes existente
- Formato: `events[CÓDIGO]_cut25seg.csv`
- Coordenadas: `events[CÓDIGO]_cut25seg_coords.csv`

## ⚠️ Importante

1. **Não commitar dados reais**: Os arquivos CSV com dados reais não devem ser enviados ao repositório
2. **Estrutura obrigatória**: Mantenha a estrutura de colunas conforme especificado
3. **Qualidade dos dados**: Verifique se não há valores nulos nas colunas críticas
4. **Tamanho dos arquivos**: Arquivos muito grandes podem impactar a performance

## 🔍 Validação dos Dados

Antes de executar a análise, verifique:

- [ ] Todas as colunas obrigatórias estão presentes
- [ ] Não há valores nulos em `x_amplitude`, `y_amplitude`, `z_amplitude`
- [ ] `event_id` contém valores únicos por linha
- [ ] Dados estão em formato numérico correto
- [ ] Encoding está em UTF-8

## 📝 Exemplo de Uso

Para verificar se seus dados estão no formato correto:

```python
import pandas as pd

# Carregar dados
df = pd.read_csv('eventsA001_cut25seg.csv')

# Verificar estrutura
print(df.columns.tolist())
print(df.dtypes)
print(df.isnull().sum())

# Verificar primeiras linhas
print(df.head())
```

---

**Nota**: Esta pasta deve conter apenas dados de eventos sísmicos. Para resultados processados, utilize a pasta `resultados_csv/`.
