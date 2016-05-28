import sys

from docx import Document

def doc_to_text_catdoc(filename):
    document = Document(filename)
    # dest_filename = '../../txt/' + filename.replace('.docx', '').replace('data/docx/', '') + '.txt'
    dest_filename = 'data/txt/test.txt'
    paragraphs = document.paragraphs
    full_text = []

    for paragraph in paragraphs:
        # print paragraph.text
        full_text.append(paragraph.text.encode('utf-8', 'ignore'))

    with open(dest_filename, 'w') as f:
        for line in full_text:
            f.write(line + '\n')

doc_to_text_catdoc('data/docx/A2015/A71482.docx')