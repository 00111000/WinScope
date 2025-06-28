import subprocess

def scan_wifi():
    print("\n--- Redes Wi-Fi Próximas ---\n")
    try:
        resultado = subprocess.run(
            ['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'],
            capture_output=True,
            text=True
        )
        print(resultado.stdout)
    except Exception as e:
        print(f"[!] Erro ao executar o comando: {e}")

    input("\nPressione Enter para voltar ao menu...")
