import re

filenames = ["Chapter-5_cleaned", "Chapter-6_cleaned", "Chapter-7_cleaned"]

for i in range(len(filenames)):

    filename = "New Revised Standard version/" + filenames[i] + ".txt"
    data = ""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        f.close()
        

    data = data.replace("\n", " ")
    data = re.sub(r'\s+', " ", data)
    data = data.lower()

    data = re.sub('[^a-zA-Z0-9\n\.]', ' ', data)
    data = re.sub(r'\s+', " ", data)
    sentences = re.split("[0-9]+", data)
    sentences = [s.strip() for s in sentences]

    output_file = "New Revised Standard version/" + filenames[i] + ".csv"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("verse")
        f.write("\n")
        for i in range(len(sentences)):
            f.write(sentences[i])
            f.write("\n")
        f.close()

    import pandas as pd

    file = pd.read_csv(output_file)
    header_list = ['verse']
    file.to_csv(output_file, header = header_list, index=False)
