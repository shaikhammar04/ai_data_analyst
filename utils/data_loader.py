import pandas as pd


def load_csv(uploaded_file):
    """
    Load CSV file into a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        return df
    except Exception as e:
        raise ValueError(f"Error loading CSV: {e}")


def get_column_types(df):
    """
    Separate numeric and categorical columns.
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    return {
        "numeric": numeric_cols,
        "categorical": categorical_cols
    }