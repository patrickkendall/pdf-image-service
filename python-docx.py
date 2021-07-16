from docx import Document
from docx.shared import Inches
from PIL import Image
import requests
from docx.shared import Pt

document = Document()

document.add_picture('propertyPicsTitle.png', width=Inches(6), height=Inches(1.5))

tables = document.tables
table = document.add_table(rows=1, cols=3)
row_cells = table.add_row().cells

for i, image in enumerate(['property0.jpeg', 'property1.jpg', 'property2.jpg']):
    paragraph = row_cells[i].paragraphs[0]
    run = paragraph.add_run()
    run.add_picture(image, width=Inches(1.9))

tables = document.tables
table = document.add_table(rows=1, cols=3)
row_cells = table.add_row().cells

for i, image in enumerate(['property3.jpg', 'property4.jpg', 'property5.jpg']):
    paragraph = row_cells[i].paragraphs[0]
    run = paragraph.add_run()
    run.add_picture(image, width=Inches(1.9))

tables = document.tables
table = document.add_table(rows=1, cols=3)
row_cells = table.add_row().cells

for i, image in enumerate(['property2.jpg', 'property4.jpg', 'property4.jpg']):
    paragraph = row_cells[i].paragraphs[0]
    run = paragraph.add_run()
    run.add_picture(image, width=Inches(1.9))

document.save('demo.docx')