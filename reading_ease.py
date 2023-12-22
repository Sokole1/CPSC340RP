import textstat

import pandas as pd

def get_csv_column_as_array(csv_file_path, column_name, num_rows):
    df = pd.read_csv(csv_file_path)
    column_array = df[column_name].values[:num_rows]
    return column_array

def generate_scores_csv(csv_file_path, column_name, num_rows, save_csv_file_path):
    # Get the text column from the CSV
    texts = get_csv_column_as_array(csv_file_path, column_name, num_rows)

    # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease
    reading_ease = [textstat.flesch_reading_ease(text) for text in texts]

    result_df = pd.DataFrame({"Reading Ease": reading_ease})

    # Save the DataFrame to a new CSV file
    result_df.to_csv(save_csv_file_path, index=False)

data_path = "data/GPT_rewrite.csv"
output_name = "reading_ease"

parts = data_path.split("/")
new_data_path = parts[0] + "/" + output_name + parts[1]

generate_scores_csv(data_path, "Modified Text", 30, new_data_path)