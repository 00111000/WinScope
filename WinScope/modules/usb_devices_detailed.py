import wmi

def listar_usb_detalhado():
    print("[*] Listando dispositivos USB conectados...\n")
    c = wmi.WMI()
    for dispositivo in c.Win32_USBHub():
        print(f"Nome: {dispositivo.Name}")
        print(f"DeviceID: {dispositivo.DeviceID}")
        print(f"Status: {dispositivo.Status}")
        print(f"PNPDeviceID: {dispositivo.PNPDeviceID}")
        print("-" * 40)

    input("\nPressione Enter para voltar ao menu...")