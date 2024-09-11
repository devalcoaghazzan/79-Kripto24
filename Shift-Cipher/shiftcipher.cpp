/*
    Nama        : Devalco Aghazzan Muslion
    NPM         : 140810220079
    Kelas       : A
    Program     : Shift Cipher
    Tugas       : Tugas Pertemuan 2 Praktikum Kriptografi 
*/  

#include <iostream>
#include <string>
using namespace std;

// Fungsi untuk mengenkripsi teks menggunakan Shift Cipher
string encrypt(string text, int shift) {
    string result = "";
    shift = shift % 26; // Mengambil nilai shift modulo 26

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Proses pengubahan karakter hanya jika karakter adalah huruf
        if (isalpha(ch)) {
            char offset = isupper(ch) ? 'A' : 'a';
            ch = (ch - offset + shift) % 26 + offset;
        }

        result += ch;
    }

    return result;
}

// Fungsi untuk mendekripsi teks yang terenkripsi
string decrypt(string text, int shift) {
    return encrypt(text, 26 - (shift % 26)); // Mengambil nilai shift modulo 26
}

int main() {
    string text;
    int shift;

    // Meminta input dari pengguna
    cout << "Masukkan teks yang akan dienkripsi: ";
    getline(cin, text);

    cout << "Masukkan besar pergeseran (K): ";
    cin >> shift;

    // Mengenkripsi teks
    string encrypted = encrypt(text, shift);
    cout << "Hasil Enkripsi: " << encrypted << endl;

    // Mendekripsi teks
    string decrypted = decrypt(encrypted, shift);
    cout << "Hasil Dekripsi: " << decrypted << endl;

    return 0;
}
