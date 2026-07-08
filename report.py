import pandas as pd

def create_detection_report(data):
    """
    Create a detection report as a pandas DataFrame.
    """

    df = pd.DataFrame(data)
    return df


def convert_to_csv(df):
    """
    Convert the DataFrame to CSV format.
    """

    return df.to_csv(index=False).encode("utf-8")
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(df, filename):
    """
    Generate a PDF detection report.
    """

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("AI Smart Image Annotation System", styles["Heading1"])
    elements.append(title)

    elements.append(Paragraph("Detection Report", styles["Heading2"]))

    # Table Data
    table_data = [list(df.columns)]

    for row in df.values.tolist():
        table_data.append(row)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.green),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ]))

    elements.append(table)

    pdf.build(elements)
    
    
    
    