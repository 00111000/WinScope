from modules import (
    monitor_disk_usage,
    check_drivers,
    usb_devices_detailed,
    suspicious_processes,
    disk_speed_test,
    wifi_scanner,
    ip_config_validator,
    check_windows_services
)

MENU_BANNER = """
           .---.                       .--.--.                                           
          /. ./|  ,--,                /  /    '.                    ,-.----.             
      .--'.  ' ;,--.'|         ,---, |  :  /`. /             ,---.  \    /  \            
     /__./ \ : ||  |,      ,-+-. /  |;  |  |--`             '   ,'\ |   :    |           
 .--'.  '   \' .`--'_     ,--.'|'   ||  :  ;_       ,---.  /   /   ||   | .\ :   ,---.   
/___/ \ |    ' ',' ,'|   |   |  ,"' | \  \    `.   /     \.   ; ,. :.   : |: |  /     \  
;   \  \;      :'  | |   |   | /  | |  `----.   \ /    / ''   | |: :|   |  \ : /    /  | 
 \   ;  `      ||  | :   |   | |  | |  __ \  \  |.    ' / '   | .; :|   : .  |.    ' / | 
  .   \    .\  ;'  : |__ |   | |  |/  /  /`--'  /'   ; :__|   :    |:     |`-''   ;   /| 
   \   \   ' \ ||  | '.'||   | |--'  '--'.     / '   | '.'|\   \  / :   : :   '   |  / | 
    :   '  |--" ;  :    ;|   |/        `--'---'  |   :    : `----'  |   | :   |   :    | 
     \   \ ;    |  ,   / '---'                    \   \  /          `---'.|    \   \  /  
      '---"      ---`-'                            `----'             `---`     `----'
"""

def menu():
    while True:
        try:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            print(MENU_BANNER)
            print("\n=== WinScope - Diagnóstico de Hardware e Rede ===\n")
            print("1. Monitorar uso do disco")
            print("2. Verificar drivers instalados")
            print("3. Listar dispositivos USB (detalhado)")
            print("4. Analisar processos suspeitos")
            print("5. Testar velocidade de leitura/gravação do disco")
            print("6. Listar redes Wi-Fi próximas")
            print("7. Validar configurações de IP")
            print("8. Verificar status de serviços do Windows")
            print("0. Sair")

            escolha = input("\nEscolha uma opção: ")

            if escolha == "1":
                monitor_disk_usage.monitorar_disco()
            elif escolha == "2":
                check_drivers.verificar_drivers()
            elif escolha == "3":
                usb_devices_detailed.listar_usb_detalhado()
            elif escolha == "4":
                suspicious_processes.analisar_processos()
            elif escolha == "5":
                disk_speed_test.teste_velocidade_disco()
            elif escolha == "6":
                wifi_scanner.scan_wifi()
            elif escolha == "7":
                ip_config_validator.validar_ip()
            elif escolha == "8":
                check_windows_services.verificar_servicos()
            elif escolha == "0":
                print("Encerrando...")
                break
            else:
                print("Opção inválida.")
                input("\nPressione Enter para continuar...")
        except Exception as e:
            print(f"\n[ERRO] Ocorreu um problema: {e}")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()
