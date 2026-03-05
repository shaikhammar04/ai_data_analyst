def generate_basic_insights(df):

    insights = []

    rows, cols = df.shape
    insights.append(f"The dataset contains {rows} rows and {cols} columns.")

    # Missing values
    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]

    if len(missing_cols) > 0:
        for col, val in missing_cols.items():
            percent = (val / rows) * 100
            insights.append(f"Column '{col}' has {percent:.2f}% missing values.")
    else:
        insights.append("No missing values were detected.")

    # Numeric analysis
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if len(numeric_df.columns) > 0:

        variances = numeric_df.var().sort_values(ascending=False)
        highest_var_col = variances.index[0]

        insights.append(
            f"'{highest_var_col}' shows the highest variance among numeric features."
        )

    # Correlation
    if numeric_df.shape[1] > 1:

        corr = numeric_df.corr().abs()

        for col in corr.columns:
            corr.loc[col, col] = 0

        max_corr = corr.unstack().idxmax()
        value = corr.unstack().max()

        insights.append(
            f"Strongest correlation detected between '{max_corr[0]}' and '{max_corr[1]}' ({value:.2f})."
        )

    # Categorical insight
    categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in categorical_cols:
        unique_vals = df[col].nunique()

        insights.append(
            f"Column '{col}' contains {unique_vals} unique categories."
        )

    return insights