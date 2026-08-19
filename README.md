# 🛒 E-Commerce Sales Data Engineering Pipeline

An end-to-end **E-Commerce Data Engineering Pipeline** built using **Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, PySpark, Apache Spark, and SQL**.

The project demonstrates how raw e-commerce data can be ingested, stored, cleaned, validated, transformed, and converted into analytical datasets using a modern cloud-based data engineering architecture.

---

## 📌 Project Overview

This project implements a complete data engineering workflow for processing e-commerce sales data.

The source data consists of customer, order, product, order-item, and payment information. The pipeline ingests raw data into **Azure Data Lake Storage Gen2**, processes it using **Azure Data Factory and Databricks**, performs data cleaning and quality validation using **PySpark**, and creates curated datasets for analytical processing using **SQL**.

### Main Objectives

- Ingest raw e-commerce datasets into Azure Data Lake Storage.
- Build an automated data ingestion pipeline using Azure Data Factory.
- Organize data using a Bronze, Silver, and Gold architecture.
- Clean and transform data using PySpark and Apache Spark.
- Perform data quality and validation checks.
- Handle missing values and duplicate records.
- Join customer, order, product, order-item, and payment data.
- Create analytical datasets for business reporting.
- Perform sales, customer, product, payment, and delivery analysis using SQL.

---

# 🏗️ Architecture

The project follows a modern **Medallion Architecture**.

```text
                         ┌─────────────────────┐
                         │   Kaggle Dataset    │
                         │                     │
                         │ Customers           │
                         │ Orders              │
                         │ Order Items         │
                         │ Products            │
                         │ Payments            │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Azure Data Factory  │
                         │                     │
                         │ Data Ingestion      │
                         │ Pipeline            │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │ Azure Data Lake Storage Gen2   │
                    │                                │
                    │         RAW / BRONZE           │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Azure Databricks    │
                         │                     │
                         │ Apache Spark        │
                         │ PySpark             │
                         │ Data Cleaning       │
                         │ Data Transformation │
                         │ Data Quality        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │              SILVER             │
                    │                                │
                    │ Cleaned & Validated Data       │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Gold Layer        │
                         │                     │
                         │ Sales Analytics     │
                         │ Customer Analytics  │
                         │ Product Analytics   │
                         │ Payment Analytics   │
                         │ Delivery Analytics  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     SQL Analytics   │
                         │                     │
                         │ Business Insights   │
                         │ KPI Analysis        │
                         └─────────────────────┘
