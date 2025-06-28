import psutil

def analisar_processos():
    print("[*] Analisando processos suspeitos...\n")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            name = proc.info['name'].lower()
            if any(suspeito in name for suspeito in ['powershell', 'cmd', 'wmic', 'regsvr32', 'mshta']):
                print(f"⚠️ Processo suspeito: {proc.info['name']} (PID: {proc.info['pid']}) - Usuário: {proc.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    input("\nPressione Enter para voltar ao menu...")