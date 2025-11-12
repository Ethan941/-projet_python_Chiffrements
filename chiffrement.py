def chiffre_cesar(text, key):#deffiniton de la fonction text + la clé
    crypted_text =''#ont crypt le text

    for char in text:#char élément de la liste  text =la liste général
        crypted_text += chr(ord(char) + key)#ord = le nuémero de la place dans la liste

    return crypted_text

print(chiffre_cesar("ethan", 4))

