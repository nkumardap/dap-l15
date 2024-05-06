"""
In this assignment we're going to plot the US debt to GDP ratio
using data we programmatically download via the FRED API.
"""

"""
EXERCISE 1

Short: Download the GDP time series for 1970-2023

Long: Find the FRED data series called "Gross Domestic Product" and look up the
abbreviation.(Note that this is NOT the real GDP, which is adjusted for 
inflation.) Download it using DataReader.

(Note that there are some "clean up" steps that you will have to do. You'll need 
to create a year variable for the purpose of merging later but the DATE variable 
will become the index. Hint: look up the reset_index() function.

Renaming the columns so they are more descriptive would be of benefit to you.)
"""

"""
EXERCISE 2

Short: Download the debt time series for 1970-2023

Long: Find the series called "Federal Debt: Total Public Debt" and download it
via DataReader.

(Similar clean up steps are involved, except that this is quarterly data, ao there 
are 4 entries per year. You'll have to get rid of the duplicates for a year 
using drop_duplicates().)
"""

"""
EXERCISE 3

Short: Merge the two datasets and create a debt-to-gdp time series.

Long: This is just debt/gdp for each year. Note that debt and GDP are recorded 
using different units and remember to adjust for that!
"""

"""
EXERCISE 4 (BONUS)

Plot the debt-to-gdp ratio over time. Include a red line for when the
ratio crossed 1.00
"""