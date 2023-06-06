![](https://github.com/Pking31/Movies/blob/da48144328560bcbeae3764485ade057233991fa/imag/logo1.JPG)

# Movies
Analysis and recomendation system(ML).
## Content description
- "Moviesdas.pbix" Dashboard on Power BI.
- Folder "datasets" : contains all the databases resulting from the cleaning of the original database.
- Folder "imag" : contains images used in readme.md.
- "main.py" : is a required file for the query API. Contains the main code to run the API and handle queries
- "Step_1 Transformations and Unnesting": is a notebook that describes the steps followed to perform transformations and unnesting on the original dataset ("movies_dataset.csv") to get all the csv in "datasets".
- "Step_2 EDA and ML": it is a python file where an Exploratory Data Analysis is carried out taking into account the implementation of a recommendation model.
- "Step_3 Creation of functions": it is a python file where the functions used by the API are created and tested.
## Role to develop
In my role as a Data Scientist in this streaming platform aggregation service start-up, I have taken on the responsibility of creating a recommendation system as my first Machine Learning project. However, when reviewing the available data, I have realized that the quality and structure of the data are very poor. This includes nested data and missing transformations. This situation has greatly hindered my work as a Data Scientist.
In order to overcome these challenges and achieve an MVP (Minimum Viable Product), I have decided to take on the additional role of Data Engineer. My main goal is to do some fast Data Engineering work to improve data maturity and establish a solid foundation for the recommender system. Next, I detail the tasks and responsibilities that I have assumed:
## Analysis and understanding of data:
I conducted a thorough analysis of the available data to understand its structure, quality and characteristics. I identified the deficiencies and areas for improvement, as well as the specific requirements necessary to develop an effective recommendation system. SEE (ETL).
## Data transformation and cleansing:
Implemented data transformation and cleansing processes to address identified deficiencies. This included data normalization, outlier correction, nested data resolution, and any other transformations needed to improve the quality and utility of the data.
## Unnesting of nested fields:
To be able to use the fields "belongs_to_collection", "production_companies" among others, it was required to un-nest them. This involved extracting the values from dictionaries or lists present in each row and rejoining them to the dataset. If it was not necessary to unstack them, an alternative was sought to access these data without the need to unstack them.
## Null values:
The "revenue" and "budget" fields that had null values have been filled with the number 0. This ensured that there were no missing values in these fields and made it easier to calculate ROI.
## Removing null values in the "release_date" field:
Records that had null values in the "release_date" field were removed. This ensured that all records had a valid and consistent release date.
## Date format and column creation "release_year":
The date values in the "release_date" field have been changed to the format YYYY-mm-dd. In addition, a new column called "release_year" was created where the year of the release date was extracted.
## ROI column creation:
A column called "return" was created where the return on investment was calculated by dividing the "revenue" and "budget" fields. If there were no data available for the calculation, the value 0 was assigned.
## Removing unused columns:
The "video", "imdb_id", "adult", "original_title", "vote_count", "poster_path" and "homepage" columns that will not be used in the project have been removed from the dataset. This allowed us to reduce the size of the dataset and optimize performance.
These transformation requirements have been focused on achieving a functional MVP quickly and efficiently. Once done, the necessary transformations were carried out to prepare the data and advance in the implementation of the recommendation system.

## Exploratory Data Analysis (EDA)
![Dashboard Power BI|100](https://github.com/Pking31/Movies/blob/aeb92ba0a72968763ff8d029119d9a6f03179251/imag/BI.JPG)
 An exploratory analysis of the data has been carried out after having cleaned them. During the analysis, the relationships between the dataset variables have been investigated, outliers or anomalies have been identified, and interesting patterns have been discovered that could be useful in further analysis. 
To explore data was created a dashboard on POWER BI, you can check it out in "Moviedas.pbix".

One of the prominent visualizations in the EDA is the word cloud, which shows the most frequent words in movie titles. This information could be used to improve the recommendation system.See (EDA and ML)




