from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid

def validate_args(args) -> bool:
    if args.type == None:
        exceptionMessage = "You must use --type to tell what script you will need."
        raise ArgumentsNotValid(exceptionMessage)
    