# Set
Music_Club = {"Taylor Swift", "BTS", "Adele", "Ed Sheeran", "Billie Eilish","Sabrina Carpenter","Waii Panyarisa"}
Colour = {"Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink"}
Fruit = {"Apple", "Banana", "Mango", "Watermelon", "Papaya", "Kiwi", "Cherry" , "Orange"}
Military_Club = {"Prayut Chan-o-cha", "Prawit Wongsuwan", "Anupong Paochinda", "Chalermchai Sitthisart", "Apirat Kongsompong"}
#print(Music_Club)
#print(f"Names{Music_Club}")
#print(f"Names{Music_Club}{Colour}{Fruit}")

# Union
All_Members = Music_Club | Colour | Fruit
#print(f"Names {All_Members}")

# Intersection
Colour_Fruit = Colour & Fruit
#print(f"Names {Colour_Fruit}")

# Difference
Dif_Colour_Fruit = Colour - Fruit
#print(f"Names {Dif_Colour_Fruit}")

#Symmetric Difference
Sym_Dif_Colour_Fruit = Colour ^ Fruit
print(f"Names {Sym_Dif_Colour_Fruit}")

# ตรวจสอบสมาชิกใน Set
Set_Check = {"Orange","Banana"}
if Set_Check.issubset(Music_Club):
    print("Yes")
else :
    print("No")
if Set_Check.issubset(Fruit):
    print("Yes")
else :
    print("No")           