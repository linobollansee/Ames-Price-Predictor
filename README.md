# Ames-Price-Predictor

Welcome to the Ames-Price-Predictor repository! This project is designed to help a friend maximize the sale price of inherited properties in Ames, Iowa, by leveraging data analysis and predictive modeling.

## Table of Contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
   - [Render](#render)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)
   - [Content](#content)
   - [Media](#media)
- [Acknowledgements](#acknowledgements)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

* We want a ML model to predict

* Our ideal outcome is to

* The model success metrics are

* The model output is

* Heuristics

* The training data

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Render

* The App live link is: <https://milestone-project-heritage-housing-issues.onrender.com>
* The project was deployed to Render using the following steps.

1. Log in to Render.com using Github.
2. Click on the New button, select Web Service.
2. At Source Code, select Git Providor.
3. Select your repository name. Click Connect.
4. Enter a unique name for your web service.
5. Select the Python3 language.
6. Select the main branch.
7. Select the Frankfurt (EU Central) Region.
8. Set the Build Command: `pip install -r requirements.txt && ./setup.sh`
9. Set the Start Command: `streamlit run app.py`
10. Set Instance Type: Free
11. Set the Environment Variables: `Key: PORT` `Value: 8501` and `Key: PYTHON_VERSION` `Value: 3.11.11`
12. Click Deploy Web Service

## Main Data Analysis and Machine Learning Libraries

* numpy==1.26.1
  * Provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
* pandas==2.1.1
  * A powerful data manipulation and analysis library, providing data structures like DataFrames for handling structured data.
* matplotlib==3.8.0
  * A plotting library used for creating static, animated, and interactive visualizations in Python.
* seaborn==0.13.2
  * Built on top of matplotlib, seaborn makes it easier to generate more attractive and informative statistical plots.
* ydata-profiling==4.12.0
  * Generates detailed data profiling reports, offering insights into the structure and statistics of datasets for exploratory data analysis.
* plotly==5.17.0
  * An interactive graphing library for creating visualizations in the form of charts, maps, and dashboards with support for web-based interactivity.
* ppscore==1.1.0 
  * A library for calculating feature importance scores in machine learning models, especially useful for feature selection.
* streamlit==1.40.2
  * An open-source app framework to quickly build and deploy interactive data science and machine learning web applications.
* feature-engine==1.6.1
  * A library for feature engineering in machine learning, providing tools for preprocessing, feature transformation, and handling missing data.
* imbalanced-learn==0.11.0
  * Provides algorithms to address class imbalance in datasets for classification tasks, including over-sampling and under-sampling techniques.
* scikit-learn==1.3.1
  * A robust library for machine learning that provides tools for classification, regression, clustering, model selection, and data preprocessing.
* xgboost==1.7.6
  * A highly efficient and scalable implementation of gradient boosting for classification and regression tasks, known for its high performance in competitions.
* yellowbrick==1.5
  * A visual analysis tool that provides diagnostic visualizations to aid in model evaluation, feature analysis, and hyperparameter tuning.
* Pillow==10.0.1
  * A Python Imaging Library (PIL) fork, which adds image processing capabilities to Python, such as opening, editing, and saving images in various formats.

## Credits

* Code Institute Community Lead Kenan Wright for putting me in touch with the tutors most suited for this project: Niel McEwen and Roman Rakic.
* Code Institute Tutor Niel McEwen for providing documentation to deploy a Streamlit application to the Render cloud platform.
* Code Institute Student Filip van Elslande for discussing some of the capabilities of the python libraries used in this project.
* Code Institute Mentor Mo Shami for project support.
* ChatGPT for quickly refreshing my memory about Python syntax.

### Content

* The Code Institute Milestone Project Heritage Housing Issues Template available at [https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues) was used to start this project. 
 
* The Code Institute churnometer repository at [https://github.com/Code-Institute-Solutions/churnometer](https://github.com/Code-Institute-Solutions/churnometer) was used for learning how to do the Jupyter notebooks and Streamlit pages in this project.

* The Code Institute Predictive Analytics course taught me all the skills required to complete this project.

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements

* Amazon for delivering to my doorstep many ready-made meals, allowing me to dedicate more time on project research and coding solutions.

