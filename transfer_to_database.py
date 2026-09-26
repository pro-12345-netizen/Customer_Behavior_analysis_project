import os
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Database Connection Configurations
username = "root"
password = "Par1234"  # <-- Put your reset password here
host = "localhost"
port = "3306"
database = "da_project"  # <-- Target database set to da_project

# 2. Create the database if it does not exist
root_engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}")
with root_engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{database}`"))

# 3. Connect to the target database
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# 4. Read your CSV file
csv_filename = "customer_shopping_behavior_cleaned.csv"
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, csv_filename)

df = pd.read_csv(csv_path)

# 5. Write the DataFrame to MySQL
table_name = "customer_shopping"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Success! Data from '{csv_filename}' has been uploaded to the '{table_name}' table inside the '{database}' database.")
