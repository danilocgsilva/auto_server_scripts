import argparse
import importlib
import os
import auto_server_scripts.scripts.php_composer as php_composer

def list_scripts():
    path = os.path.dirname(php_composer.__file__)
    modules_raw = os.listdir(path)
    modules_cleaned = []
    for module in modules_raw:
        if not module == '__pycache__':
            modules_cleaned.append(module)

    return modules_cleaned

def main():
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
        action='store_true'
    )

    args = parser.parse_args()

    if args.type == None:
        print("You must use --type to tell what script you will need.")
    else:
        try:
            module = importlib.import_module(
                "auto_server_scripts.scripts." + args.type
            )

            message = module.exec(args.docker)
            print(message)
        except ModuleNotFoundError as e:
            print("There are no type like " + args.type)
            scripts_files = list_scripts()
            print("The available modules are:")
            for module in list_scripts():
                print(" * " + module)
    
