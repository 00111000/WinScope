# 🛠️ WinScope - Diagnóstico de Hardware e Sistema

**WinScope** é uma ferramenta modular desenvolvida para diagnóstico técnico em estações Windows. Ideal para laboratórios, suporte técnico, manutenção e auditoria de hardware.  
Fornece informações sobre discos, USBs, rede local, desempenho, processos, drivers e muito mais.

---

## 💻 Funcionalidades

* 🔢 Monitoramento de uso do disco (`monitor_disk_usage`)
* 🔢 Verificação de drivers instalados (`check_drivers`)
* 🔢 Listagem de dispositivos USB conectados (`usb_devices_detailed`)
* 🔢 Análise de processos suspeitos (`suspicious_processes`)
* 🔢 Teste de velocidade do disco (`disk_speed_test`)
* 🔢 Scanner de redes Wi-Fi próximas (`wifi_scanner`)
* 🔢 Validação de IPs e adaptadores (`ip_config_validator`)
* 🔢 Verificação de serviços essenciais do Windows (`check_windows_services`)

---

## 📦 Requisitos

- Python 3.8+
- Sistema: Windows 10 ou superior
- Execução como **administrador** em funções de sistema
- Instale as dependências com:

```bash
pip install -r requirements.txt
```

📁 Estrutura
```
techaudit/
├── main.py                  # Menu principal
├── cogs/
│   ├── monitor_disk_usage.py
│   ├── check_drivers.py
│   ├── usb_devices_detailed.py
│   ├── suspicious_processes.py
│   ├── disk_speed_test.py
│   ├── wifi_scanner.py
│   ├── ip_config_validator.py
│   └── check_windows_services.py
├── requirements.txt
└── app.bat
```

🧪 Como usar
```
Basta clicar no app.bat que ele inicia a ferramenta.
```

⚠️ Finalidade educacional
Projeto voltado para fins didáticos, auditoria técnica e suporte em ambientes controlados.

🎓 Autor
Criado por [00111000], estudante de Técnico em Redes de Computadores.
