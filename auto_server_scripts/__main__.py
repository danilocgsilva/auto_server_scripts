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

def generate_file(fullFilePath: str, fileContent: str):
    f = open(fullFilePath, "w")
    f.write(fileContent)
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
        help="When requiring to inject code in the docker content, it is required to provides this argument"
        nargs='?'
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
        if args.server_name:
            instantiatedClass.setVhostName(args.server_name)

        content = instantiatedClass.exec()
        if args.generate_file:
            full_file_path = args.server_name + ".conf"
            if args.to_directory:
                full_file_path = os.path.join(args.to_directory, full_file_path)
            generate_file(full_file_path, content)
            print("The file " + full_file_path + " has been generated.")
        if args.dockerreceipt_inject:

        else:
            print(
                content
            )
        
    except ArgumentsNotValid as e:
        print(str(e))
    except ModuleNotFoundError as e:
        print("There are no type like " + args.type)
        scripts_files = list_scripts()
        print("The available modules are:")
        for module in list_scripts():
            print(" * " + module)
    
