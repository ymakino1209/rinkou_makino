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

# export dataframe
def export_file(dataframe, file_name, delimited, encode):
    return dataframe.to_csv(path_or_buf = file_name,
                     columns=None, header=None, index=None, sep=delimited, encoding=encode)

# export line M to N
def extract_line_m_to_n(dataframe, num_lines1, num_lines2):
    df_m_to_n = dataframe[num_lines1 - 1:num_lines2]
    return df_m_to_n

# delete redundant lines
def delete_redundant_line(dataframe, col_name):
    Series_col = dataframe[col_name]
    Series_col_drop_dup = Series_col.drop_duplicates()
    df_col_drop_dup = pd.DataFrame(Series_col_drop_dup)
    return df_col_drop_dup

# calculate the frequency of a column
def cal_col_freq(dataframe, col_name):
    Series_col_freq = dataframe[col_name].value_counts() / len(dataframe)
    Series_col_freq.sort_values(ascending = False)
    df_col_freq = pd.DataFrame(Series_col_freq)
    df_col_freq.rename(columns={col_name:'frequency'})
    return df_col_freq

# define main function (to increase readability)
if __name__ == "__main__":
    information='''Type (1-3) of analysis: \n
            type1: export line M to N; \n
            type2: export 1st column (delete redundant lines, certain order); \n
            type3: calculate and display the frequency of 2nd column; \n'''

    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("mode", help=information, type=str)
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--initial_number", help="slice lines from initial number to end number", type=int)
    parser.add_argument("--end_number", help="number of lines 2", type=int)
    args = parser.parse_args()

    mode = args.mode
    filename = args.file
    nlines_initial = args.initial_number
    nlines_end = args.end_number

    # parameter
    col_names = ("city", "address")
    encode_name = "utf_8"
    
    # read file
    df = read_file(filename, col_names, encode_name)

    if mode == "type1":
        #自然数M, Nをコマンドライン引数にとり、入力のうちM行目からN行目を出力する
        # export line M to N
        file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + str(nlines_initial) + "_to_" + str(nlines_end) + ".txt"
        df_m_to_n = extract_line_m_to_n(df, nlines_initial, nlines_end)
        export_file(df_m_to_n, file_name_new, "\t", encode_name)

    elif mode == "type2":
        # １列目だけファイルに出力する（重複行は除去する、順番は任意）
        # export 1st column (delete redundant lines, certain order)
        col_num = 1
        file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + col_names[col_num - 1] + "_level.txt"
        df_col = delete_redundant_line(df, col_names[col_num - 1])
        export_file(df_col, file_name_new, "\t", encode_name)

    elif mode == "type3":
        # 各行の２列目の文字列の出現頻度を求め、出現頻度の高い順にソートして標準出力に表示する
        # calculate and display the frequency of 2nd column
        col_num = 2
        file_name_new = os.path.splitext(os.path.basename(filename))[0] + "_" + col_names[col_num - 1] + "_freq.txt"
        df_col = cal_col_freq(df, col_names[col_num - 1])
        #pd.set_option('display.max_rows', None)
        pd.set_option('show_dimensions', False)
        print(df_col)

    else:
        print(information)
