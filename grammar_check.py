import language_tool_python

import pandas as pd
import numpy as np
import string

def get_csv_column_as_array(csv_file_path, column_name, num_rows):
    df = pd.read_csv(csv_file_path)
    column_array = df[column_name].values[:num_rows]
    return column_array

def generate_scores_csv(csv_file_path, column_name, num_rows, save_csv_file_path):
    texts = get_csv_column_as_array(csv_file_path, column_name, num_rows)

    tool = language_tool_python.LanguageTool('en-US')

    # Initialize a list to store the average number of grammar errors per sentence for each text
    avg_errors_per_sentence = []

    for text in texts:
        # Split text into sentences
        sentences = tool.split_into_sentences(text)

        # Count grammar errors for each sentence
        total_errors = sum(len(tool.check(sentence)) for sentence in sentences)

        # Calculate average errors per sentence if there are sentences, otherwise 0
        avg_errors = total_errors / len(sentences) if sentences else 0
        avg_errors_per_sentence.append(avg_errors)

    # Create a DataFrame with the results
    result_df = pd.DataFrame({"Grammar mistakes per sentence": avg_errors_per_sentence})

    # Save the DataFrame to a new CSV file
    result_df.to_csv(save_csv_file_path, index=False)

data_path = "data/Starting_data.csv"
output_name = "grammar_mistakes"

parts = data_path.split("/")
new_data_path = parts[0] + "/" + output_name + parts[1]

generate_scores_csv(data_path, "text", 100, new_data_path)
