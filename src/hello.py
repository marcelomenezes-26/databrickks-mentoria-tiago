# Databricks notebook source
print("Hello world")

# COMMAND ----------

date_ingestion = dbutils.widgets.get("date_ingestion")
print(date_ingestion)
