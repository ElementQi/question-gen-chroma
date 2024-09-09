
from chunking_evaluation import QwenSyntheticEvaluation
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--key", default='', type=str)
parser.add_argument("--corpora-path", default='corpora/pride_and_prejudice.txt', type=str)
parser.add_argument("--save-path", default='saves/generated_queries_and_excerpts.csv', type=str)
parser.add_argument("--query-num", default=5, type=int)
parser.add_argument("--round-num", default=1, type=int)
# if the model is in English, no need to set this flag
parser.add_argument("--non-en", default=False, type=bool)
args = parser.parse_args()


if __name__ == "__main__":
    OPENAI_API_KEY = args.key
    # this should be a list, but for simplicity, just use a single file
    corpora_paths = [args.corpora_path]
    queries_csv_path = args.save_path
    query_num = args.query_num
    round_num = args.round_num
    is_not_en = args.non_en

    evaluation = QwenSyntheticEvaluation(corpora_paths, queries_csv_path, openai_api_key=OPENAI_API_KEY)
    evaluation.generate_queries_and_excerpts(approximate_excerpts=True, num_rounds=round_num, queries_per_corpus=query_num)

    # change unicode to utf-8
    if is_not_en:
        from cn_purify import unicode_transform
        unicode_transform(queries_csv_path)