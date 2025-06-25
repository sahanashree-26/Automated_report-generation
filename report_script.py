import csv
from fpdf import FPDF

filename = 'data.csv'
names = []
scores = []
total = 0

with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        score = int(row['Score'])
        names.append(name)
        scores.append(score)
        total += score

average = total / len(scores)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Student Score Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "Name", border=1)
pdf.cell(50, 10, "Score", border=1, ln=True)

pdf.set_font("Arial", size=12)
for name, score in zip(names, scores):
    pdf.cell(100, 10, name, border=1)
    pdf.cell(50, 10, str(score), border=1, ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "Average Score:", border=0)
pdf.cell(50, 10, f"{average:.2f}", border=0)

pdf.output("report.pdf")

print("PDF report created as 'report.pdf'")
