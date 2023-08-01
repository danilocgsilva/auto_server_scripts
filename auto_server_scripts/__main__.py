import argparse
import importlib
import os
import auto_server_scripts.scripts.php_composer as php_composer
from auto_server_scripts.validate_args import validate_args
from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid

def list_scripts():
    path = os.path.dirname(php_composer.__file__)
    modules_raw = os.listdir(path)
    modules_cleaned = []
    for module in modules_raw:
        if not module == '__pycache__':
            modules_cleaned.append(module)

    return modules_cleaned

def commandLineToClassConversor(command_line: str):
    terms = command_line.split("_")
    uppercasedTerms = []
    for term in terms:
        uppercasedTerms.append(term.capitalize())
    
    finalClassName = ""
    for uppercasedTerm in uppercasedTerms:
        finalClassName += uppercasedTerm
    
    return finalClassName

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

    try:
        validate_args(args)
        module = importlib.import_module(
            "auto_server_scripts.scripts." + args.type
        )
        LoadedClass = getattr(module, commandLineToClassConversor(args.type))
        instantiatedClass = LoadedClass()
        
        if args.docker:
            instantiatedClass.setDocker(args.docker)
        
        print(
            instantiatedClass.exec()
        )
    except ArgumentsNotValid as e:
        print(str(e))
    except ModuleNotFoundError as e:
        print("There are no type like " + args.type)
        scripts_files = list_scripts()
        print("The available modules are:")
        for module in list_scripts():
            print(" * " + module)
    
