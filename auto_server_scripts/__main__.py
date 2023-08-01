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

def generate_file(fileName: str, fileContent: str):
    f = open(fileName, "w")
    f.write(content)
    f.close()

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
        action='store_true',
        help="Prefixes the output with a RUN, with is suitable to a Dockerfile receipt."
    )
    parse.add_argument(
        "--to_path",
        "-p",
        required=False,
        help="Outputs to a file in the designated path."
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
            
        content = instantiatedClass.exec()
        if args.to_path:
            generate_file(content)
        else:
            print(content)
        
    except ArgumentsNotValid as e:
        print(str(e))
    except ModuleNotFoundError as e:
        print("There are no type like " + args.type)
        scripts_files = list_scripts()
        print("The available modules are:")
        for module in list_scripts():
            print(" * " + module)
    
