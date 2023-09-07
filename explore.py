import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

#this function creates a count plot bar chart with a count as the y-axis(categorical to categorical)
def countplt(df, target, feature):
    
    sns.countplot(data = df, x = feature, hue = target)
    
    return plt.show()


#this function creates a cat plot bar chart with a count as the y-axis(numerical to categorical)
def catplt(df, target, feature):
    
    sns.catplot(data= df, x= target, y= feature, kind = 'bar')
    
    return plt.show()


#this function applies pearson r correlation test and returns values
def corr(x, y):

    corr, p = stats.pearsonr(x, y)

    return corr, p


#this function applies chi-squared test and prints out values and conclusion
def chi(df, target, feature):
    
    cross_tab = pd.crosstab(df[target], df[feature])

    chi2_stat, p_val, dof, expected = stats.chi2_contingency(cross_tab)

    print("Chi-Square Statistic:", chi2_stat)
    print("P-value:", p_val)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)
    print('')

    if p_val < 0.05:
    
        print("Conclusion: There is a significant association between the variables. We reject the null hypothesis")

    else:
    
        print("Conclusion: There is no significant association between the variables. we fail to reject the null hypothesis")

        
#this function applies a one sample two tailed t-test and prints values and conclusions
def one_samp_t(sample, overall_mean):

    t, p = stats.ttest_1samp(sample, overall_mean)

    print(t, p/2)
    print('')

    a =.05

    if p/2 > a:
    
        print("Conclusion: We fail to reject the null hypothesis.")

    elif t < 0:
    
        print(" Conclusion: We fail to reject null hypothesis.")

    else:
    
        print("Conclusion: We reject the null hypothesis.")