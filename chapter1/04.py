given_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = given_string.split()
index_set = {1, 5, 6, 7, 8, 9, 15, 16, 19}
ans_dict = {}
for i in range(len(words)):
    if i + 1 in index_set:
        ans_dict[words[i][0]] = i + 1
    else:
        ans_dict[words[i][0:2]] = i + 1
print(ans_dict)