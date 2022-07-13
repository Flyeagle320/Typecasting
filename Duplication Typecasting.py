# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:43:50 2022

@author: Rakesh
"""
#lets import pandas package for data manipulation##

import pandas as pd
import seaborn as sns

##loading dataset##
retail = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/OnlineRetail.csv',header=0,encoding='unicode_escape')
##to find null or NA value##
retail.info()

retail.describe() ###to find mean , min and max ##

## lets check for count of NA in columns##
retail.isna().sum()
retail.isnull().sum()

## for mean ,median mode imputation we can use simple imputer or df.fillna()
from sklearn.impute import SimpleImputer
import numpy as np

#mode imputer##
mode_imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
retail["CustomerID"] = pd.DataFrame(mode_imputer.fit_transform(retail[["CustomerID"]]))
retail["Description"] = pd.DataFrame(mode_imputer.fit_transform(retail[["Description"]]))
retail.isnull().sum()

retail.dtypes

#typecasting##
## Convertingfrom Float64 to int64##

retail.UnitPrice = retail.UnitPrice.astype('int64')
retail.CustomerID = retail.CustomerID.astype('int64')

retail.dtypes

retail.nunique()

##Duplicate identification in the Data##
duplicates = retail.duplicated()
sum(duplicates)

#Lets Remove duplicates##
retail1 = retail.drop_duplicates()

retail1.dtypes
retail1.nunique()

##################################EDA############################
##measure of central tendency##############
#mean#
retail1.Quantity.mean()
retail1.UnitPrice.mean()
#median##
retail1.Quantity.median()
retail1.UnitPrice.median()

##Measure of Dispersion#
#Variance##
retail1.Quantity.var()
retail1.UnitPrice.var()
##Standard Deviation##
retail1.Quantity.std()
retail1.UnitPrice.std()
#range
range_Quantity = max(retail1.Quantity)- min(retail1.Quantity)
range_Quantity

range_UnitPrice = max(retail1.UnitPrice)- min(retail1.UnitPrice)
range_UnitPrice

##Skewness##
retail1.Quantity.skew()
retail1.UnitPrice.skew()

##Kurtosis##
retail1.Quantity.kurt()
retail1.UnitPrice.kurt()

retail1.dtypes
retail.columns

##Now lets see data using boxplot##

boxplot = retail1.boxplot(column=['Quantity', 'UnitPrice','CustomerID'])

##Let see using scatterplot#
import seaborn as sns

sns.pairplot(retail1.iloc[ :, : ])














