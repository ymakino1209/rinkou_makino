# rinkou01.py by makino
  
# import libraries
import os
import sys
import argparse
import pandas as pd
from pandas import DataFrame

# read file
def read_file(path):
    df = pd.read_table(path, encoding="utf_8", header=None, names=('city', 'address'))
    return df

# タブをスペースに置換したファイルを出力する
# export file as space-limited file
def exprot_file_space(DataFrame):
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_space.txt"
    return DataFrame.to_csv(path_or_buf = file_name_new,
                            sep=" ", columns=None, header=None, index=None, encoding="utf_8")

# 自然数Nをコマンドライン引数にとり、入力のうち先頭のN行を出力する
# export the initial "n" lines
def exprot_file_initial_n(DataFrame, num_lines):
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_initial" + str(num_lines) + ".txt"
    df_initial_n = DataFrame[:num_lines]
    return df_initial_n.to_csv(path_or_buf = file_name_new, 
                               sep="\t", columns=None, header=None, index=None, encoding="utf_8")

# 自然数Nをコマンドライン引数にとり、入力のうち末尾のN行を出力する
# exprot the last "n" lines
def exprot_file_last_n(DataFrame, num_lines):
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_last" + str(num_lines) + ".txt"  
    df_last_n = df[-num_lines:]
    return df_last_n.to_csv(path_or_buf = file_name_new, 
                            sep="\t", columns=None, header=None, index=None, encoding="utf_8")

# １列目の文字列を集計して標準出力に表示する(文字列/カウント数を表示）
#  Count the first column & display string/counts
def count_city(DataFrame):
    Series_count_city = DataFrame["city"].value_counts()
    Series_count_city.rename(columns={'city':'出現回数'})
    # pd.set_option('display.max_rows', None)
    return print(Series_count_city)

# define main function (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines 1", type=int)
    
    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    
    # read file
    df = read_file(filename)

    # display the number of lines
    print('The number of lines is %d' % len(df))

    # export file as space-limited file
    exprot_file_space(df)
    
    # export the initial "n" lines
    exprot_file_initial_n(df, nlines)

    # exprot the last "n" lines
    exprot_file_last_n(df, nlines)

    #  Count the first column & display string/counts
    count_city(df)
