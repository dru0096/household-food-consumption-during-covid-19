def two_sample_calculations(df, samples, row, col, alpha = 0.05):
    XA = df.iloc[row,col+1]
    NA = samples[df.columns[col+1]]
    XB = df.iloc[row,col]
    NB = samples[df.columns[col]]
    d = (XA/NA) - (XB/NB)           
    sigma2 = (((XA + XB)/(NA + NB))/NA) + (((XA + XB)/(NA + NB))/NB)
    statistic = d/np.sqrt(sigma2)
    p_value=(1-scipy.stats.norm.cdf(statistic))
    positive_critical_value = scipy.stats.norm.ppf(1-(alpha/2))
    negative_critical_value = -scipy.stats.norm.ppf(1-(alpha/2))
    if ( (statistic < positive_critical_value) and (statistic > negative_critical_value) ):
        print("We accept the null Hypothesis and we can confidently say that both means are the same")
        print("The statistic is",statistic)
        print("The positive critical value is",positive_critical_value)
    else:
        print("We reject the null Hypothesis and we can confidently say that both means are different")
        print("The statistic is",statistic)
        print("The positive critical value is",positive_critical_value)
        print()