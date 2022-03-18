def year_differences_any_category(df, row):
    df2 = df.copy()
    #print("Considering goods: {}".format(df2.iloc[row,1]))
    df3=pd.DataFrame(df2.iloc[row,3:])
    df3.columns = ["Original"]
    df3["Shifted"] = df3["Original"].shift(1)  #Add a new column with column 0 shifted 1 level down
    df3['diff'] = df3["Shifted"] - df3["Original"] #Add a difference column to show difference year on year for category
    df3.reset_index(inplace=True)
    df3.rename(columns={'index':'year'}, inplace = True)
    return df3
