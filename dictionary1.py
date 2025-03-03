def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😀",
        ":(" : "😩"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("Enter your message or type 'exit' to quit: ")
while True:
    if message == "" :
        message = input("Enter your message or type 'exit' to quit: ")
    elif message.lower() == "exit":
        print("Goodbye ✌")
        break
    else:
        print(emoji_converter(message))
        break




