#!/usr/bin/env python3

import argparse
import sys
import signal
import subprocess
from concurrent.futures import ThreadPoolExecutor

def def_handler(sig,frame):
    print("\n[!] Saliendo...")
    sys.exit(1)
    
signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP -> 192.168.1.1 / Rango IP -> 192.168.1.1-100")
    args = parser.parse_args()
    return args.target

def parse_targets(target_str):
    target_split = target_str.split(".")
    target_octets = '.'.join(target_split[:3])
    
    if len(target_split) == 4:
        if "-" in target_split[3]:
            start, end = target_split[3].split("-")
            return [f"{target_octets}.{i}" for i in range(int(start), int(end) + 1)]
        else:
            return [target_str]
    else:
        print(f"\n[!] El target propocionado esta mal")
    
def host_discovery(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.DEVNULL, timeout=1)
        if ping.returncode == 0:
            print(f"[+] El host -> {target} esta abierto")
    except subprocess.TimeoutExpired:
        pass

def main():
    args = get_arguments()
    targets = parse_targets(args)
    
    print(f"\n[+] Host activos en la red: ")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(host_discovery, targets)
    
if __name__ == '__main__':
    main()
    