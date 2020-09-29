# rinkou01_advanced.py by makino

# import libraries
import os
import sys
import argparse
import pandas as pd
from pandas import DataFrame

# read file
def read_file(path, col_names, encode):
    df = pd.read_table(path, header=None, names=col_names, encoding=encode)
    return df

# export file
def export_file(DataFrame, file_name, delimited, encode):
    return DataFrame.to_csv(path_or_buf = file_name, 
                     columns=None, header=None, index=None, sep=delimited, encoding=encode)

#自然数M, Nをコマンドライン引数にとり、入力のうちM行目からN行目を出力する
# export line M to N
def extract_line_m_to_n(DataFrame, num_lines1, num_lines2):
    df_m_to_n = DataFrame[num_lines1 - 1:num_lines2]
    return df_m_to_n

# １列目だけファイルに出力する（重複行は除去する、順番は任意）
# delete redundant lines
def delete_redundant_line(DataFrame, col_name):
    Series_col = DataFrame[col_name]
    Series_col_drop_dup = Series_col.drop_duplicates()
    return Series_col_drop_dup

# 各行の２列目の文字列の出現頻度を求め、出現頻度の高い順にソートして標準出力に表示する
# calculate the frequency of a column
def cal_col_freq(DataFrame, col_name):
    Series_col_freq = DataFrame[col_name].value_counts() / len(DataFrame)
    Series_col_freq.rename(columns={col_name:'出現頻度'})
    Series_col_freq.sort_values(ascending = False)
    return Series_col_freq 

# define main function (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number1", help="number of lines 1", type=int)
    parser.add_argument("number2", help="number of lines 2", type=int)
        
    args = parser.parse_args()

    filename = args.file
    nlines1 = args.number1
    nlines2 = args.number2

    # parameter
    col_names = ("city", "address")
    encode_name = "utf_8"

    # read file
    df = read_file(filename, col_names, encode_name)

    # export line M to N
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + str(nlines1) + "_to_" + str(nlines2) + ".txt"
    df_m_to_n = extract_line_m_to_n(df, nlines1, nlines2)
    export_file(df_m_to_n, file_name_new, "\t", encode_name)

    # export 1st column (delete redundant lines; certain oeder)
    col_num = 1
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + col_names[col_num - 1] + "_level.txt"
    Series_col = delete_redundant_line(df, col_names[col_num - 1])
    export_file(Series_col, file_name_new, "\t", encode_name)

    # calculate and display the frequency of 2nd column (address)
    col_num = 2
    file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + col_names[col_num - 1] + "_freq.txt"
    Series_col = cal_col_freq(df, col_names[col_num - 1])
    #pd.set_option('display.max_rows', None)
    print(Series_col)
