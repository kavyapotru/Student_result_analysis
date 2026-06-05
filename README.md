# 📊 Student Result Analysis Dashboard

A Python-based data analysis tool to process and visualize student academic performance using SQL queries and Matplotlib charts.

## 🔍 Features

- Loads student data from CSV into a **SQLite database**
- Runs **SQL queries** to calculate subject-wise averages
- Calculates **Pass/Fail ratio** automatically
- Generates a **4-chart dashboard** with visualizations
- Auto-generates a **text report** with summary statistics
- Reduces manual effort by ~70% compared to manual Excel analysis

## 📁 Project Structure

```
student_dashboard/
│
├── analysis.py       # Main Python script
├── students.csv      # Sample student data
├── students.db       # Auto-generated SQLite database
├── report.txt        # Auto-generated summary report
└── charts/
    └── dashboard.png # Generated dashboard image
```

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** - Data manipulation
- **SQLite3** - Database queries
- **Matplotlib** - Data visualization

## ▶️ How to Run

```bash
# Install dependencies
pip install pandas matplotlib

# Run the analysis
python analysis.py
```

## 📈 Dashboard Preview

The dashboard generates 4 charts:
1. Subject-wise Average Scores (Bar Chart)
2. Pass/Fail Ratio (Pie Chart)
3. Student-wise Percentage (Bar Chart)
4. Top 5 Students (Horizontal Bar Chart)

## 👩‍💻 Developer

**Kavya Sri Potru**  
GitHub: [github.com/kavyapotru](https://github.com/kavyapotru)  
LinkedIn: [linkedin.com/in/kavya-sree-potru-089722292](https://www.linkedin.com/in/kavya-sree-potru-089722292)
