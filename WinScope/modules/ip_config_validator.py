import subprocess

def validar_ip():
    print("\n--- Configurações TCP/IP ---\n")
    resultado = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
    print(resultado.stdout)
    input("\nPressione Enter para voltar ao menu...")
