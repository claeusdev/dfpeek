import pandas as pd


class DFPeek:
    def __init__(self, file_path) -> None:
        self.frame = pd.read_csv(file_path)
        self.d_types = self.frame.dtypes

    @property
    def shape(self):
        return self.frame.shape

    @property
    def column_names(self):
        return self.frame.columns.to_list()

    def numerical_columns(self):
        return self.d_types[self.d_types.isin(["int64", "float64"])].index.tolist()

    def categorical_columns(self):
        return self.d_types[self.d_types.isin(["object", "category"])].index.tolist()

    def summarize(self):
        rows, columns = self.shape
        print("No. of rows:", rows)
        print("No. of columns:", columns)
        print("Columns:", self.column_names)
        print("Numerical Columns:", self.numerical_columns())
        print("Categorical Columns:", self.categorical_columns())
        print("Null Values?:", self.null_cols())
        print("========= TOP 10 rows =======")
        print(self.frame)
        print("========= BOTTOM 10 rows =======")

    def null_cols(self):
        # Step 1: Use isnull() to create a DataFrame of boolean values
        null_data = self.frame.isnull()
        # Step 2: Use any() to find columns that contain any null values
        null_columns = null_data.any()

        # Step 3: Filter the columns
        columns_with_nulls = null_columns[null_columns].index.tolist()
        return columns_with_nulls
