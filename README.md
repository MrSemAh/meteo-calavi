# meteo-calavi
Predict the maximum temperature the next day in Abomey-Calavi (Latitude ~ 6.44, Longitude ~ 2.34)

## Problem
Being able to predict the max temperature of the next day using a set of data.
For this pretext project we'll be wor

## Data sources
- Open-Meteo

## Methodology

## Results

## Limits

## Notes
- We defined a data cleaning method in order to be consistent with the ML pipeline
- Daily aggregates provided by Open-Meteo were deliberately recalculated in order to control the feature engineering pipeline
- **Baseline** : We first assume a simple baseline of having the same temperature at J+1 than J

### Simple Linear Regression
Using linear regression on all columns of dataset including J-1 temperature, we have been able to get a lower mean error than the one with the baseline thus going from ~0.78 to ~0.72.

### Linear Regression with lags
Knowing that temperature highly depends on previous days weather and not only the day before, we've enriched our dataset with data from `day-1`, `day-2` and `day-3` data for some of the columns. This maneuver allow us to have a ~20% error reduction. We've been able to obtain under 0.64 mean error.
