import platform
import psutil
import cpuinfo

def mostrar_info():
    print("\n--- Informações do Sistema ---\n")
    print("Sistema Operacional:", platform.system(), platform.release())
    print("Arquitetura:", platform.machine())
    print("Processador:", cpuinfo.get_cpu_info()['brand_raw'])
    print("Núcleos (físicos/lógicos):", psutil.cpu_count(logical=False), "/", psutil.cpu_count())
    print("Memória RAM Total:", round(psutil.virtual_memory().total / (1024**3), 2), "GB")
    print("Discos:")
    for disco in psutil.disk_partitions():
        uso = psutil.disk_usage(disco.mountpoint)
        print(f"- {disco.device} ({disco.mountpoint}): {round(uso.total / (1024**3), 2)} GB totais")
