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
  1. **Gini Coefficient:** Income inequality measure.
  2. **Population Density:** Number of residents per square kilometer.
  3. **Depression Rate:** Percentage of people with depression in a country.
  4. **Human Development Index:** Measures life expectancy, education level, and living standards.
  5. **GDP per Capita:** National GDP divided by population.
  6. **Political Regime and Democracy Score.**
