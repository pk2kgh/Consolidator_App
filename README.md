# Consolidator – Student Data Extraction & Excel Automation  | Created in 2020

A Python-based Android application built using **Pandas, Kivy, and KivyMD** to simplify and automate student data extraction from CSV files which is the DB containing details of all students and generate customized Excel document which was used in my case to provide consolidated Interested student list for College final year campus placement, this really helped me consolidate and provide Interested student list at no time.

The application allows users to select specific student records and relevant data fields through a simple mobile interface, eliminating the need for manual CSV filtering and spreadsheet manipulation.

## Project Overview

Managing large student datasets often involves extracting specific student records and selecting relevant attributes for reporting.

Consolidator automates this process by allowing users to:

- Import student records from CSV files.
- Select specific students using their IDs.
- Choose the required data fields using predefined shortcuts.
- Extract the requested rows and columns using Pandas.
- Export the filtered dataset into an Excel file.

## Key Features

- **CSV Import:** Load CSV datasets directly from Android device storage.
- **Student Record Selection:** Extract specific student records using comma-separated student IDs.
- **Dynamic Column Selection:** Select required attributes using predefined field identifiers.
- **Data Processing with Pandas:** Use DataFrames for structured data extraction and manipulation.
- **Excel Export:** Generate customized `.xlsx` reports.
- **Mobile Interface:** Interactive Android interface built with Kivy and KivyMD.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | CSV processing, DataFrame manipulation, row and column selection |
| Kivy | Cross-platform application framework |
| KivyMD | Material Design user interface |
| OpenPyXL / Excel engine | Excel file export (via Pandas) |
| JSONStore | Kivy storage component imported for potential local data persistence |

## How It Works

The application follows a simple data extraction workflow:

1. **Import Dataset:** The user selects a CSV file from device storage.
2. **Enter Student IDs:** The user provides comma-separated student IDs.
3. **Select Data Fields:** The user enters field identifiers corresponding to the required columns.
4. **Process Dataset:** Pandas reads the CSV and constructs a customized DataFrame containing the selected records and columns.
5. **Export Report:** The resulting DataFrame is exported as an Excel workbook.

## Pandas Implementation

The core data processing logic uses Pandas to transform the source CSV into a customized dataset.

### 1. Reading the CSV Dataset

```python
data = pd.read_csv(csv_path)
```

Reads the source CSV file into a Pandas DataFrame.

### 2. Selecting Student Records

```python
def list_cov(STID):
    st_id = STID.split(",")

    for i in range(len(st_id)):
        st_id[i] = int(st_id[i]) - 1

    return st_id
```

Converts user-provided student IDs into zero-based row indices for DataFrame selection.

### 3. Mapping Field Identifiers

```python
key_value = {
    'tg': 'TAG',
    'rn': 'REGISTER NUMBER',
    'n': 'NAME',
    'mi': 'MAIL ID',
    'rln': 'ROLL NO',
    'te': 'SSLC(Percentage)',
    'tw': 'HSC (percentage)',
    'cg': 'CGPA',
    'pn': 'PHONE NUMBER',
    'g': 'GENDER',
    'br': 'BRANCH'
}
```

Maps short field identifiers to their corresponding dataset column names, making field selection easier for users.

### 4. Creating a Customized DataFrame

```python
data = pd.read_csv(csv_path)

df = pd.DataFrame(
    data,
    index=selected_student_indices,
    columns=selected_columns
)
```

Uses Pandas DataFrame indexing to extract the requested student records and attributes.

### 5. Exporting to Excel

```python
df.to_excel(
    output_path,
    index=False
)
```

Exports the processed dataset into an Excel workbook without including the DataFrame index.

## Example Use Case

Consider a student dataset containing thousands of records with attributes such as:

- Register Number
- Student Name
- Email ID
- CGPA
- Branch
- Backlogs
- Contact Number

Suppose a user needs only a few student records with their names, register numbers, and CGPA.

Instead of manually filtering the CSV file and copying the results into Excel, Consolidator automates the extraction and generates a customized spreadsheet.

## Project Learnings

This project provided practical experience with:

- Python application development.
- Pandas DataFrame operations.
- CSV data ingestion and Excel report generation.
- Row and column indexing.
- Mapping user inputs to dataset attributes.
- Automating repetitive data extraction workflows.
- Integrating data processing logic with a mobile application interface.

## Project Context

This project was developed approximately seven years ago as a practical automation application.

It represents an early hands-on application of Python and Pandas to solve a real-world structured data processing problem.

The project demonstrates foundational experience in data manipulation, reporting automation, and application development.

