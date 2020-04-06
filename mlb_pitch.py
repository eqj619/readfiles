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

Index(['year', 'month', 'day', 'st_fl', 'regseason_fl', 'playoff_fl',
       'game_type', 'game_type_des', 'local_game_time', 'game_id',
       'home_team_id', 'away_team_id', 'home_team_lg', 'away_team_lg',
       'interleague_fl', 'park_id', 'park_name', 'park_location',
       'inning_number', 'bat_home_id', 'outs_ct', 'pit_mlbid',
       'pit_first_name', 'pit_last_name', 'pit_box_name', 'pit_hand_cd',
       'bat_mlbid', 'bat_first_name', 'bat_last_name', 'bat_box_name',
       'bat_hand_cd', 'ab_number', 'start_bases', 'end_bases', 'event_outs_ct',
       'pa_ball_ct', 'pa_strike_ct', 'pitch_seq', 'pa_terminal_fl',
       'pa_event_cd', 'pitch_res', 'pitch_des', 'pitch_id', 'x', 'y',
       'start_speed', 'end_speed', 'sz_top', 'sz_bot', 'pfx_x', 'pfx_z', 'px',
       'pz', 'x0', 'y0', 'z0', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az',
       'break_y', 'break_angle', 'break_length', 'pitch_type',
       'pitch_type_seq', 'type_confidence', 'zone', 'spin_dir', 'spin_rate',
       'sv_id', 'event_num'],
      dtype='object')
"""
parkList = []
parkList = sorted(df.park_name.unique())
df.park_name.unique()
for p in parkList:
    print(p)
print(len(parkList))


dfpc = df[df["park_name"] == "Petco Park"]
print(dfpc['pit_last_name'].describe())

pitlist = []
pitlist = dfpc['pit_last_name'].value_counts()
print(pitlist)

dfdv = dfpc[['pit_last_name', 'start_speed', 'x', 'y']]
print(dfdv[dfdv['pit_last_name'] == 'Darvish'])
