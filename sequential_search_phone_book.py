def find_phone_number(name, phone_book):
    for entry in phone_book:
        if entry[0] == name:
            return entry[1]
    return None

# Buku telepon
phone_book = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

# Cari nomor telepon Jane
name = "Jane Smith"
phone_number = find_phone_number(name, phone_book)

# Tampilkan nomor telepon Jane
if phone_number:
    print("Nomor telepon", name, "adalah", phone_number)
else:
    print("Tidak dapat menemukan nomor telepon", name)