import os
import glob
from lxml import etree
import matplotlib.pyplot as plt
import pandas as pd

TEI_FOLDER = "tei"

figure_counts = {}

for file in glob.glob(os.path.join(TEI_FOLDER, "*.xml")):
    tree = etree.parse(file)
    root = tree.getroot()
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}

    paper_name = os.path.basename(file)

    # Contar todas las figuras (incluye tablas)
    figures = root.xpath("//tei:figure", namespaces=ns)
    figure_counts[paper_name] = len(figures)

# Crear DataFrame para graficar
df = pd.DataFrame.from_dict(figure_counts, orient='index', columns=['num_figures'])
df = df.sort_index()  # orden alfabético

# Crear gráfico de barras
plt.figure(figsize=(12,6))
bars = plt.bar(df.index, df['num_figures'], color='skyblue')
plt.xlabel("Article")
plt.ylabel("Number of Figures")
plt.title("Number of Figures per Article")
plt.xticks(rotation=45, ha='right')

# Etiquetas encima de las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(int(height)),
             ha='center', va='bottom')

plt.tight_layout()
plt.savefig("resultados/figures_per_article.png")
plt.show()
