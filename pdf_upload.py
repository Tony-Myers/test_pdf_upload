import fitz  
import stremlit# PyMuPDF

# Open a sample PDF file
pdf_document = fitz.open("path/to/your/document.pdf")

# Print the number of pages
print(f"Number of pages: {pdf_document.page_count}")

# Close the document
pdf_document.close()

