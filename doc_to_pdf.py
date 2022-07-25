import os
import shutil
import docx2txt
import zipfile
from lxml import etree
from PIL import Image


def convert_png_to_jpg(image_path: str, output_dir):
    if not image_path.endswith(".png"):
        print(f"Not an png file: {image_path}")
        return
    im = Image.open(image_path)
    im = im.convert("RGB")
    file_name = image_path.split("/")[-1]
    im = im.save(os.path.join(output_dir, file_name.replace(".png", ".jpg")), quality=95)
    return im


def create_pdf_from_docs(input_dir: str, output_dir):
    temp_dir = os.path.join(output_dir, "temp")
    for root, dirs, files in os.walk(input_dir):
        [os.makedirs(os.path.join(output_dir, _dir), exist_ok=True) for _dir in dirs]
        for file in files:
            os.makedirs(temp_dir, exist_ok=True)
            if not file.endswith('.docx'):
                continue

            print(f"Processing file: {file}")
            zip_file = zipfile.ZipFile(os.path.join(root, file))
            doc_xml = zip_file.read('word/document.xml')
            doc_tree = etree.fromstring(doc_xml)

            pdf_pages = []
            for i, node in enumerate(doc_tree.iter(tag=etree.Element)):
                if node.prefix == 'pic' and 'name' in node.attrib:
                    pdf_pages.append(node.attrib['name'])
            pdf_pages = [name.replace('.png', '.jpg') for name in pdf_pages]

            docx2txt.process(os.path.join(root, file), temp_dir)
            # converting png to jpg
            [convert_png_to_jpg(os.path.join(temp_dir, im), temp_dir) for im in os.listdir(temp_dir)]
            # deleting png
            [os.remove(os.path.join(temp_dir, im)) for im in os.listdir(temp_dir) if im.endswith('.png')]

            images = [Image.open(os.path.join(temp_dir, f)) for f in pdf_pages]
            pdf_path = os.path.join(output_dir, root.split("/")[-1], f"{file.split('.')[0]}.pdf")
            images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])

            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    input_docx_dir = '/home/userd136/Desktop/bkst_accountType/'
    pdf_output_dir = '/home/userd136/Desktop/bkst_actype_pdf'
    create_pdf_from_docs(input_docx_dir, output_dir=pdf_output_dir)
