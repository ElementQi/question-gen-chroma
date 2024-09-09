import pandas as pd
import json
from tqdm import tqdm

def unicode_transform(csv_filepath):
    df = pd.read_csv(csv_filepath)

    for i in tqdm(range(len(df))):
        try:
            references_str = df["references"][i]
            references_list = json.loads(references_str)

            df.at[i, "references"] = json.dumps(references_list, ensure_ascii=False)

        except Exception as e:
            print(f"Error processing row {i}: {e}")

    df.to_csv(csv_filepath, index=False)

    print(f"Purified already: {csv_filepath}")


if __name__ == "__main__":
    unicode_transform("saves/novel_query.csv")