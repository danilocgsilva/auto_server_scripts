import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        "-t",
        type=str,
        required=False,
        help="The type of script needed"
    )

