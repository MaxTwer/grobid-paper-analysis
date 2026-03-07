#!/bin/bash
set -e


echo "Limpiando carpeta tei"
rm -f tei/*

echo "Generando XMLs"
bash proceso.sh

echo "Generando nube"
python3 keyword_cloud.py

echo "Contando figuras por artículo"
python3 figures_per_article.py

echo "Extrayendo links por articulo"
python3 links_per_article.py

echo "Fin"
