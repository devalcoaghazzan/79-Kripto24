#
#    Nama        : Devalco Aghazzan Muslion
#    NPM         : 140810220079
#    Kelas       : A
#    Program     : Vigenere Cipher
#    Tugas       : Tugas Pertemuan 5 Praktikum Kriptografi 
#

import string

# Fungsi untuk mengenkripsi pesan dengan Vigenère cipher
def vigenere_encrypt(text, key):
    result = []
    key_length = len(key)
    key_index = 0

    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            key_char = ord(key[key_index % key_length].lower()) - ord('a')
            result.append(chr((ord(ch) - base + key_char) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)

# Fungsi untuk mendekripsi pesan dengan Vigenère cipher
def vigenere_decrypt(text, key):
    result = []
    key_length = len(key)
    key_index = 0

    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            key_char = ord(key[key_index % key_length].lower()) - ord('a')
            result.append(chr((ord(ch) - base - key_char + 26) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)

# Fungsi untuk mencari kunci dari ciphertext dan plaintext yang diketahui
def find_key_from_plaintext_and_ciphertext(plaintext, ciphertext):
    key = []
    length = len(plaintext)

    for i in range(length):
        if plaintext[i].isalpha() and ciphertext[i].isalpha():
            key_char = (ord(ciphertext[i].lower()) - ord(plaintext[i].lower()) + 26) % 26
            if plaintext[i].islower():
                key.append(chr(key_char + ord('a')))
            else:
                key.append(chr(key_char + ord('A')))
        else:
            key.append(' ')  # Jika karakter bukan huruf, tambahkan spasi

    return ''.join(key)

def main():
    while True:
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari kunci dari ciphertext dan plaintext")
        print("4. Exit")
        choice = input("Pilih opsi: ")

        if choice == '4':
            print("\nTERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI!\n")
            break

        key = ""
        text = ""
        plaintext = ""
        ciphertext = ""
        
        if choice == '1':
            key = input("Masukkan kunci: ")
            text = input("Masukkan Plaintext: ")
            print("Hasil enkripsi:", vigenere_encrypt(text, key))
        elif choice == '2':
            key = input("Masukkan kunci: ")
            text = input("Masukkan Ciphertext: ")
            print("Hasil dekripsi:", vigenere_decrypt(text, key))
        elif choice == '3':
            plaintext = input("Masukkan plaintext: ")
            ciphertext = input("Masukkan ciphertext: ")
            if len(plaintext) != len(ciphertext):
                print("Panjang plaintext dan ciphertext harus sama!")
            else:
                print("Perkiraan kunci:", find_key_from_plaintext_and_ciphertext(plaintext, ciphertext))
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == '__main__':
    main()