---

**Project Category:** Python | Data Processing | Data Automation | Mobile Application Development# Consolidator – Student Data Extraction & Excel Automation

A Python-based Android application built using **Pandas, Kivy, and KivyMD** to simplify student data extraction from CSV files and generate customized Excel reports.

The application allows users to select specific student records and relevant data fields through a simple mobile interface, eliminating the need for manual CSV filtering and spreadsheet manipulation.

## Project Overview

Managing large student datasets often involves extracting specific student records and selecting relevant attributes for reporting.

Consolidator automates this process by allowing users to:

- Import student records from CSV files.
- Select specific students using their IDs.
- Choose the required data fields using predefined shortcuts.
- Extract the requested rows and columns using Pandas.
- Export the filtered dataset into an Excel file.

## Key Features

- **CSV Import:** Load CSV datasets directly from Android device storage.
- **Student Record Selection:** Extract specific student records using comma-separated student IDs.
- **Dynamic Column Selection:** Select required attributes using predefined field identifiers.
- **Data Processing with Pandas:** Use DataFrames for structured data extraction and manipulation.
- **Excel Export:** Generate customized `.xlsx` reports.
- **Mobile Interface:** Interactive Android interface built with Kivy and KivyMD.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | CSV processing, DataFrame manipulation, row and column selection |
| Kivy | Cross-platform application framework |
| KivyMD | Material Design user interface |
| OpenPyXL / Excel engine | Excel file export (via Pandas) |
| JSONStore | Kivy storage component imported for potential local data persistence |

## How It Works

The application follows a simple data extraction workflow:

1. **Import Dataset:** The user selects a CSV file from device storage.
2. **Enter Student IDs:** The user provides comma-separated student IDs.
3. **Select Data Fields:** The user enters field identifiers corresponding to the required columns.
4. **Process Dataset:** Pandas reads the CSV and constructs a customized DataFrame containing the selected records and columns.
5. **Export Report:** The resulting DataFrame is exported as an Excel workbook.

## Pandas Implementation

The core data processing logic uses Pandas to transform the source CSV into a customized dataset.

### 1. Reading the CSV Dataset

```python
data = pd.read_csv(csv_path)
```

Reads the source CSV file into a Pandas DataFrame.

### 2. Selecting Student Records

```python
def list_cov(STID):
    st_id = STID.split(",")

    for i in range(len(st_id)):
        st_id[i] = int(st_id[i]) - 1

    return st_id
```

Converts user-provided student IDs into zero-based row indices for DataFrame selection.

### 3. Mapping Field Identifiers

```python
key_value = {
    'tg': 'TAG',
    'rn': 'REGISTER NUMBER',
    'n': 'NAME',
    'mi': 'MAIL ID',
    'rln': 'ROLL NO',
    'te': 'SSLC(Percentage)',
    'tw': 'HSC (percentage)',
    'cg': 'CGPA',
    'pn': 'PHONE NUMBER',
    'g': 'GENDER',
    'br': 'BRANCH'
}
```

Maps short field identifiers to their corresponding dataset column names, making field selection easier for users.

### 4. Creating a Customized DataFrame

```python
data = pd.read_csv(csv_path)

df = pd.DataFrame(
    data,
    index=selected_student_indices,
    columns=selected_columns
)
```

Uses Pandas DataFrame indexing to extract the requested student records and attributes.

### 5. Exporting to Excel

```python
df.to_excel(
    output_path,
    index=False
)
```

Exports the processed dataset into an Excel workbook without including the DataFrame index.

## Example Use Case

Consider a student dataset containing thousands of records with attributes such as:

- Register Number
- Student Name
- Email ID
- CGPA
- Branch
- Backlogs
- Contact Number

Suppose a user needs only a few student records with their names, register numbers, and CGPA.

Instead of manually filtering the CSV file and copying the results into Excel, Consolidator automates the extraction and generates a customized spreadsheet.

## Project Learnings

This project provided practical experience with:

- Python application development.
- Pandas DataFrame operations.
- CSV data ingestion and Excel report generation.
- Row and column indexing.
- Mapping user inputs to dataset attributes.
- Automating repetitive data extraction workflows.
- Integrating data processing logic with a mobile application interface.

## Project Context

This project was developed approximately seven years ago as a practical automation application.

It represents an early hands-on application of Python and Pandas to solve a real-world structured data processing problem.

The project demonstrates foundational experience in data manipulation, reporting automation, and application development.

---

**Project Category:** Python | Data Processing | Data Automation | Mobile Application Development
