def binary_search(dictionary, target_word):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        if dictionary[mid][0] == target_word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < target_word:
            left = mid + 1
        else:
            right = mid - 1

    return "Kata tidak ditemukan dalam kamus."

# Kamus dalam bentuk list berisi tuple (kata, definisi)
kamus = [
    ("Apple", "Buah Apel"),
    ("Banana", "Buah Pisang"),
    ("Cat", "Kucing"),
    ("Duck", "Bebek"),
    ("Elephant", "Gajah")
]

# Contoh penggunaan binary search untuk mencari definisi kata
kata_dicari = input("Masukkan Kata Yang Ingin Dicari ? : ")
definisi = binary_search(kamus, kata_dicari)
print(f"Definisi dari kata '{kata_dicari}': {definisi}")