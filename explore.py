import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats



def bar_plt4(df, feature, target):
    '''
    This function is specifically to create a bar chart for county and tax value.
    
    Parameters:
    df = data
    feature = df.column
    target = target variable
    '''
    
    #create the bar plot
    ax = sns.barplot(data = df, x = feature, y = target, errorbar = None, color = 'skyblue', width = .9)
    ax = plt.gca()
    for p in ax.patches:
        # Get the height (value) of each bar
        value = int(p.get_height())  
        # Exclude zero values
        if value != 0:  
            # Format value with commas
            label = f"${value:,}"  
            # Customize the labels
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontsize = 8)
    
    #create labels
    plt.xlabel('County')
    plt.ylabel('Tax Value')
    
    #remove y-axis and borders
    plt.yticks([])
    sns.despine(ax=ax, left=True, bottom=True)
    ax.yaxis.set_visible(False)
    
    #set title for chart
    plt.title("Average tax value", y= 1.10)
    plt.show()



def bar_plt3(df, feature, target):
    '''
    This function is specifically to create a bar chart for decade and tax value.
    
    Parameters:
    df = data
    feature = df.column
    target = target variable
    '''
    
    #create the bar plot
    ax = sns.barplot(data = df, x = feature, y = target, errorbar = None, color = 'skyblue', width = .9)
    ax = plt.gca()
    for p in ax.patches:
        # Get the height (value) of each bar
        value = int(p.get_height())  
        # Exclude zero values
        if value != 0:  
            # Format value with commas
            label = f"${value:,}"  
            # Customize the labels
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontsize = 8)
    
    new_labels = ['<=1950', '1960', '1970', '1980', '1990', '2000', '2010']
    plt.xticks(range(len(new_labels)), new_labels)
    
    #create labels
    plt.xlabel('Decade')
    plt.ylabel('Tax Value')
    
    #remove y-axis and borders
    plt.yticks([])
    sns.despine(ax=ax, left=True, bottom=True)
    ax.yaxis.set_visible(False)
    
    #set title for chart
    plt.title("Average tax value", y= 1.10)
    plt.show()



def bar_plt2(df, feature, target):
    '''
    This function is specifically to create a bar chart for square ft and tax value.
    
    Parameters:
    df = data
    feature = df.column
    target = target variable
    '''
    
    #create the bar plot
    ax = sns.barplot(data = df, x = feature, y = target, errorbar = None, color = 'skyblue', width = .9)
    ax = plt.gca()
    for p in ax.patches:
        # Get the height (value) of each bar
        value = int(p.get_height())  
        # Exclude zero values
        if value != 0:  
            # Format value with commas
            label = f"${value:,}"  
            # Customize the labels
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontsize = 8)
    
    new_labels = ['1000', '1500', '2000', '2500', '3000', '3500', '3600+']
    plt.xticks(range(len(new_labels)), new_labels)
    
    #create labels
    plt.xlabel('Square Ft')
    plt.ylabel('Tax Value')
    
    #remove y-axis and borders
    plt.yticks([])
    sns.despine(ax=ax, left=True, bottom=True)
    ax.yaxis.set_visible(False)
    
    #set title for chart
    plt.title("Average tax value", y= 1.10)
    plt.show()
    
    
    
def bar_plt(df, feature, target):
    '''
    This function is specifically to create a bar chart for total rooms and tax value.
    
    Parameters:
    df = data
    feature = df.column
    target = target variable
    '''
    
    #create the bar plot
    ax = sns.barplot(data = df, x = feature, y = target, errorbar = None, color = 'skyblue', width = .9)
    ax = plt.gca()
    for p in ax.patches:
        # Get the height (value) of each bar
        value = int(p.get_height())  
        # Exclude zero values
        if value != 0:  
            # Format value with commas
            label = f"${value:,}"  
            # Customize the labels
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontsize = 8)
    
    new_labels = ['3', '4', '5', '6', '7+']
    plt.xticks(range(len(new_labels)), new_labels)
    
    #create labels
    plt.xlabel('Total Rooms (bed & bath)')
    plt.ylabel('Tax Value')
    
    #remove y-axis and borders
    plt.yticks([])
    sns.despine(ax=ax, left=True, bottom=True)
    ax.yaxis.set_visible(False)
    
    #set title for chart
    plt.title("Average tax value", y= 1.10)
    plt.show()
    

    
def spear_test(df, continuous, continuous2):
    '''
    This function calls the spearmanr() function from stats and conducts a statistical test on two continuous variables to determine correlation.
    
    Parameters:
    df = data
    continuous = continuous feature
    continuous2 = second continuous feature
    '''
    
    r, p = stats.spearmanr(df[continuous], df[continuous2])

    print('a = .05')
    print(f'r = {r}')
    print(f'p = {p}')
    
    print('')
    
    a = .05

    if p < a:

        print('We reject the null hypothesis')

    else:

        print('We fail to reject the null hypothesis')



def corr(x, y):
    '''
    This function applies pearson r correlation test and determines correlation between features.
    
    Parameters:
    x = df.column
    y = df.column2
    '''

    corr, p = stats.pearsonr(x, y)
    
    a = .5
    
    if p < a:
        
        print('We reject the null hypothesis')
    
    else:
        
        print('We fail to reject the null hypothesis')

