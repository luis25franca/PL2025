text = input("Input string \n")

# Example string "Lorem 1psum dolor sit 2amet, OFF consectetur 1200000adipiscing = elit. oN Nunc pharetra 3pellentesque 4 augu10e,  =semper sagittis offset ornare 100at. OFF Nulla sapien 30lorem =, mollis ON vel 2ultricies =ut, mollis."

accumulator = 0
i = 0
active = True
while i < len(text):
    if text[i].isdigit() and active == True:
        num = text[i]
        i+=1
        while(text[i].isdigit() and i < len(text)):
            num += text[i]
            i += 1
        accumulator += int(num)
            
    if text[i].lower() == "o" and not text[i-1].isalpha():
        if text[i+1].lower() == "f" and text[i+2].lower() == "f" and not text[i+3].isalpha():
            active = False
            i+=3
        if text[i+1].lower() == "n"  and not text[i+2].isalpha():
            active = True
            i+=2
    if text[i] == "=":
        print(accumulator)
    i += 1