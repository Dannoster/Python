import os
from pdf2image import convert_from_path

for i in range(1,7):
    dir = f"/Users/daniil/Downloads/3/2_ex_new/graph_{i}"
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            path_of_pdf = os.path.join(dir, file)
            pages = convert_from_path(path_of_pdf, use_cropbox=True)
            for page in pages:
                new_file_dir = f'{dir}/{file}.jpg'.replace(".pdf",'')
                page.save(new_file_dir, 'JPEG')
