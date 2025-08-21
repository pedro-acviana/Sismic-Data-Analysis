# 🌐 Configuração do GitHub Pages

Este arquivo contém as instruções para configurar o GitHub Pages e ativar a aplicação web.

## 📋 Passos para Configuração

### 1. Habilitar GitHub Pages
1. Vá para o repositório: https://github.com/pedro-acviana/Sismic-Data-Analysis
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Pages**
4. Em **Source**, selecione **GitHub Actions**
5. Clique em **Save**

### 2. Configurar Permissões
1. Ainda em **Settings**, vá para **Actions** → **General**
2. Em **Workflow permissions**, selecione:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. Clique em **Save**

### 3. Executar Deploy
1. Vá para a aba **Actions**
2. Clique em **Deploy Voilà App to GitHub Pages**
3. Clique em **Run workflow** → **Run workflow**
4. Aguarde o deploy completar (cerca de 2-3 minutos)

### 4. Acessar a Aplicação
Após o deploy, a aplicação estará disponível em:
**https://pedro-acviana.github.io/Sismic-Data-Analysis/**

## 🔧 Troubleshooting

### Problema: Workflow falha
**Solução**: Verifique se as permissões estão corretas em Settings → Actions

### Problema: Página não carrega
**Solução**: 
1. Aguarde alguns minutos após o deploy
2. Verifique se o GitHub Pages está ativo em Settings → Pages
3. Limpe o cache do navegador

### Problema: Upload de arquivo não funciona
**Solução**: 
1. Verifique se o arquivo é .csv
2. Confirme que tem as colunas obrigatórias
3. Tente com um arquivo menor primeiro

## 📊 Testando a Aplicação

### Arquivo de Teste
Você pode usar este CSV de exemplo para testar:

```csv
event_id,plane,max_magnitude,sensor,x_amplitude,y_amplitude,z_amplitude,source_file
71355,Plano_E,8.221685819782874e-06,SC.MAC11.00,5.311947914910374e-06,4.619219562237287e-06,4.247603760279728e-06,test.csv
71355,Plano_G,4.619101879705084e-06,BR.ESM09,3.3824204760572643e-06,1.8428907226242277e-06,2.5493308303766977e-06,test.csv
71360,Plano_E,7.19736468079588e-06,SC.MAC11.00,3.82248358313014e-06,3.903764876140116e-06,4.685221168406385e-06,test.csv
```

### Funcionalidades Esperadas
- ✅ Upload de arquivo CSV
- ✅ Validação automática do formato
- ✅ Cálculo de energia total
- ✅ Detecção de ruídos
- ✅ Gráficos interativos
- ✅ Download de resultados

## 🔄 Atualizações Futuras

Para atualizar a aplicação:
1. Faça alterações no `webapp_analysis.ipynb`
2. Commit e push para o repositório
3. O GitHub Actions fará deploy automaticamente

## 📱 Compatibilidade

A aplicação funciona em:
- ✅ Chrome/Edge (recomendado)
- ✅ Firefox
- ✅ Safari
- ✅ Dispositivos móveis (tablets/celulares)

---

*Aplicação desenvolvida com Jupyter, IPywidgets e GitHub Pages*
