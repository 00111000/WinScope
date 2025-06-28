import wmi
import platform

def listar_usb():
    if platform.system() != "Windows":
        print("[!] Este script adaptado é apenas para Windows.")
        return

    print("\n--- Dispositivos USB conectados ---\n")
    w = wmi.WMI()
    for usb in w.Win32_USBHub():
        print(f"Nome: {usb.Name}")
        print(f"DeviceID: {usb.DeviceID}")
        print(f"Status: {usb.Status}\n")
