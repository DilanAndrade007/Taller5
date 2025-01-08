from elasticsearch import Elasticsearch
import pandas as pd
import re

# Conexión a Elasticsearch
def connect_elasticsearch():
    es = Elasticsearch("http://localhost:9200")
    if es.ping():
        print("Conectado a Elasticsearch")
        return es
    else:
        print("No se pudo conectar a Elasticsearch")
        exit()

# Crear un índice con esquema
def create_index(es, index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(
            index=index_name,
            body={
                "mappings": {
                    "properties": {
                        "Title": {"type": "text"},
                        "Plot": {"type": "text"},
                    }
                }
            },
        )
        print(f"Índice '{index_name}' creado.")
    else:
        print(f"Índice '{index_name}' ya existe.")

# Normalizar texto
def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

# Indexar documentos
def index_documents(es, index_name, data):
    for idx, row in data.iterrows():
        doc = {"Title": row["Title"], "Plot": row["Plot"]}
        es.index(index=index_name, id=idx, body=doc)
    print(f"Se han indexado {len(data)} documentos en el índice '{index_name}'.")

# Realizar búsqueda
def search_elasticsearch(es, query, index_name):
    response = es.search(
        index=index_name,
        body={
            "query": {
                "match": {
                    "Plot": query
                }
            }
        },
    )
    titles = [hit["_source"]["Title"] for hit in response["hits"]["hits"]]
    return titles

# Cargar datos del CSV
def load_data(file_path):
    dataset = pd.read_csv(file_path)
    data = dataset[["Title", "Plot"]].dropna()
    data["Plot"] = data["Plot"].apply(normalize_text)
    return data

# Validar documentos en el índice
def validate_documents(es, index_name):
    doc_count = es.count(index=index_name)["count"]
    print(f"El índice '{index_name}' contiene {doc_count} documentos.")

if __name__ == "__main__":
    # Configuración
    INDEX_NAME = "movies"
    FILE_PATH = "./wiki_movie_plots_deduped.csv"

    # 1. Conectar a Elasticsearch
    es = connect_elasticsearch()

    # 2. Crear índice
    create_index(es, INDEX_NAME)

    # 3. Cargar datos
    data = load_data(FILE_PATH)

    # 4. Indexar documentos
    index_documents(es, INDEX_NAME, data)

    # 5. Validar cantidad de documentos
    validate_documents(es, INDEX_NAME)

    # 6. Realizar consultas
    queries = ["time travel", "genetic engineering", "space adventure", "robot"]
    for query in queries:
        results = search_elasticsearch(es, query, INDEX_NAME)
        print(f"Resultados para '{query}': {results}")
