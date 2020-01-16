## Correlations between poverty, food environment and diabetes

### Problem statement
 During the past two decades, the number of American adults diagnosed with diabetes has more than doubled as the population has aged and become more overweight or obese. Often a healthy lifestyle (healthy diet, regular physical activity, maintaining a normal body weight and avoiding tobacco use) is the recommended measure to prevent or delay the onset of type 2 diabetes (the most common type of diabetes). Meanwhile, worldwide the prevalence of diabetes has increased more rapidly in middle- and low- income countries, suggesting a potential link between financial well-being and diabetes rate.   
 
 Although economic status and healthy lifestyle are not independent from each other, by far it is not clear which is a stronger predictor of the prevelance of diabetes rate. While it is difficult to directly gather information and assess the healthiness of people's lifestyles, residents' chances of maintaining a healthy diet and physical activity can be informed by the local food and fitness environment such as the diversity and/or abundance of grocery stores, farmer's markets and fitness facilities.   
 
 In this project, we will utilize the 
[Food_Environment_Atlas_database](https://www.ers.usda.gov/data-products/food-environment-atlas/) to answer these questions:    
 
 - Which is a stronger predictor of adult diabetes rate in the United States, economic status or food and fitness environment  
 - Will the conclusions change if we group the counties by urbanity (metro vs. non-metro counties) and poverty level (persisten-poverty vs. non-poverty)?  
 
 In addition, we will also explore potential patterns of economic status and food environment among the counties.For example,  which areas are featured by high concentration of farmers' markets or convenience stores?   
 
 Conclusions of this project could be useful to government agencies, city planners, policy makers and local communities that want to promote a healthier food environment. Local food producers, grocery stores and companies in the health and wellness industry may also be interested.   
 
### Methods
A suite of machine learning algorithms will be used to address the above questions, including:  

 Predicting Diabetes (Supervised learning models)
 - Linear regression 
 - Decision Trees
 - Random Forest
 - XGBoost     

 Finding patterns of economic and food environment among counties (unsupervised learning models)
 - PCA
 - K-means clustering  
 
### Files
Code can be accessed here: [Final_food-poverty-diabetes.ipynb](https://github.com/BrachyS/food-env-atlas/blob/master/Final_food-poverty-diabetes.ipynb)  
Data file: [data_atlas](https://github.com/BrachyS/food-env-atlas/tree/master/data_atlas)    
Final report:  
Presentation slides:

(Author's note: This is the first capstone project completed for my Data Science training with the **Springboard Data Science Career Track** education program.)  

 