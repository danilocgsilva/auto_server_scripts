import importlib
import os
import auto_server_scripts.scripts.php_composer as php_composer
from auto_server_scripts.validate_args import validate_args
from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid
from auto_server_scripts.arguments_parser import arguments_parser
import sys

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
    
    args = arguments_parser(sys.argv[1:])

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
    
