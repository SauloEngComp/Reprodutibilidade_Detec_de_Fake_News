import pickle
from pathlib import Path

# --- Configuração ---
RESULTS_DIR = Path('Results')
EMBEDDINGS_DIR = RESULTS_DIR / 'Embeddings'
METRICS_DIR = RESULTS_DIR / 'Metrics'
EMBEDDINGS_FILE = EMBEDDINGS_DIR / 'embeddings.pkl'
RESULTS_FILE = METRICS_DIR / 'results.pkl'

print("Iniciando limpeza dos arquivos .pkl...")

# --- 1. Limpando embeddings.pkl ---
try:
    with open(EMBEDDINGS_FILE, 'rb') as file:
        embeddings = pickle.load(file)

    if 'BART' in embeddings:
        print("Encontrado 'BART' em embeddings.pkl. Removendo...")
        del embeddings['BART']
        
        with open(EMBEDDINGS_FILE, 'wb') as file:
            pickle.dump(embeddings, file)
        print("'BART' removido de embeddings.pkl com sucesso.")
    else:
        print("'BART' não encontrado em embeddings.pkl (provavelmente já limpo).")

except FileNotFoundError:
    print(f"AVISO: {EMBEDDINGS_FILE} não encontrado. Pulando.")
except Exception as e:
    print(f"Erro ao processar {EMBEDDINGS_FILE}: {e}")


# --- 2. Limpando results.pkl ---
try:
    with open(RESULTS_FILE, 'rb') as file:
        results = pickle.load(file)

    if 'BART' in results:
        print("\nEncontrado 'BART' em results.pkl. Removendo...")
        del results['BART']
        
        with open(RESULTS_FILE, 'wb') as file:
            pickle.dump(results, file)
        print("'BART' removido de results.pkl com sucesso.")
    else:
        print("\n'BART' não encontrado em results.pkl (provavelmente já limpo).")

except FileNotFoundError:
    print(f"AVISO: {RESULTS_FILE} não encontrado. Pulando.")
except Exception as e:
    print(f"Erro ao processar {RESULTS_FILE}: {e}")

print("\nLimpeza concluída!")