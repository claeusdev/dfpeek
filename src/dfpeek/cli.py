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


def main():
    import pandas as pd

    args = create_parser().parse_args()
    df = pd.read_csv(args.path)
    print(df)
