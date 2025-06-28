import psutil
import time

def monitorar_rede():
    print("\n--- Monitorando velocidade da rede ---\n")
    try:
        io_antes = psutil.net_io_counters()
        time.sleep(1)
        io_depois = psutil.net_io_counters()

        bytes_recebidos = io_depois.bytes_recv - io_antes.bytes_recv
        bytes_enviados = io_depois.bytes_sent - io_antes.bytes_sent

        print(f"Download: {bytes_recebidos / 1024:.2f} KB/s")
        print(f"Upload: {bytes_enviados / 1024:.2f} KB/s")

    except Exception as e:
        print(f"Erro ao monitorar rede: {e}")
