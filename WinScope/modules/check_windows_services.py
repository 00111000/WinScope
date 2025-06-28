import wmi

def verificar_servicos():
    print("\n--- Status de Serviços do Windows ---\n")
    w = wmi.WMI()
    servicos_essenciais = ['Dhcp', 'Dnscache', 'MpsSvc']  # DHCP, DNS Client, Firewall
    for servico in servicos_essenciais:
        for s in w.Win32_Service(Name=servico):
            status = "Rodando" if s.State == "Running" else "Parado"
            print(f"{s.DisplayName} ({servico}): {status}")
            
    input("\nPressione Enter para voltar ao menu...")