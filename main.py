import easyocr

def text_recognition(path, lang):
    reader = easyocr.Reader(lang)
    try:
        result = reader.readtext(path, detail=0, paragraph=True) # can set any parameters
    except Exception as er:
        print("Reading error: ", er)
    return result

def file_work(path_, lang=["en"], new_file_name=None):
    new_file_name = f'text_reg/{path_.split("/")[1].split(".")[0]}.txt' if new_file_name == None else new_file_name

    with open(new_file_name, 'w') as file:
        result = text_recognition(path=path_, lang=lang)
        for a in result:
            try:
                file.write(a + "\n")
            except:
                print("Error writing: " + a)

    print(result)

def main():
    #file_work("pictures/picture1.png", ["en", "ru"], "text_reg/test2.txt")
    file_work("pictures/picture3.png", ["en"])

if __name__ == "__main__":
    main()