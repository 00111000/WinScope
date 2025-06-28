import wmi

def verificar_drivers():
    print("[*] Verificando drivers instalados...\n")
    c = wmi.WMI()
    for driver in c.Win32_PnPSignedDriver():
        print(f"Dispositivo: {driver.DeviceName}")
        print(f"Versão do Driver: {driver.DriverVersion}")
        print(f"Fabricante: {driver.Manufacturer}")
        print(f"Data do Driver: {driver.DriverDate}")
        print("-" * 40)

    input("\nPressione Enter para voltar ao menu...")