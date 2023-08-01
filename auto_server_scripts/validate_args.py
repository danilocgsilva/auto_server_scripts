from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid

def validate_args(args) -> bool:
    if args.type == None:
        exceptionMessage = "You must use --type to tell what script you will need."
        raise ArgumentsNotValid(exceptionMessage)
    if args.type == "apache_new_vhost":
        if not args.server_name:
            exceptionMessage = "You have provided the apache_new_vhost type. Thus, needs the --server-name as well..."
            raise ArgumentsNotValid(exceptionMessage)
    