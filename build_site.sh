#!/bin/bash

# Script para gerar site estático com Voilà

echo "🔄 Instalando dependências..."
pip install voila jupyter ipywidgets pandas numpy matplotlib seaborn

echo "🏗️ Gerando site estático com Voilà..."
voila --template=material --no-browser webapp_analysis.ipynb --output_dir=docs --VoilaConfiguration.file_extension='.html'

echo "📁 Copiando index.html para docs/"
cp index.html docs/

echo "✅ Site gerado em ./docs/"
echo "🌐 Para testar localmente, execute: cd docs && python -m http.server 8000"
