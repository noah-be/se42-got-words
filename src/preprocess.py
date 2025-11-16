import re
from itertools import chain
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import stopwords




def tokenize(text: str):
    return re.findall(r"[A-Za-z']+", text.lower())


def add_token_column(df: pd.DataFrame, text_col: str = "text", tokens_col: str = "tokens") -> pd.DataFrame:
    df[tokens_col] = df[text_col].apply(tokenize)
    return df


def build_frequency(df: pd.DataFrame, tokens_col: str = "tokens"):
    all_tokens = list(chain.from_iterable(df[tokens_col]))
    freq = Counter(all_tokens)
    freq_df = (
        pd.DataFrame(freq.items(), columns=["word", "count"])
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )
    return freq_df, all_tokens




def load_stopwords():
    nltk.download("stopwords")
    return set(stopwords.words("english"))

def apply_stopwords(freq_df, stopwords_set):
    return (
        freq_df[~freq_df["word"].isin(stopwords_set)]
        .reset_index(drop=True)
    )
