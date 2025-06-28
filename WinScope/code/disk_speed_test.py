import time
import os

def teste_velocidade_disco():
    print("\n--- Teste de Velocidade do Disco ---\n")
    tamanho = 50 * 1024 * 1024  # 50MB
    arquivo_teste = "teste_velocidade.tmp"

    # Teste de escrita
    inicio = time.time()
    with open(arquivo_teste, 'wb') as f:
        f.write(os.urandom(tamanho))
    fim = time.time()
    escrita = tamanho / (fim - inicio) / (1024 * 1024)  # MB/s
    print(f"Velocidade de escrita: {escrita:.2f} MB/s")

    # Teste de leitura
    inicio = time.time()
    with open(arquivo_teste, 'rb') as f:
        f.read()
    fim = time.time()
    leitura = tamanho / (fim - inicio) / (1024 * 1024)
    print(f"Velocidade de leitura: {leitura:.2f} MB/s")

    os.remove(arquivo_teste)
    input("\nPressione Enter para voltar ao menu...")
