import os
import glob
from lxml import etree

TEI_FOLDER = "tei"
OUTPUT_FILE = "resultados/links_per_article.txt"

with open(OUTPUT_FILE, "w") as out:
    for file in glob.glob(os.path.join(TEI_FOLDER, "*.xml")):
        tree = etree.parse(file)
        root = tree.getroot()
        ns = {"tei": "http://www.tei-c.org/ns/1.0"}

        paper_name = os.path.basename(file)
        out.write(f"=== {paper_name} ===\n")

        # Extraer todos los target de <ref> y <ptr>
        links = root.xpath("//tei:ref/@target | //tei:ptr/@target", namespaces=ns)

        # Filtrar solo los que empiezan con http/https
        links = [l for l in links if l.startswith("http") and "grobid" not in l.lower()]

        if links:
            for link in links:
                out.write(link + "\n")
        else:
            out.write("No links found\n")
        
        out.write("\n")

