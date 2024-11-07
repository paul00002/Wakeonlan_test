import socket
import struct

def send_wol(mac_address):
    # Converte l'indirizzo MAC in un formato corretto
    mac_address = mac_address.replace(":", "").replace("-", "")
    
    # Crea il magic packet (16 ripetizioni dell'indirizzo MAC precedute da FF FF FF FF FF FF)
    magic_packet = bytes.fromhex("FF" * 6 + mac_address * 16)
    
    # Crea un socket UDP per l'invio in broadcast
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Abilita l'invio in broadcast
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        # Specifica l'indirizzo IP di broadcast della tua rete (es. 192.168.1.255)
        broadcast_address = '192.168.1.255'  # Cambia con il tuo IP di broadcast
        
        # Invia il pacchetto al broadcast IP e alla porta 9
        sock.sendto(magic_packet, (broadcast_address, 9))
    
    print("Pacchetto WoL inviato in broadcast all'indirizzo MAC:", mac_address)

# Esempio di utilizzo
mac_address = "B4:2E:99:47:5B:46"  # Sostituisci con l'indirizzo MAC del dispositivo
send_wol(mac_address)
