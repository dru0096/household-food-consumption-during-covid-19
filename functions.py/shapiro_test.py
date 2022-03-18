def shapiro_test(df):
    shapiro_test = scipy.stats.shapiro(df[df['diff'].isna() == False]['diff'])
    shapiro_statistic= shapiro_test.statistic
    
    shapiro_pval= shapiro_test.pvalue

    if (shapiro_test.pvalue > 0.05 ):
        print("The data doesn't follow a normal distribution")
        print("The means are changing")
        print("The shapiro statistic is",shapiro_statistic)
        print("The shapiro p-value is",shapiro_pval)
    else:
        print("The data follows a normal distribution")
        print("The shapiro statistic is",shapiro_statistic)
        print("The shapiro p-value is",shapiro_pval)