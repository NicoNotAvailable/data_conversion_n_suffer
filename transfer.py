import csv
import pandas as pd
import re

error_log = 'games_errors.log'


def convert_csv_separator(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)

        with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                writer.writerow(row)


def normalize(text):
    text = str(text).lower().strip()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def create_id(row):
    return f"{normalize(row['track_name'])}___{normalize(row['artist'])}"


def extent_spotify():
    clear_file("definitive_spotify.tsv")
    clear_file("definitive_spotify.csv")
    main_df = pd.read_csv("spotify_dataset.csv")
    streaming_df = pd.read_csv("spotify_final_dataset.csv")

    main_df.rename(columns={'song': 'track_name', 'Artist(s)': 'artist'}, inplace=True)
    streaming_df.rename(columns={'Song Name': 'track_name', 'Artist Name': 'artist'}, inplace=True)

    main_df['custom_id'] = range(1, len(main_df) + 1)

    streaming_df['merge_key'] = streaming_df['track_name'] + '___' + streaming_df['artist']
    main_df['merge_key'] = main_df['track_name'] + '___' + main_df['artist']

    columns_to_yoink = [
        'Days', 'Top 10 (xTimes)', 'Peak Position', 'Peak Position (xTimes)',
        'Position', 'Peak Streams', 'track_name', 'artist'
    ]
    streaming_features = streaming_df.drop(columns=[col for col in columns_to_yoink if col in streaming_df.columns])

    merged_df = pd.merge(main_df, streaming_features, on='merge_key', how='left')
    merged_df.drop(columns=['merge_key'], inplace=True)

    merged_df.to_csv("definitive_spotify.tsv", sep="\t", index=False)
    merged_df.to_csv("definitive_spotify.csv", sep="\t", index=False)
    print("✨ uwu your file is ready and full of ID magic ✨")


def extend_MY_COCK_WHAT_IS_THIS():
    clear_file("definitive_spotify.tsv")
    clear_file("definitive_spotify.csv")
    main_df = pd.read_csv("spotify_dataset.csv")
    streaming_df = pd.read_csv("spotify_final_dataset.csv")

    main_df.rename(columns={'song': 'track_name', 'Artist(s)': 'artist'}, inplace=True)
    streaming_df.rename(columns={'Song Name': 'track_name', 'Artist Name': 'artist'}, inplace=True)

    main_df['custom_id'] = range(1, len(main_df) + 1)

    streaming_df['merge_key'] = streaming_df['track_name'] + '___' + streaming_df['artist']
    main_df['merge_key'] = main_df['track_name'] + '___' + main_df['artist']

    columns_to_yoink = [
        'Days', 'Top 10 (xTimes)', 'Peak Position', 'Peak Position (xTimes)',
        'Position', 'Peak Streams', 'track_name', 'artist'
    ]
    streaming_features = streaming_df.drop(columns=[col for col in columns_to_yoink if col in streaming_df.columns])

    merged_df = pd.merge(main_df, streaming_features, on='merge_key', how='left')
    merged_df.drop(columns=['merge_key'], inplace=True)

    for col in merged_df.select_dtypes(include='object').columns:
        merged_df[col] = merged_df[col].astype(str).str.replace('"', '', regex=False)

    merged_df.to_csv("definitive_spotify.tsv", escapechar = '\\', sep="\t", index=False, quoting=3)
    merged_df.to_csv("definitive_spotify.csv", escapechar = '\\', sep="\t", index=False, quoting=3)

    print("✨ uwu your file is ready and full of ID magic ✨")


def clean_quotes(text):
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    return text.replace('""', '´').strip()


def ach_fick_doch_alles(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, quotechar='"', delimiter=',', skipinitialspace=True)
        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

        for row in reader:
            cleaned_row = [clean_quotes(field) for field in row]
            writer.writerow(cleaned_row)


def clear_file(input_file):
    f = open(input_file, "w+")
    f.close()


def so_du_huso_du_wirst_gefickt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = line.replace('""', '')
            outfile.write(cleaned_line)


def remove_dual_escape(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile, \
            open(error_log, 'w', encoding='utf-8') as errfile:

        reader = csv.reader(infile, quotechar='"', delimiter=',', skipinitialspace=True)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        line_num = 0
        good = 0
        bad = 0

        for line in infile:
            line_num += 1
            try:
                row = next(csv.reader([line], quotechar='"', delimiter=',', skipinitialspace=True))
                writer.writerow([field.strip() for field in row])
                good += 1
            except Exception as e:
                errfile.write(f"Fehler in Zeile {line_num}: {str(e)}\nInhalt: {line[:200]}...\n\n")
                bad += 1

        print(f"Fertig: {good} Zeilen gespeichert, {bad} fehlerhafte Zeilen ausgelassen.")


def convert_csv_tsv(input_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open('output.tsv', 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            writer.writerow(row)


def remove_dual_escape_alt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, quotechar='"', delimiter=',', skipinitialspace=True)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            # Optional: Strip leading/trailing whitespace from each field
            cleaned_row = [field.strip() for field in row]
            writer.writerow(cleaned_row)


# remove_dual_escape("games.csv", "out.csv")
# clear_file("out.csv")
# so_du_huso_du_wirst_gefickt("games.csv", "out.csv")
# ach_fick_doch_alles("games.csv", "out.csv")
# extent_spotify()
extend_MY_COCK_WHAT_IS_THIS()
