import pandas as pd
import glob
#df = pd.read_csv("~/Dropbox/MLB/mlbam_pitch_20190901.csv", index_col=0)

mlbpathPattern = r"/Users/eijioga/Dropbox/MLB/*_pitch*.csv"
filelist = glob.glob(mlbpathPattern)

dflist = []
for afile in filelist:
    print(afile)
    dflist.append(pd.read_csv(afile, index_col=0))
print(dflist)

df = pd.concat(dflist)
print(df.describe())

"""
print(df.describe())
print(df.info())
print(df.head(10))
print(df.columns)
#print(df[df["park_name"]].info())
"""
parkList = []
parkList = sorted(df.park_name.unique())
df.park_name.unique()
for p in parkList:
    print(p)
print(len(parkList))
