import pickle
import numpy as np
from pathlib import Path
import sys
import os

# --- ATENÇÃO AQUI ---
# Mantenha esta linha EXATAMENTE assim, 
# pois sua pasta se chama 'Results'
RESULTS_DIR = Path('Results')
# --------------------


# --- Construção do caminho ---
# Pega o diretório atual de onde o script está rodando
CWD = Path.cwd() 
EMBEDDINGS_FILE_PATH = CWD / RESULTS_DIR / 'Embeddings' / 'embeddings.pkl'


print("--- Verificador de Arquivos ---")
print(f"Diretório atual (CWD): {CWD}")
print(f"Pasta de Resultados (Relativa): {RESULTS_DIR}")
print(f"Tentando abrir o caminho ABSOLUTO:")
print(f"==> {EMBEDDINGS_FILE_PATH}") # Imprime o caminho completo
print("---------------------------------")


# --- Carregar o arquivo .pkl ---
try:
    with open(EMBEDDINGS_FILE_PATH, 'rb') as f:
        embeddings = pickle.load(f)
except FileNotFoundError:
    print(f"\nERRO: Arquivo não encontrado!")
    print(f"O Python NÃO conseguiu encontrar o arquivo no caminho exato acima.")
    print(f"Verifique se o caminho está 100% correto ou se há um erro de permissão.")
    sys.exit() # Encerra o script se não achar o arquivo
except Exception as e:
    print(f"\nERRO INESPERADO: {e}")
    sys.exit()

# --- Checar o tamanho (shape) de TODOS os embeddings ---
try:
    print("\n--- Verificando TODOS os embeddings encontrados ---")
    
    if not embeddings:
        print("ERRO: O arquivo .pkl está vazio.")
        sys.exit()

    overall_train_samples = -1
    overall_test_samples = -1
    is_consistent = True
    found_keys = list(embeddings.keys())

    for key in found_keys:
        data = embeddings[key]
        if 'X_train_embeddings' not in data or 'X_test_embeddings' not in data:
            print(f"\n⚠️ Atenção: Embedding '{key}' está incompleto (faltando arrays). Pulando.")
            continue
            
        train_shape = data['X_train_embeddings'].shape
        test_shape = data['X_test_embeddings'].shape
        
        train_samples = train_shape[0]
        test_samples = test_shape[0]
        
        print(f"\n  Embedding: '{key}'")
        print(f"    Amostras de Treino: {train_samples} (Formato: {train_shape})")
        print(f"    Amostras de Teste:  {test_samples} (Formato: {test_shape})")
        
        # Seta o valor na primeira iteração
        if overall_train_samples == -1:
            overall_train_samples = train_samples
            overall_test_samples = test_samples
        # Compara com as iterações seguintes
        elif overall_train_samples != train_samples or overall_test_samples != test_samples:
            is_consistent = False
            print(f"    🚨 ALERTA: Tamanho inconsistente! Este embedding diverge dos anteriores.")

    
    # --- Veredito Final ---
    print("\n--- VEREDITO GERAL ---")
    
    if not is_consistent:
        print(f"❌ ERRO: Os {len(found_keys)} embeddings no arquivo .pkl têm tamanhos INCONSISTENTES.")
        print("   Isso não deveria acontecer. Verifique como o arquivo foi gerado.")
    elif overall_train_samples == 7200 and overall_test_samples == 1800:
        print(f"✅ Todos os {len(found_keys)} embeddings foram gerados com 100% dos dados (7200/1800 amostras).")
    elif overall_train_samples == 720 and overall_test_samples == 180:
        print(f"✅ Todos os {len(found_keys)} embeddings foram gerados com 10% dos dados (720/180 amostras).")
    elif overall_train_samples == 576 and overall_test_samples == 144:
         print(f"✅ Todos os {len(found_keys)} embeddings foram gerados com 8% dos dados (576/144 amostras).")
    else:
        print(f"⚠️ Atenção: Todos os {len(found_keys)} embeddings foram gerados com um tamanho de dados não padrão:")
        print(f"   {overall_train_samples} amostras de treino / {overall_test_samples} amostras de teste.")

except Exception as e:
    print(f"\nERRO: O arquivo .pkl parece estar corrompido ou em um formato inesperado.")
    print(f"Detalhe: {e}")