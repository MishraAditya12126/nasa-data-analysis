import pandas as pd

df = pd.read_csv('cleaned_5250.csv')

class Preprocessor:
    def __init__(self,df):
        self.df = df

    def planets_list(self,plnt_type):
        return self.df[df['planet_type'] == plnt_type]['name'].unique().tolist()

    def plnts_each_year(self):
        td = self.df.groupby(['discovery_year','detection_method'])['name'].count().reset_index().sort_values(by=['discovery_year'])
        td.rename(columns={'discovery_year':'Discovery year','detection_method':'Detection method','name':'Count'},inplace=True)
        return td
    def plnt_type_count(self):
        td = self.df['planet_type'].value_counts().reset_index()
        td.rename(columns={'index':'Planet type','planet_type':'Count'},inplace=True)
        return td
    def detection_method_cnt(self):
        td = self.df['detection_method'].value_counts().reset_index()
        td.rename(columns={'index':'Detection Method','detection_method':'Count'},inplace=True)
        return td
