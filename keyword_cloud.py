import os
import glob
from lxml import etree
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import string

# Descargar stopwords si no lo has hecho
nltk.download('stopwords')

# Carpeta con los XML
TEI_FOLDER = "tei"

# Recoger todos los abstracts
abstract_texts = []

for file in glob.glob(os.path.join(TEI_FOLDER, "*.xml")):
    tree = etree.parse(file)
    root = tree.getroot()
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}

    abstract = root.xpath("//tei:abstract//text()", namespaces=ns)
    abstract_text = " ".join(abstract)
    abstract_texts.append(abstract_text)

# Concatenar todos los abstracts
full_text = " ".join(abstract_texts)

# Limpiar texto
full_text = full_text.lower()
translator = str.maketrans('', '', string.punctuation)
full_text = full_text.translate(translator)

# Eliminar stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in full_text.split() if w not in stop_words]
clean_text = " ".join(words)

# Crear la nube
wc = WordCloud(width=800, height=400, background_color="white").generate(clean_text)

# Mostrar y guardar
plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Keyword Cloud from Abstracts")
plt.savefig("resultados/keyword_cloud.png")
plt.show()
