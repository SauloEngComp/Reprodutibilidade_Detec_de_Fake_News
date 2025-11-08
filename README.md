# Reprodutibilidade_Detec_de_Fake_News
Reprodução do artigo "Detecção de Fake News em Português" (Vieira et al., 2025), comparando embeddings e classificadores (MLP, RFC, SVC).
# Reprodução: Detecção de Fake News com Embeddings em Português

Este repositório contém o código e os resultados da reprodução do artigo **"Detecção de Fake News em Português: Análise Comparativa entre Métodos de Representação em Português, Inglês e Multilíngues"** (Vieira et al., 2025)[cite: 5, 6].
O objetivo deste projeto, desenvolvido para a disciplina de Aprendizagem de Máquina [cite: 376], é replicar a metodologia de comparação de diferentes embeddings de linguagem (como BERTimbau, ROBERTA, TUCANO, etc.) [cite: 13, 19, 32] na tarefa de detecção de fake news. O estudo utiliza os classificadores MLP, RFC e SVC [cite: 11] sobre o dataset FAKE.BR CORPUS[cite: 17, 37].

## 🚀 Requisitos e Instalação

Para executar este projeto, você precisará do Python 3.x e das bibliotecas listadas no `requirements.txt`.

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Crie um ambiente virtual (venv):**
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * No Windows (CMD/PowerShell):
        ```bash
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    [cite_start]O arquivo `requirements.txt` [cite: 375] contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

      ⚡ Executando o Experimento Principal (`compare_embbedings.py`)

O script `compare_embbedings.py` é o orquestrador principal. Ele baixa os dados, calcula os embeddings, treina os classificadores e salva os resultados.

1.  **Configure a Fração dos Dados:**
    * Abra o arquivo `compare_embbedings.py` em um editor de código.
    * [cite_start]Localize a função `load_data()`[cite: 2, 86].
    * Ajuste a variável `fracao` para o percentual de dados que deseja usar (ex: `fracao = 0.8` para 80% ou `fracao = 0.1` para 10%).

2.  **Execute o Script:**
    Com o `venv` ativado, execute:
    ```bash
    python compare_embbedings.py
    ```

3.  **Acompanhe o Processo:**
    [cite_start]O script foi projetado para "pular" o trabalho que já foi feito[cite: 2, 192, 217]. Se ele for interrompido, você pode simplesmente executá-lo novamente, e ele continuará de onde parou.

4.  **Resultados:**
    O script irá criar/atualizar a pasta `Results/`. [cite_start]Os resultados finais de métricas estarão em `Results/Metrics/results.csv` [cite: 2, 237] [cite_start]e os embeddings brutos em `Results/Embeddings/embeddings.pkl`[cite: 2, 214].

       🛠️ Ferramentas Adicionais e Solução de Problemas

Estes scripts ajudam a gerenciar, auditar e corrigir os resultados do experimento.

### 1. Verificar o Tamanho dos Dados (Script `verificar.py`)

Se você não tem certeza de quantos dados (`embeddings.pkl`) usou em uma execução anterior, este script audita os arquivos.

* **Uso:**
    1.  (Opcional) Edite o script para apontar para a pasta `Results` correta (ex: `RESULTS_DIR = Path('Results_80_porcento')`).
    2.  Execute:
        ```bash
        python verificar.py
        ```
* **Saída:** O script informará o "VEREDITO" de quantos dados (ex: 5760 amostras, 80%) foram usados para cada embedding.

---

### 2. Corrigir uma Execução Corrompida (`remove_bart.py`)

Se o script principal foi interrompido (ex: processou o BART com 8% dos dados e o resto com 80%), criando um arquivo `.pkl` inconsistente.

* **Uso:**
    1.  (Opcional) Edite o script para remover um embedding diferente (o padrão é 'BART').
    2.  Execute o script de limpeza **PRIMEIRO**:
        ```bash
        python remove_bart.py
        ```
    3.  Configure o `compare_embbedings.py` para a fração correta (ex: 80%).
    4.  Rode o script principal (`python compare_embbedings.py`). Ele irá pular os modelos existentes e rodar **apenas** o que foi removido, garantindo consistência.

---

### 3. Gerar CSV Manualmente (`to_csv.py`)

[cite_start]Se o script `compare_embbedings.py` travou *depois* de salvar os `results.pkl` [cite: 1, 14][cite_start], mas *antes* de conseguir criar o `results.csv`[cite: 1, 29].

* **Uso:**
    1.  Execute:
        ```bash
        python to_csv.py
        ```
* **Saída:** O script irá ler os arquivos `.pkl` e gerar o `results.csv` na pasta `Results/Metrics/`.

## 📚 Artigo Original (Referência)

Este trabalho é uma reprodução de:
* Vieira, C. B., Souza, J. V. S., & Cavalcanti, G. D. C. (2025). *Detecção de Fake News em Português: Análise Comparativa entre Métodos de Representação em Português, Inglês e Multilíngues*. Anais do [Nome do Evento da SBC].
* Saulo Gomes Martins / Universidade Federal do Sul e Sudeste do Pará
