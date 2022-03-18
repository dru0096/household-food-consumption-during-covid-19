def two_sample_test_upgraded(df, samples, food_cat = None, year_1 = None, year_2 = None, alpha = 0.05):

    if ( food_cat == None ): # Do the analysis for every food_cat
        if ( ( year_1 == None) and ( year_2 == None ) ): # Do the analysis for all the years
            for row in range(df.shape[0]):
                print("Considering goods: {}".format(df.iloc[row,1]))
                for col in range(3,df.shape[1]-1):
                    print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                    print()
                    two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        elif ( ( year_1 != None) and ( year_2 == None ) ): # Do the analysis from pairs of years starting from year_1
            for row in range(df.shape[0]):
                print("Considering goods: {}".format(df.iloc[row,1]))
                year_1_index = list(df.columns).index(year_1)
                for col in range(year_1_index, df.shape[1]-1):
                    print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                    print()
                    two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        elif ( ( year_1 == None ) and ( year_2 != None ) ): # Do the analysis from first year until year_2
            for row in range(df.shape[0]):
                print("Considering goods: {}".format(df.iloc[row,1]))
                year_2_index = list(df.columns).index(year_2)
                for col in range(3, year_2_index):
                    print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                    print()
                    two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        else:  # Do the analysis between year_1 and year_2
            for row in range(df.shape[0]):
                print("Considering goods: {}".format(df.iloc[row,1]))
                year_1_index = list(df.columns).index(year_1)
                year_2_index = list(df.columns).index(year_2)
                for col in range(year_1_index, year_2_index):
                    print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                    print()
                    two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
    else: # Do the analysis for only one food_cat
        if ( (year_1 == None) and ( year_2 == None) ): # Do the analysis for all the years
            row = list(df.iloc[:,1].values).index(food_cat)
            food_cat=list(hshld_food_consumption.iloc[:,1].values)
            print("Considering goods: {}".format(df.iloc[row,1]))
            for col in range(3,df.shape[1]-1):
                print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                print()
                two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        elif ( ( year_1 != None) and ( year_2 == None) ): # Do the analysis from pairs of years starting from year_1
            row = list(df.iloc[:,1].values).index(food_cat)
            food_cat=list(hshld_food_consumption.iloc[:,1].values)
            print("Considering goods: {}".format(df.iloc[row,1]))
            year_1_index = list(df.columns).index(year_1)
            for col in range(year_1_index, df.shape[1]-1):
                print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                print()
                two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        elif ( ( year_1 == None ) and ( year_2 != None) ): # Do the analysis from first year until year_2
            row = list(df.iloc[:,1].values).index(food_cat)
            food_cat=list(hshld_food_consumption.iloc[:,1].values)
            print("Considering goods: {}".format(df.iloc[row,1]))
            year_2_index = list(df.columns).index(year_2)
            for col in range(3, year_2_index):
                print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                print()
                two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)
        else: # Do the analysis between year_1 and year_2
            row = list(df.iloc[:,1].values).index(food_cat)
            print("Considering goods: {}".format(df.iloc[row,1]))
            year_1_index = list(df.columns).index(year_1)
            year_2_index = list(df.columns).index(year_2)
            for col in range(year_1_index, year_2_index):
                print("Considering years {} and {}".format(df.columns[col],df.columns[col+1]))
                print()
                two_sample_calculations(df, samples, row = row, col = col, alpha = alpha)