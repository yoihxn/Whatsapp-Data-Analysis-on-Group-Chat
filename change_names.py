import pandas as pd

def replace_member_names(df):
    replace_dict = {
        #make pairs of names and aliases according to your own group
    }
    
    df['member'] = df['member'].replace(replace_dict)
    return df