from pypdf import PdfReader
import os

input_file = os.getenv('input', 'file.pdf')

output_file = os.getenv('output', 'file.txt')

reader = PdfReader(input_file)

with open(output_file, 'a+') as txt_file:
  for page in reader.pages:
    page_text = page.extract_text().strip()
    txt_file.write(page_text)
