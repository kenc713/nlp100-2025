string_a: str = "パトカー"
string_b: str = "タクシー"
length = len(string_a)

result: str = ""
for i in range(length):
    result += string_a[i] + string_b[i]
print(result)