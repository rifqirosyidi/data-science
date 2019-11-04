import numpy as np
import pandas as pd
import xlwt


def msg(str_value):
    print("\n[", str_value, "]")

# data_frame = pd.DataFrame(
#     [['Jan', 58, 42, 74, 22, 2.95],
#      ['Feb', 61, 45, 78, 26, 3.02],
#      ['Mar', 65, 48, 84, 25, 2.34],
#      ['Apr', 67, 50, 92, 28, 1.02],
#      ['May', 71, 53, 98, 35, 0.48],
#      ['Jun', 75, 56, 107, 41, 0.11],
#      ['Jul', 77, 58, 105, 44, 0.0],
#      ['Aug', 77, 59, 102, 43, 0.03],
#      ['Sep', 77, 57, 103, 40, 0.17],
#      ['Oct', 73, 54, 96, 34, 0.81],
#      ['Nov', 64, 48, 84, 30, 1.7],
#      ['Dec', 58, 42, 73, 21, 2.56]],
#     index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#     columns=['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation'])
# print(data_frame)


# Importing The Data frame With txt or csv files rather than Hardcode it
file_name = "raw_data.txt"
data_frame = pd.read_csv(file_name)
print(data_frame)


# Print The First 5 Or The Last 3
msg("First Five Data, data_frame.head()")
print(data_frame.head())
msg("Last Three Data, data_frame.tail(3)")
print(data_frame.tail(3))


# *** Get The Data Type, Index, Column and Value
msg("Get Data Type")
print(data_frame.dtypes)

msg("Get Index")
print(data_frame.index)

msg("Get Column")
print(data_frame.columns)

msg("Get Value")
print(data_frame.values)

# *** Statistical Summary
msg("Statistical Summary - Data Describe")
print(data_frame.describe())


# *** Sorting The Data
msg("Sorted By Record High")
print(data_frame.sort_values('record_high', ascending=False))


# *** Slicing the Record
msg("Slicing Data")
print(data_frame.avg_low)  # Or print(data_frame['avg_low'])
print(data_frame[2:4])  # Print the Data 2 - 3

# Slice The Features
msg("data_frame[[ val1, val2 ]]")
print(data_frame[['record_high', 'record_low']])

# Slice using loc
msg("data_frame.loc[:,[val1, val2]]")
print(data_frame.loc[2, ['avg_high', 'avg_low']])  # Get Row index of a column

print(data_frame.loc[:, ['avg_high']]) # It will return all the data col

# Slicing using index locator
msg("Iloc Slicing")
print(data_frame.iloc[2:5, [2, 3]])


# *** Filtering The Data
print("Filtering")
print(data_frame[data_frame.avg_low > 50.0])

msg("Filter by Jun, Jul and Aug")
print(data_frame[data_frame.month.isin(['Jun', 'Jul', 'Aug'])])


# *** Assignment (Similar to slicing)
msg("Change The Average Precipitation of month Jun")
msg("Before")
print(data_frame[data_frame.month.isin(['Jun'])])

# Reassign
data_frame.loc[5, ['avg_precipitation']] = 2.0
msg("After")
print(data_frame[data_frame.month.isin(['Jun'])])


# Handlink Blank Value to Nan
msg("Assign Not a Number")
data_frame.loc[5, ['avg_precipitation']] = np.nan
print(data_frame[data_frame.month.isin(['Jun'])])


# *** Creating New Fields
msg("Creating New Fields")
data_frame['daily_update'] = (data_frame['avg_high'] + data_frame['avg_low']) / 2
print(data_frame)


# *** Renaming Fields
msg("Rename")
data_frame.rename(columns={'avg_precipitation' : 'avg_rain'}, inplace=True)  # Inplace using to reassign the var
# data = data_frame.rename -------> Without inplace
print(data_frame)

# Renaming All Field
msg("Renaming All Column")
data_frame.columns = ['month', 'av_hi', 'av_lo', 'rec_hi', 'rec_lo', 'av_rain', 'av_day']
print(data_frame)


# Iterate Data Frame
msg("Iterating The Data Frames")
for index, row in data_frame.iterrows():
    print(index, row['month'], row['av_day'])


# Write To Some File
data_frame.to_csv('data_frames.csv')
data_frame.to_excel('data_frames.xls', index=None, header=True)


