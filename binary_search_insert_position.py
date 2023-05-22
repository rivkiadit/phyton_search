def search_insert_position(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Data dan target
data = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Cari posisi sisipan elemen
insert_position = search_insert_position(data, target)

# Tampilkan hasil
print("Elemen", target, "dapat disisipkan pada indeks", insert_position, "untuk menjaga daftar tetap terurut.")