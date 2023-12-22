import evaluate
import pandas as pd

# Code from: https://huggingface.co/spaces/evaluate-metric/perplexity
def get_csv_column_as_array(csv_file_path, column_name, num_rows):
    df = pd.read_csv(csv_file_path)
    column_array = df[column_name].values[:num_rows]
    return column_array

def generate_scores_csv(csv_file_path, column_name, num_rows, save_csv_file_path):
    # Get the text column from the CSV
    texts = get_csv_column_as_array(csv_file_path, column_name, num_rows)

    perplexity = evaluate.load("perplexity", module_type="metric")
    results = perplexity.compute(model_id='gpt2',
                                add_start_token=False,
                                predictions=texts)

    perplexity = results["perplexities"]

    result_df = pd.DataFrame({"Perplexity": perplexity})

    # Save the DataFrame to a new CSV file
    result_df.to_csv(save_csv_file_path, index=False)

data_path = "data/Starting_data.csv"
output_name = "perplexity"

parts = data_path.split("/")
new_data_path = parts[0] + "/" + output_name + parts[1]

generate_scores_csv(data_path, "text", 100, new_data_path)