from pypdf import PdfReader

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


# extract_text_from_pdf("cv3.pdf")
# print(extract_text_from_pdf("cv3.pdf"))