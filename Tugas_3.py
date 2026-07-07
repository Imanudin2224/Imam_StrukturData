# teknik duplikan list

x = ["dadang", "wowok", "cecep"]
print(f"x awal : {x}")
print("-" * 40)

y = x
print("1. y = x -> referensi")
x[0] = "cecep"
print(f"x : {x}")
print(f"y : {y}") 
print(f"alamat x : {hex(id(x))}")
print(f"alamat y : {hex(id(y))}")
print("-" * 40)

z = x.copy()
w = x[:]
d = copy.deepcopy(x)

x[1] = "budi"
x[2] = "andi"

print("2. Setelah x diubah lagi")
print(f"x : {x}")
print(f"z = x.copy() : {z}") 
print(f"w = x[:] : {w}") 
print(f"d = deepcopy(x) : {d}") 
print("-" * 40)

print("Alamat Memory:")
print(f"alamat x : {hex(id(x))}")
print(f"alamat z : {hex(id(z))}")
print(f"alamat w : {hex(id(w))}")
print(f"alamat d : {hex(id(d))}")