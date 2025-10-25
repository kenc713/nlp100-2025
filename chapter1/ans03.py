given_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = given_string.split()
ans = [len(word.strip(".,")) for word in words]
print(ans)
