import importlib
import os
import auto_server_scripts.scripts.php_composer as php_composer
from auto_server_scripts.validate_args import validate_args
from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid
from auto_server_scripts.arguments_parser import arguments_parser
from auto_server_scripts.FileOperations import FileOperations
import sys

def list_scripts():
    path = os.path.dirname(php_composer.__file__)
    modules_raw = os.listdir(path)
    modules_cleaned = []
    for module in modules_raw:
        if not module == '__pycache__':
            modules_cleaned.append(module)

    return modules_cleaned

# def generate_file(fullFilePath: str, fileContent: str):
#     f = open(fullFilePath, "w")
#     f.write(fileContent)
#     f.close()

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
    
    args = arguments_parser()

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

        virtualHostFileContent = instantiatedClass.exec()
        file_name = args.server_name + ".conf"
        fileOperations = FileOperations()
        if args.generate_file:
            full_file_path = ""
            if args.to_directory:
                full_file_path = os.path.join(args.to_directory, file_name)
            fileOperations.generate_file(full_file_path, virtualHostFileContent)
            print("The file " + full_file_path + " has been generated.")
        if args.dockerreceipt_inject:
            instantiatedClass.injectInDockerReceipt(args, fileOperations, file_name)
        else:
            print(virtualHostFileContent)
            if not args.no_hint:
                print("")
                print("hint: you can use the --dockerreceipt-inject as a parameter to automatically injects a new virtual host configuration file in an existing docker receipt.")
            
    except ArgumentsNotValid as e:
        print(str(e))
    except ModuleNotFoundError as e:
        print("There are no type like " + args.type)
        scripts_files = list_scripts()
        print("The available modules are:")
        for module in list_scripts():
            print(" * " + module)
    
