# Automated_report-generation
Python script to generate PDF report from CSV
# 📊 Automated PDF Report Generator

This Python project reads student data from a CSV file, calculates the average score, and generates a formatted PDF report using the `fpdf` library.
🔧 Features

- 📂 Reads data from any `.csv` file
- 🧮 Calculates total and average score
- 📝 Creates a clean, formatted PDF report
- ✅ Easy to use – beginner friendly!
📁 Files

| File Name         | Description                                |
|------------------|--------------------------------------------|
| `report_script.py` | Main Python script                        |
| `data.csv`         | Sample student data                       |
| `report.pdf`       | Output PDF report (auto-generated)        |
| `README.md`        | Project description and usage instructions|

 ▶️ How to Run

1. Install Python from https://python.org
2. Install the required library:
   pip install fpdf
3. Place your `.csv` file in the same folder.
4. Run the script:
   python report_script.py
5. Enter your CSV file name when asked.
6. A new `report.pdf` will be created!

 🛠 Built With

- Python
- [FPDF](https://pypi.org/project/fpdf/) – for PDF generation

 Sample CSV Format:

```csv
Name,Score
Alice,85
Bob,90
Charlie,78


