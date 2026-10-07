from db import tampilkan_aset_db

data = tampilkan_aset_db()

for item in data:
    print(item)