# Import necessary libraries
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the CSV URL
url = "https://health.data.ny.gov/resource/5dtw-tffi.csv?$limit=2400000"
df = pd.read_csv(url)

pd.set_option('display.float_format', lambda x: '%.3f' % x)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')
df_len = len(df) 
df.total_charges = df.total_charges.apply(lambda x : x.replace(',',''))
df.total_costs = df.total_costs.apply(lambda x : x.replace(',',''))
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')
df['length_of_stay'] = pd.to_numeric(df['total_costs'], errors='coerce')
df['age_group'] = pd.to_numeric(df['total_costs'], errors='coerce')


#### describing the data model 
print(df.info())
print(df.describe())
df.shape
len(df)
df.columns



df['gender'].value_counts()
df['length_of_stay'].value_counts()




#total charges plot
sns.boxplot(data=df, x='total_charges')
plt.title('Boxplot of Total Charges')
plt.savefig('boxplot_total_charges.png')
plt.show()

#length of stay 
plt.figure(figsize=(10, 6))
sns.histplot(df['length_of_stay'], bins=30)
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay (days)')
plt.ylabel('Frequency')
plt.savefig('length_of_stay.png')
plt.show()

#type of admission
plt.figure(figsize=(8, 6))
sns.countplot(df['type_of_admission'])
plt.title('Count of Different Types of Admissions')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.savefig('type_of_admission.png')
plt.show()



# Distribution type for age group, gender, and admission type

age_group_distribution = df['age_group'].value_counts()
gender_distribution = df['gender'].value_counts()
admission_type_distribution = df['type_of_admission'].value_counts()

print("Age Group Distribution:")
print(age_group_distribution)
print("\nGender Distribution:")
print(gender_distribution)
print("\nType of Admission Distribution:")
print(admission_type_distribution)

# age group
sns.countplot(df['age_group'])
plt.title('Count of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.savefig('age_group.png')
plt.show()


#gender
sns.countplot(data=df, x='gender')
plt.title('Frequency of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.savefig('gender.png')
plt.show()










# ----------------- Basic Descriptive Statistics -----------------
# Descriptive statistics for Length of Stay, Total Charges, and Total Costs

# For Length of Stay
df['length_of_stay'].mean()
df['length_of_stay'].median()
df['length_of_stay'].std()
df['length_of_stay'].min()
df['length_of_stay'].max()
df['length_of_stay'].quantile([0.25, 0.50, 0.75])




#total Charges 
df['total_charges'].value_counts()
df['total_charges'].describe()
df['total_charges'].mean()
df['total_charges'].median()
df['total_charges'].std()
df['total_charges'].min()
df['total_charges'].max()
df['total_charges'].quantile([0.25, 0.50, 0.75])



df['total_costs'].value_counts()
df['total_costs'].describe()
df['total_costs'].mean()
df['total_costs'].median()
df['total_costs'].std()
df['total_costs'].min()
df['total_costs'].max()
df['total_costs'].quantile([0.25, 0.50, 0.75])