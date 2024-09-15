# Online Retail Analysis

---

_Table of Contents_

- [**1. Tech Stack**](#1-tech-stack)

- [**2. Data Architecture**](#2-data-architecture)
  * [2.1. Conceptual Architecture](#21-conceptual-architecture)
  * [2.2. Physical Architecture](#22-physical-architecture)

- [**3. Dataset**](#3-dataset)

- [**4. End to End Solution**](#4-end-to-end-solution)
  * [4.1. Build Data Pipeline](#41-build-data-pipeline)
  * [4.2. Result of Pipeline](#42-result-of-pipeline)

- [**5. Report**](#5-report)
  * [5.1. Data Modelling](#51-data-modelling)
  * [5.2. Report](#52-report)

---


# **1. Tech Stack**

- **Docker**: Docker is a containerization platform that simplifies the deployment and management of applications by encapsulating them into portable containers. These containers include all the necessary dependencies, ensuring that your applications run consistently across different environments. Just like a virtualized environment, Docker containers provide isolated environments for running applications without the overhead of traditional virtual machines.

- **Astro CLI**: Astro CLI is a command-line interface designed for managing and deploying data workflows within your data engineering ecosystem. It streamlines the orchestration of complex data tasks and workflows, similar to how a conductor manages an orchestra, ensuring that each data task is executed in the correct sequence and dependencies are effectively handled.

- **Great Expectation**: Great Expectation is a data quality monitoring tool that helps you maintain the integrity of your data. It allows you to set up and run automated data quality checks to detect and alert you to anomalies or issues in your data pipelines. Great Expectation ensures that your data meets quality standards throughout the ETL process, just like a quality control system in manufacturing.

- **Hadoop (HDFS)**: Hadoop is an open-source framework designed for storing and processing large volumes of data across distributed clusters. The Hadoop Distributed File System (HDFS) is a key component of Hadoop, providing scalable and fault-tolerant storage by breaking data into blocks and distributing them across multiple nodes. This architecture ensures high availability and efficient data management, making it ideal for handling big data workloads.

- **Apache Superset**: Apache Superset is an open-source data exploration and visualization platform designed for creating interactive dashboards and visualizations. It offers a rich set of features for connecting to various data sources, performing data analysis, and generating insightful visualizations. With its user-friendly interface and extensive support for SQL queries, Superset enables users to explore data, build custom dashboards, and share insights across teams, making it a powerful tool for data-driven decision-making.

- **Apache Airflow**: Apache Airflow is a workflow automation tool that allows you to define, schedule, and monitor complex data workflows. It acts like a task scheduler for your data engineering processes, ensuring that each step in your pipeline is executed in the correct order and dependencies are managed efficiently.

- **Data Build Tools (DBT)**: DBT is a data transformation tool that enables you to build and manage your data models using SQL. It facilitates transformations and data modeling within your data warehouse, integrating with workflow orchestrators like Airflow to automate the execution of data transformation tasks and ensuring that your data is ready for analysis.


# **2. Data Architecture**

## 2.1. Conceptual Architecture
![Items (1)](https://github.com/thanhphat2609/Global_Super_Store/assets/84914537/600e237e-01d7-4c09-891c-1551acfbc45e)

- **Data Source**: These include the various systems from which data is **extracted**, such as: Relational Database, File systems, SaaS applications, Real-time data.
- **Staging**: Extract data from Source into Files of Lakehouse (csv, parquet) or Delta Tables.
- **Data Warehouse**: Data in the data warehouse is organized according to a unified data model, which makes it easy to query and analyze.
- **Analytics**: This last step we will use tools and techniques to analyze the data in the data warehouse, such as: Power BI, Tableau, Superset ..

## 2.2. Physical Architecture
![dockerarchitecture](https://github.com/user-attachments/assets/ccfe5173-93e4-4049-9391-d2e6e1aa13f5)

- **Source Data (CSV from Kaggle)**: The project sources data from a Kaggle Online Retail dataset in CSV format, representing the initial stage.

- **Data Storage (Hadoop HDFS)**: The ingested CSV data is stored in a data lake, leveraging Hadoop for distributed storage, allowing scalability and fault tolerance. The storage layer is named Online_Retail_Analysis.

- **Orchestration Layer**: This layer manages workflow automation, data quality checks and data transformation using **Python, Great_Expectations, Data Build Tools (DBT)**.

- **Reporting Layer**: The transformed data is pushed to an SQL database using SSMS (SQL Server Management Studio) for querying. Apache Superset then accesses this structured data for generating insights and reports, allowing stakeholders to visualize and make decisions based on the processed data.

- **Containerization with Docker**: The entire setup is containerized using Docker, ensuring portability and consistency across different environments.

=> This architecture streamlines the ETL process, enabling automated orchestration, reliable data quality, efficient storage, and powerful reporting capabilities for data-driven decisions.

# **3. Dataset**

Link for specific dataset in Kaggle: [Online_Retail_Dataset](https://www.kaggle.com/datasets/tunguz/online-retail)

| Column        | Description                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| InvoiceNo     | Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation. |
| StockCode     | Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.         |
| Description   | Product (item) name. Nominal.                                                                                 |
| Quantity      | The quantities of each product (item) per transaction. Numeric.                                               |
| InvoiceDate   | Invoice Date and time. Numeric, the day and time when each transaction was generated.                        |
| UnitPrice     | Unit price. Numeric, Product price per unit in sterling.                                                       |
| CustomerID    | Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.                      |
| Country       | Country name. Nominal, the name of the country where each customer resides.                                  |


# **4. End to End Solution**

## 4.1. Build Data Pipeline

- **Container**

Container for project
![image](https://github.com/user-attachments/assets/f0628e01-2eaa-4272-a358-ca52ebb870f5)

Container for Hadoop
![image](https://github.com/user-attachments/assets/e216fb04-0aa4-44a7-8dc2-ccf695b3b5e0)

Container for Superset
![image](https://github.com/user-attachments/assets/7c9c1338-3e68-4b08-bc0d-8ed1adaf5141)

- **HDFS Data Lake Storage**:
![image](https://github.com/user-attachments/assets/cec9ece6-abc0-411a-bff4-945905314aae)

- **Data Pipeline in Airflow**:
![image](https://github.com/user-attachments/assets/fbebbdff-d437-4b05-b10b-59060a4b2692)

- **Variable in Airflow Orchestration**:
![image](https://github.com/user-attachments/assets/8f08347e-f416-4a10-84fd-0aa030994e2f)

## 4.2. Result of Pipeline

- **PIPELINE result**
![image](https://github.com/user-attachments/assets/30275f4d-0979-4978-9e40-97946700ecee)

- **DATA QUALITY check for SOURCE**
![image](https://github.com/user-attachments/assets/4d543f93-a2c0-4559-a0bb-cfa32b3a9be8)

- **STAGING Phase**

![image](https://github.com/user-attachments/assets/6ce6f301-3c71-4aa4-807e-3d2199b2a386)

- **DATA WAREHOUSE Phase**

![image](https://github.com/user-attachments/assets/0088105c-0431-48ae-9cfc-63c8dad9d1d6)

- **DATA QUALITY check for Data MODEL**

Not Updated Yet. (Dont know what to check for Data Modelling)

# **5. Report**

## 5.1. Data Modelling

![image](https://github.com/user-attachments/assets/04036de9-693b-4503-89df-e74cef787b09)

## 5.2. Report

![image](https://github.com/user-attachments/assets/af741614-4d7d-42fd-a586-5e27bb23b955)
