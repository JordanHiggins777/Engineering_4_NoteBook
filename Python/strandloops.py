txt = input("Enter a sentence: ")

for letter in txt:
	print (letter)

txt = txt.replace(" ", "-")

txt = txt.split("-")
