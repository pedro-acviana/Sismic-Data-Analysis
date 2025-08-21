# Pasta de Resultados CSV

Esta pasta deve conter os resultados processados dos dados sísmicos em formato CSV.

## 📋 Arquivos Esperados

### Arquivos de Resultados Principais:
```
eventsA001_cut25seg_results.csv
eventsA002_cut25seg_results.csv
eventsA003_cut25seg_results.csv
eventsD001_cut25seg_results.csv
eventsE001_cut25seg_results.csv
eventsF001_cut25seg_results.csv
eventsNDA_cut25seg_results.csv
eventsNDA0_cut25seg_results.csv
eventsNDA1_cut25seg_results.csv
```

### Arquivos de Consolidação:
```
CONSOLIDADO_todos_arquivos.csv      # Consolidação de todos os eventos
ESTATISTICAS_PROCESSAMENTO.csv      # Estatísticas do processamento
```

## 📊 Formato dos Dados Esperado

### Arquivo de Resultados (`*_results.csv`):
Cada arquivo deve conter as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `event_id` | int | Identificador único do evento sísmico |
| `plane` | string | Plano sísmico (Plano_E, Plano_G, Plano_H) |
| `max_magnitude` | float | Magnitude máxima registrada |
| `sensor` | string | Identificador do sensor |
| `x_amplitude` | float | Amplitude processada na direção X |
| `y_amplitude` | float | Amplitude processada na direção Y |
| `z_amplitude` | float | Amplitude processada na direção Z |
| `source_file` | string | Arquivo fonte original |

### Exemplo de Dados:
```csv
event_id,plane,max_magnitude,sensor,x_amplitude,y_amplitude,z_amplitude,source_file
71355,Plano_E,8.221685819782874e-06,SC.MAC11.00,5.311947914910374e-06,4.619219562237287e-06,4.247603760279728e-06,eventsA001_cut25seg.csv
71355,Plano_G,4.619101879705084e-06,BR.ESM09,3.3824204760572643e-06,1.8428907226242277e-06,2.5493308303766977e-06,eventsA001_cut25seg.csv
71355,Plano_H,9.949358966112327e-06,BR.ESM08,5.0398112033706266e-06,7.826914946590054e-06,3.5113315550920123e-06,eventsA001_cut25seg.csv
```

## 🔧 Especificações Técnicas

### Processamento de Dados:
- **Amplitudes**: Valores processados e filtrados dos dados brutos
- **Segmentação**: Dados cortados em segmentos de 25 segundos
- **Qualidade**: Dados já passaram por verificação de qualidade

### Formato de Arquivo:
- **Encoding**: UTF-8
- **Separador**: Vírgula (,)
- **Decimal**: Ponto (.)
- **Cabeçalho**: Primeira linha contém nomes das colunas

### Convenções de Nomenclatura:
- **Padrão**: `events[CÓDIGO]_cut25seg_results.csv`
- **Códigos válidos**: A001, A002, A003, D001, E001, F001, NDA, NDA0, NDA1
- **Sufixo obrigatório**: `_results.csv`

## 📈 Arquivo Consolidado

### `CONSOLIDADO_todos_arquivos.csv`:
Contém todos os eventos de todos os arquivos em um único dataset:
- Mesma estrutura dos arquivos individuais
- Coluna adicional identificando arquivo de origem
- Ordenado por `event_id` e `sensor`

### `ESTATISTICAS_PROCESSAMENTO.csv`:
Contém métricas do processamento:
- Número total de eventos por arquivo
- Estatísticas de qualidade
- Resumo de sensores e planos
- Informações de tempo de processamento

## ⚠️ Validação dos Dados

### Verificações Obrigatórias:
- [ ] Todas as colunas obrigatórias presentes
- [ ] Valores de amplitude são numéricos
- [ ] Não há valores nulos em colunas críticas
- [ ] `event_id` são números inteiros válidos
- [ ] `plane` contém apenas valores válidos (Plano_E, Plano_G, Plano_H)

### Valores Esperados:
- **Amplitudes**: Geralmente entre 1e-08 e 1e-03
- **Event IDs**: Números inteiros > 0
- **Sensores**: Formato padrão (ex: SC.MAC11.00, BR.ESM09)

## 🔍 Scripts de Validação

### Verificação Básica:
```python
import pandas as pd

def validate_results_file(filepath):
    """Valida arquivo de resultados"""
    try:
        df = pd.read_csv(filepath)
        
        # Verificar colunas obrigatórias
        required_cols = ['event_id', 'plane', 'max_magnitude', 'sensor', 
                        'x_amplitude', 'y_amplitude', 'z_amplitude', 'source_file']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            print(f"❌ Colunas faltando: {missing_cols}")
            return False
            
        # Verificar valores nulos
        null_counts = df[['x_amplitude', 'y_amplitude', 'z_amplitude']].isnull().sum()
        if null_counts.sum() > 0:
            print(f"❌ Valores nulos encontrados: {null_counts.to_dict()}")
            return False
            
        # Verificar tipos de dados
        if not pd.api.types.is_numeric_dtype(df['event_id']):
            print("❌ event_id deve ser numérico")
            return False
            
        print(f"✅ Arquivo válido: {filepath}")
        print(f"   - {len(df)} registros")
        print(f"   - {df['event_id'].nunique()} eventos únicos")
        print(f"   - {df['sensor'].nunique()} sensores únicos")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return False

# Exemplo de uso
validate_results_file('eventsA001_cut25seg_results.csv')
```

## 📊 Uso no Pipeline de Análise

Estes arquivos são utilizados como entrada para:

1. **Análise de Energia Total** (`analise_energia_total.ipynb`)
2. **Ortogonalização de Sensores** (`ortogonalizacao_sensores_notebook.ipynb`)
3. **Detecção de Ruídos** (análise automática)
4. **Geração de Relatórios** (estatísticas e visualizações)

## 📁 Estrutura de Saída

Após o processamento, os resultados são salvos em `resultados_energia/`:
- Dados originais + energia calculada
- Classificação de ruídos
- Resumos estatísticos
- Relatórios de qualidade

---

**Nota**: Esta pasta contém dados processados prontos para análise. Para dados brutos, consulte `dados_sismologicos/Eventos/`.
