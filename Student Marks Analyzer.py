import pandas as pd

# Load data
df = pd.read_csv("students.csv")

# Add total and average columns
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Find topper
topper = df.loc[df["Average"].idxmax()]

print(" Student Performance Summary\n")
print(df[["Name", "Maths", "Science", "English", "Total", "Average"]])

print(f"\n Topper: {topper['Name']} with an average of {topper['Average']:.2f}")
print(f" Lowest Scorer: {df.loc[df['Average'].idxmin()]['Name']}")

# Optional: Save results
df.to_csv("student_results.csv", index=False)
