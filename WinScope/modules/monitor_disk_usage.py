import psutil

def monitorar_disco():
    print("[*] Monitorando uso de disco...\n")
    uso = psutil.disk_usage('/')
    print(f"Total: {uso.total / (1024**3):.2f} GB")
    print(f"Usado: {uso.used / (1024**3):.2f} GB")
    print(f"Disponível: {uso.free / (1024**3):.2f} GB")
    print(f"Porcentagem de uso: {uso.percent}%")

    input("\nPressione Enter para voltar ao menu...")