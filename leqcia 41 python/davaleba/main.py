import os
def Cls():
    os.system("cls")

Cls()

my_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# my_text = "ab ab aa 1 2 3"

#ფაილში ჩაწერა
file = open("text.txt", "w", encoding="utf-8")
file.write(my_text)
file.close()

#ფაილიდან წაკითხვა/დაბეჭდვა
file = open("text.txt", 'r', encoding="utf-8")
my_text = file.read()
file.close()
print(my_text)

#ახალ ხაზზე გადატანა
print("\n"*1)
print("_"*70)
print("\n"*1)

#სიმბოლოების რაოდენობა
print("სიმბოლოების რაოდენობა = ", len(my_text))

# სიტყვების რაოდენობა
my_text_splite = my_text.split()
len_my_text_split = len(my_text_splite)
print("სიტყვების რაოდენობა = ", len_my_text_split)

#განსხვავებული სიტყვების რაოდენობა
my_text_set = set(my_text_splite)
len_my_text_set = len(my_text_set)
print("განსხვავებული სიტყვების რაოდენობა = ", len_my_text_set)

#სიტყვაში სიმბოლოების საშუალო რაოდენობა
result = 0
for i in my_text_splite:
    result += len(i)
    # print(len(i))
result /= len_my_text_split
print("სიტყვაში სიმბოლოების საშუალო რაოდენობა = ", result)
