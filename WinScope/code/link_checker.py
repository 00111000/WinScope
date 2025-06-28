# link_checker.py (versão para Windows com psutil)
import psutil
import platform

def verificar_link():
    if platform.system() != "Windows":
        print("[!] Este script adaptado é apenas para Windows.")
        return

    print("\n--- Verificando interfaces de rede ---\n")
    interfaces = psutil.net_if_stats()
    for nome, stats in interfaces.items():
        status = "Conectado" if stats.isup else "Desconectado"
        velocidade = f"{stats.speed} Mbps" if stats.speed > 0 else "Desconhecida"
        print(f"Interface: {nome} | Status: {status} | Velocidade: {velocidade}")
