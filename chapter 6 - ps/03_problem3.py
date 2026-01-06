a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

message = input("Entre your comment: ")

if((a in message) or (b in message) or (c in message) or (d in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
