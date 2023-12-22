import pandas as pd
import string

# Calculates set(words) / len(words)

def get_csv_column_as_array(csv_file_path, column_name, num_rows):
    df = pd.read_csv(csv_file_path)
    column_array = df[column_name].values[:num_rows]
    return column_array

def calculate_vocab_richness(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    words = text.split()
    unique_words = set(words)
    return len(unique_words) / len(words)


def generate_scores_csv(csv_file_path, column_name, num_rows, save_csv_file_path):
    texts = get_csv_column_as_array(csv_file_path, column_name, num_rows)

    richness_scores = [calculate_vocab_richness(text) for text in texts]

    result_df = pd.DataFrame({"Percent Unique Words": richness_scores})
    result_df.to_csv(save_csv_file_path, index=False)

data_path = "data/Starting_data.csv"
output_name = "vovab_richness_scores"

parts = data_path.split("/")
new_data_path = parts[0] + "/" + output_name + parts[1]

generate_scores_csv(data_path, "text", 100, new_data_path)
