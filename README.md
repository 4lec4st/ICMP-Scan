# Host Discovery - ICMP Scan

## Descripción
Este script realiza un escaneo rápido de hosts en una red local mediante el comando "ping". Detecta dispositivos activos dentro de un rango de direcciones IP especificado.

## Requisitos
- Python 3.x
- Permisos de administrador (para enviar paquetes ICMP)

## Instalación
1. Clona el repositorio o guarda el script en tu máquina.
2. Asegúrate de que el script tenga permisos de ejecución:
```bash
chmod +x script.py
```

## Uso
Ejecuta el script con la dirección IP o el rango de IPs a escanear:
```bash
python3 script.py -t 192.168.1.1
```
O escanea un rango de IPs:
```bash
python3 script.py -t 192.168.1.1-100
```

### Salida Esperada
- Lista los hosts activos en la red:
```
[+] El host -> 192.168.1.1 esta abierto
[+] El host -> 192.168.1.2 esta abierto
```
- Si se presiona Ctrl+C durante la ejecución, se muestra:
```
[!] Saliendo...
```
