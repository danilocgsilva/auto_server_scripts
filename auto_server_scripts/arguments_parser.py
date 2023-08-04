import argparse

def arguments_parser(args):
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        "-t",
        type=str,
        required=False,
        help="The type of script needed",
        nargs='?'
    )
    parser.add_argument(
        "--docker",
        "-d",
        required=False,
        action='store_true',
        help="Prefixes the output with a RUN, with is suitable to a Dockerfile receipt."
    )
    parser.add_argument(
        "--generate-file",
        "-f",
        required=False,
        action='store_true',
        help="Sinalizes that I want to generate a file."
    )
    parser.add_argument(
        "--server-name",
        "-s",
        required=False,
        help="Tells the name of the virtual host to be created for Apache."
    )
    parser.add_argument(
        "--to-directory",
        "-td",
        required=False,
        help="If the file generation is asked, put the file in the given folder."
    )
    parser.add_argument(
        "--dockerreceipt-inject",
        "-di",
        required=False,
        action='store_true',
        help="Alters a docker receipt (a folder with docker-compose.yml and Dockerfile) to build the environment with a Virtual Host"
    )
    parser.add_argument(
        "--dockerreceipt-address",
        "-da",
        required=False,
        help="When requiring to inject code in the docker content, it is required to provides this argument",
        nargs='?'
    )

    return parser.parse_args(args)
    