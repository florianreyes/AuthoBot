import argparse


def cli() -> None:
    parser = argparse.ArgumentParser("AuthoBot Argument Parser")

    parser.add_argument(
        "--endpoints",
        "-e",
        required=True,
        help="A file containing the endpoints to be tested in the format: https://host:port/example/route one per line",
    )

    parser.add_argument(
        "--header1",
        "-h1",
        help="First authorization header (e.g 'Authorization: Bearer ...')",
    )
    parser.add_argument(
        "--header2",
        "-h2",
        help="Second authorization header (e.g 'Authorization: Bearer ...')",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="bypassed.txt",
        help="Output file",
    )
    parser.add_argument(
        "--endpoints",
        "-e",
        help="A file containing the endpoints to be tested in the format: https://host:port/example/route one per line",
    )

    ### python3 authobot --endpoints ends.txt --token1 <TOKEN1> --token2 <TOKEN2> --headparam <HEADER>
