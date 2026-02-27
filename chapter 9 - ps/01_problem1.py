f = open("poems.txt")

content = f.read()

if("twinkle" in content):
    print("The word twinkle is present in content")

else:
    print("The word Twinkle does not content in content")
f.close()