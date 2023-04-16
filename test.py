import csv
from fpdf import FPDF

from googletrans import Translator, constants
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def translatet(word):
    tra = Translator()
    tt = tra.translate(word)
    return tt.text

def create_pdf():
    # Create the canvas and set the font
    c = canvas.Canvas("multi_language_paragraphs.pdf", pagesize=letter)
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    c.setFont('Arial', 16)

    # Define the paragraphs as a list of tuples
    paragraphs = [
        ("Header 1", "Body Text 1", "www.example.com/1"),
        ("عنوان 2", "نص 2", "www.example.com/2"),
        ("Заголовок 3", "Текст 3", "www.example.com/3")
    ]

    # Set the starting position for the first paragraph
    x_pos = 2 * inch
    y_pos = 10 * inch
    with open('output_file.csv', encoding="utf-8-sig") as csv_file:
        # Create a CSV reader object
        reader = csv.reader(csv_file)
        
        # Skip the header row

        # Loop over each row in the CSV file
        for row in reader:
            header = row[1]
            body = row[0]
            link = row[2]
            # Add header
            if y_pos < 1.5 * inch:
                c.showPage()
                y_pos = 10 * inch
        # Add header
            header_width = c.stringWidth(header, 'Arial', 16)
            if x_pos + header_width > 7.5 * inch:
                x_pos = 2 * inch
                y_pos -= 0.5 * inch
            c.drawString(x_pos, y_pos, header)

            # Add body
            body_width = c.stringWidth(body, 'Arial', 16)
            if x_pos + body_width > 7.5 * inch:
                x_pos = 2 * inch
                y_pos -= 0.5 * inch
            c.drawString(x_pos, y_pos - 0.5 * inch, body)

            # Add link as a separate line
            link_text = "Link: " + link
            link_width = c.stringWidth(link_text, 'Arial', 16)
            if x_pos + link_width > 7.5 * inch:
                x_pos = 2 * inch
                y_pos -= 0.5 * inch
            link_x = x_pos
            link_y = y_pos - 1 * inch
            c.setFillColorRGB(0, 0, 255)
            c.drawString(link_x, link_y, link_text)

            # Add line separator
            c.line(x_pos, y_pos - inch, x_pos + 5.5 * inch, y_pos - inch)

            # Update the x and y position for the next paragraph
            x_pos += 5.5 * inch
            if x_pos > 7.5 * inch:
                x_pos = 2 * inch
                y_pos -= 1.5 * inch

    # Save the PDF
    c.save()

create_pdf()


def writte():
 with open('output_file.csv', encoding="utf-8-sig") as csv_file:
        # Create a CSV reader object
        reader = csv.reader(csv_file)
        
        # Skip the header row

        # Loop over each row in the CSV file
        for row in reader:
            # Print the values in each row
            t = translatet(row[0])
            d = translatet(row[1])
            



