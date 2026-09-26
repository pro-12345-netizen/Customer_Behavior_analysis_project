# 🛍️ Customer Shopping Behavior Analysis

A complete, end-to-end data analytics project — from raw data to business insights — covering Python-based EDA, SQL-driven business analysis, an interactive Power BI dashboard, and a stakeholder-ready presentation.

---

## 📌 Overview

This project analyzes customer shopping behavior using transactional data from **3,900 purchases** across multiple product categories. The goal is to uncover patterns in customer spending, segmentation, product preferences, and subscription behavior — and translate them into clear, actionable business recommendations.

**Workflow:** Data Loading → EDA & Cleaning (Python) → SQL Analysis → Power BI Dashboard → Report & Presentation

---

## 📊 Dataset

| Detail | Description |
|---|---|
| **Rows** | 3,900 |
| **Columns** | 18 |
| **Customer Demographics** | Age, Gender, Location, Subscription Status |
| **Purchase Details** | Item Purchased, Category, Purchase Amount, Season, Size, Color |
| **Shopping Behavior** | Discount Applied, Promo Code Used, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type |
| **Data Quality** | 37 missing values in the `Review Rating` column (handled during cleaning) |

---

## 🛠️ Tools & Technologies

- **Python** – pandas, for data loading, cleaning, and feature engineering
- **SQL** – PostgreSQL / MySQL / SQL Server, for structured business analysis
- **Power BI** – interactive dashboard and data visualization
- **Gamma** – presentation deck design

---

## 🔍 Steps

### 1. Data Loading & Exploration (Python)
- Imported the dataset using `pandas`
- Used `df.info()` and `.describe()` to understand structure and summary statistics

### 2. Data Cleaning
- Checked for null values and imputed missing `Review Rating` entries using the **median rating per product category**
- Standardized column names to `snake_case` for consistency
- Verified redundancy between `discount_applied` and `promo_code_used`, and dropped the redundant column

### 3. Feature Engineering
- Created `age_group` by binning customer ages
- Created `purchase_frequency_days` from purchase data

### 4. Database Integration
- Connected the cleaned Python DataFrame to **PostgreSQL** for structured SQL analysis

### 5. SQL Analysis (Business Questions)
Ten targeted queries were written to answer key business questions, including:
1. Revenue by Gender
2. High-Spending Discount Users
3. Top 5 Products by Rating
4. Shipping Type Comparison
5. Subscribers vs. Non-Subscribers
6. Discount-Dependent Products
7. Customer Segmentation (New / Returning / Loyal)
8. Top 3 Products per Category
9. Repeat Buyers & Subscription Correlation
10. Revenue by Age Group

### 6. Dashboard Design (Power BI)
Built an interactive dashboard to visualize insights, with filters for subscription status, gender, category, and shipping type.

### 7. Reporting & Presentation
Compiled findings into a written report and a summary presentation built in **Gamma**.

---

## 📈 Dashboard

The Power BI dashboard presents key metrics and trends at a glance:

- **3.9K** total customers
- **$59.76** average purchase amount
- **3.75** average review rating
- Interactive filters: Subscription Status, Gender, Category, Shipping Type
- Visuals: Revenue by Category, Sales by Category, Revenue by Age Group, Sales by Age Group, Subscription Status breakdown

> 📎 *Dashboard file / screenshots available in the Power Bi Document.*

---

## ✅ Results & Key Insights

| Insight | Finding |
|---|---|
| **Revenue by Gender** | Male customers generated significantly higher total revenue than female customers |
| **Top-Rated Products** | Gloves, Sandals, Boots, Hats, and Skirts had the highest average ratings |
| **Shipping Type** | Express shipping customers spent slightly more on average than Standard shipping customers |
| **Subscribers vs. Non-Subscribers** | Non-subscribers generated far higher total revenue, despite a similar average spend |
| **Discount-Dependent Products** | Hats, Sneakers, Coats, Sweaters, and Pants relied most heavily on discounts |
| **Customer Segments** | The majority of customers (3,116) fall into the "Loyal" segment |
| **Repeat Buyers** | Customers with more than 5 purchases were more likely to hold a subscription |
| **Revenue by Age Group** | Young Adults contributed the highest total revenue, followed closely by Middle-aged and Adult groups |

### 💡 Business Recommendations
- **Boost Subscriptions** – Promote exclusive benefits to convert non-subscribers
- **Customer Loyalty Programs** – Reward repeat buyers to strengthen retention
- **Review Discount Policy** – Balance promotional sales with profit margins
- **Product Positioning** – Highlight top-rated and best-selling items in marketing campaigns
- **Targeted Marketing** – Focus on high-revenue age groups and express-shipping customers

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<pro-12345-netizen>/customer-shopping-behavior-analysis.git
   cd customer-shopping-behavior-analysis
   ```

2. **Set up the Python environment**
   ```bash
   pip install pandas numpy sqlalchemy psycopg2
   ```

3. **Run the data cleaning & EDA notebook**
   ```bash
   jupyter notebook notebooks/eda_and_cleaning.ipynb
   ```

4. **Load data into your SQL database**
   - Update database credentials in `db_config.py` / connection script
   - Run the loading script to push the cleaned DataFrame into PostgreSQL/MySQL/SQL Server

5. **Run SQL queries**
   - Open `sql/business_queries.sql` in your SQL client
   - Execute queries individually to reproduce the analysis

6. **Open the Power BI dashboard**
   - Open `dashboard/Customer_Behavior_Dashboard.pbix` in Power BI Desktop
   - Refresh the data connection if needed

7. **View the report & presentation**
   - Report: `reports/Customer_Shopping_Behavior_Analysis_Report.pdf`
   - Presentation: `presentation/Customer_Shopping_Behavior_Analysis.pptx`

---

## 📁 Project Structure

```
customer-shopping-behavior-analysis/
│
├── data/                     # Raw and cleaned datasets
├── notebooks/                 # Python EDA & cleaning notebooks
├── sql/                        # SQL business analysis queries
├── dashboard/                  # Power BI dashboard file
├── reports/                    # Final written report
├── presentation/                # Gamma-generated presentation
└── README.md
```

---

## 👤 Author

**pro-12345-netizen**
 Data Analytics Enthusiast

Feel free to connect or reach out with feedback and suggestions!

---

⭐ *If you found this project useful, consider giving it a star on GitHub!*
