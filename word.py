def main():
    word = input("Sentance: ")

    sentance = ""
    # Split ThisIsASentance into This is a sentance
    for char in word:
        if char.isupper() and sentance != "":
            sentance += " "
            char = char.lower()
        sentance += char
    
    sentance += "."

        

    print(sentance)
        


if __name__ == "__main__":
    main()