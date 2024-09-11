# Online Retail Analysis

Certainly! Here’s a table of contents formatted in a similar style to the example you provided:

---

_Table of Contents_

- [**1. Tech Stack**](#1-tech-stack)

- [**2. Data Architecture**](#2-data-architecture)
  * [2.1. Conceptual Architecture](#21-conceptual-architecture)
  * [2.2. Physical Architecture](#22-physical-architecture)

- [**3. Dataset**](#3-dataset)

- [**4. Data Pipeline**](#4-data-pipeline)
  * [4.1. Build Data Pipeline](#51-build-data-pipeline)
  * [4.2. Result of Pipeline](#52-result-of-pipeline)

- [**5. Report**](#5-report)
  * [5.1. Data Modelling](#51-data-modelling)
  * [5.2. Report](#52-report)

---


# **1. Tech Stack**

- **Docker**: Docker is a containerization platform that simplifies the deployment and management of applications by encapsulating them into portable containers. These containers include all the necessary dependencies, ensuring that your applications run consistently across different environments. Just like a virtualized environment, Docker containers provide isolated environments for running applications without the overhead of traditional virtual machines.

- **Astro CLI**: Astro CLI is a command-line interface designed for managing and deploying data workflows within your data engineering ecosystem. It streamlines the orchestration of complex data tasks and workflows, similar to how a conductor manages an orchestra, ensuring that each data task is executed in the correct sequence and dependencies are effectively handled.

- **Soda**: Soda is a data quality monitoring tool that helps you maintain the integrity of your data. It allows you to set up and run automated data quality checks to detect and alert you to anomalies or issues in your data pipelines. Soda ensures that your data meets quality standards throughout the ETL process, just like a quality control system in manufacturing.

- **Hadoop (HDFS)**: Hadoop is an open-source framework designed for storing and processing large volumes of data across distributed clusters. The Hadoop Distributed File System (HDFS) is a key component of Hadoop, providing scalable and fault-tolerant storage by breaking data into blocks and distributing them across multiple nodes. This architecture ensures high availability and efficient data management, making it ideal for handling big data workloads.

- **Power BI Desktop**: Power BI Desktop is a powerful business intelligence tool from Microsoft that enables users to create interactive reports and visualizations. It provides a user-friendly interface for connecting to various data sources, transforming data, and building insightful dashboards. With its robust data modeling and visualization capabilities, Power BI Desktop helps organizations turn raw data into actionable insights, facilitating better decision-making and data-driven strategies.

- **Apache Airflow**: Apache Airflow is a workflow automation tool that allows you to define, schedule, and monitor complex data workflows. It acts like a task scheduler for your data engineering processes, ensuring that each step in your pipeline is executed in the correct order and dependencies are managed efficiently.

- **Data Build Tools (DBT)**: DBT is a data transformation tool that enables you to build and manage your data models using SQL. It facilitates transformations and data modeling within your data warehouse, integrating with workflow orchestrators like Airflow to automate the execution of data transformation tasks and ensuring that your data is ready for analysis.


# **2. Data Architecture**

## 2.1. Conceptual Architecture
![Items (1)](https://github.com/thanhphat2609/Global_Super_Store/assets/84914537/600e237e-01d7-4c09-891c-1551acfbc45e)

- **Data Source**: These include the various systems from which data is **extracted**, such as: Relational Database, File systems, SaaS applications, Real-time data.
- **Staging**: Extract data from Source into Files of Lakehouse (csv, parquet) or Delta Tables.
- **Data Warehouse**: Data in the data warehouse is organized according to a unified data model, which makes it easy to query and analyze.
- **Analytics**: This last step we will use tools and techniques to analyze the data in the data warehouse, such as: Power BI, Tableau, ..

## 2.2. Physical Architecture
![dockerarchitecture](https://github.com/user-attachments/assets/9251b5b8-a0af-42e6-a681-b1bf8d6115d3)

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


# **4. Data Pipeline**

## Build Data Pipeline

Not Updated Yet

## Result of Pipeline

Not Updated Yet

# **5. Report**

## 5.1. Data Modelling

Not Updated Yet

## 5.2. Report

Not Updated Yet