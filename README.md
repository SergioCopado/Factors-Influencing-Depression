# Factors-Influencing-Depression: Semantic Web and Linked Data Project

## Overview
This project explores the influence of various social, economic, and political factors on mental health issues, specifically focusing on depression across different countries. Using Semantic Web technologies and Linked Data principles, we analyze key data related to mental health, aiming to identify the main factors that may contribute to the prevalence of depression. This work combines heterogeneous datasets from various sources, including DBpedia, to create an enriched view of these factors using a custom ontology.

## Objectives
The primary objectives of this project are:

1. To investigate potential correlations between depression and a country's economic, demographic, and political metrics.
2. To gather, clean, and integrate data from diverse sources, aiming for consistency and ease of access.
3. To apply Semantic Web principles, constructing an ontology that represents relevant factors influencing depression.
4. To facilitate intuitive user access to the data through a Python-based interface and interactive visualizations.

## Case Study
We selected various countries with available data on:

1. **Democracy levels** (using democratic scores and rankings)
2. **Economic indicators** (GDP per capita, Gini coefficient)
3. **Demographic factors** (population density, human development index)

The selected data focuses on 2022, the year with the most comprehensive and accurate data. Our data model centers on the following key classes and subclasses:

1. Zone and Country (linked via object properties).
2. Metrics class with sub-classes for each type of metric, including:
  * **Gini Coefficient:** Income inequality measure.
  *  **Population Density:** Number of residents per square kilometer.
  * **Depression Rate:** Percentage of people with depression in a country.
  * **Human Development Index:** Measures life expectancy, education level, and living standards.
  * **GDP per Capita:** National GDP divided by population.
  * **Political Regime and Democracy Score.**

## Ontology Development
Our ontology enables the integration of multiple datasets linked by key indicators. The process involves:

1. **Data Cleaning:** Using Python’s pandas to clean data, replacing spaces with underscores in CSV columns.
2. **Data Enrichment:** Extracting data from DBpedia using SPARQL queries and converting data types to match the ontology requirements.
3. **Mapping:** Creating triple maps for each key class and linking each with the appropriate data properties and object properties.
4. **Output:** Generating RDF data using Helio Playground, then importing the Turtle files into GraphDB for query processing.

## GraphDB Integration
Data was stored and queried within GraphDB, using the following process:

1. Create a Repository in GraphDB named semantic-web-project.
2. Import Data in Turtle format, configuring the repository for efficient querying.
3. Run Queries on the imported data to analyze and visualize correlations between factors.
   
## Application Interface
We developed a Python interface for user-friendly access to the data, enabling:

* Data Visualization: General data statistics and prevalence rates by country and factor.
* Country-Specific Queries: Retrieve all data for a selected country.
* Variable Comparisons: Generate visual comparisons between any two variables.
* Correlation Analysis: Display heatmaps showing correlation among all variables using Pearson coefficients.
* User Options:
  * 1 Visualize general data (e.g., country count by regime type, depression prevalence).
  * 2 View data for a specific country.
  * 3 Compare two user-selected variables.
  * 4 Display all-variable correlations as a heatmap.
  * 5 List all countries in the dataset.
  * 99 Exit.
        
## Key Findings
Our findings suggest that:

The Human Development Index correlates with higher depression prevalence. However, this relationship is complex and influenced by numerous external factors, such as seasonal sunlight exposure, social structure, and healthcare infrastructure.
Results are not conclusive for all countries, as data availability and mental health diagnostic capabilities vary significantly.

## Conclusions
Our analysis highlights the multifactorial nature of depression, cautioning against oversimplified interpretations of data correlations. In under-resourced countries, mental health diagnoses are limited, impacting data accuracy. Further studies are needed to deepen understanding of these relationships.
