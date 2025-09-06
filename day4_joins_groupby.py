import pandas as pd

# 1) Load
emp = pd.read_csv("employees.csv")
dept = pd.read_csv("departments.csv")

print("Employees:\n", emp)
print("\nDepartments:\n", dept)

# 2) Joins
inner = emp.merge(dept, on="dept_id", how="inner")
print("\nINNER JOIN:\n", inner)

left = emp.merge(dept, on="dept_id", how="left")
print("\nLEFT JOIN:\n", left)

right = emp.merge(dept, on="dept_id", how="right")
print("\nRIGHT JOIN:\n", right)

outer = emp.merge(dept, on="dept_id", how="outer", indicator=True)
print("\nOUTER JOIN (+indicator):\n", outer)

# 3) GroupBy
by_dept = left.groupby("dept_name", dropna=False, as_index=False)["salary"].mean()
print("\nAvg salary by dept:\n", by_dept)

agg = left.groupby("dept_name", dropna=False).agg(
    count=("emp_id", "count"),
    avg_sal=("salary", "mean"),
    max_sal=("salary", "max"),
).reset_index()
print("\nAggregations:\n", agg)

# 4) Top 3 salaries
top_paid = left.sort_values("salary", ascending=False).head(3)
print("\nTop 3 salaries:\n", top_paid)
