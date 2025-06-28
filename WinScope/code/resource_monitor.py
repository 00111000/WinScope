import psutil

def monitorar_uso():
    print("\n--- Monitorando uso da CPU e RAM ---\n")
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        print(f"Uso da CPU: {cpu}%")
        print(f"Uso da RAM: {ram}%")
    except Exception as e:
        print(f"Erro ao monitorar recursos: {e}")
