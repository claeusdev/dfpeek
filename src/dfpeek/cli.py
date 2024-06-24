from argparse import Action, Namespace, ArgumentParser


class FileAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values,
        option_string: str | None = None,
    ) -> None:
        # return super().__call__(parser, namespace, values, option_string)
        file, path = values
        namespace.filetype = file.lower()
        namespace.path = path


def create_parser():
    parser = ArgumentParser(description="Explore data from files")

    parser.add_argument(
        "-f",
        help="file type & path to file",
        nargs=2,
        metavar=("file_type", "file_path"),
        action=FileAction,
        required=True,
    )
    return parser


class DFPeek:
    def __init__(self, frame) -> None:
        self.frame = frame

    def summarize(self):
        shape = self.frame.shape
        cols = self.frame.columns.to_list()
        # datatypes
        d_types = self.frame.dtypes
        print(d_types)

        numerical_columns = d_types[d_types.isin(["int64", "float64"])].index.tolist()
        categorical_columns = d_types[
            d_types.isin(["object", "category"])
        ].index.tolist()

        print("Numerical Columns:", numerical_columns)
        print("Categorical Columns:", categorical_columns)

        # Calculate correlation matrix for numerical columns
        # correlation_matrix = self.frame.corr()
        # print("Correlation Matrix:")
        # print(correlation_matrix)

        print(shape, cols, self.null_cols())

    def null_cols(self):
        # Step 1: Use isnull() to create a DataFrame of boolean values
        null_data = self.frame.isnull()

        # Step 2: Use any() to find columns that contain any null values
        null_columns = null_data.any()

        # Step 3: Filter the columns
        columns_with_nulls = null_columns[null_columns].index.tolist()
        return columns_with_nulls


def main():
    import pandas as pd

    args = create_parser().parse_args()
    df = pd.read_csv(args.path)
    summary = DFPeek(df)
    print(summary.summarize())
