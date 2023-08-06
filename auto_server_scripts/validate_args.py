from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid

def validate_args(args) -> bool:
    if args.type == None:
        exceptionMessage = "You must use --type to tell what script you will need."
        raise ArgumentsNotValid(exceptionMessage)
    if args.type == "apache_new_vhost":
        if not args.server_name:
            exceptionMessage = "You have provided the apache_new_vhost type. Thus, needs the --server-name as well..."
            raise ArgumentsNotValid(exceptionMessage)
        if args.dockerreceipt_inject:
            if not args.dockerreceipt_address:
                exceptionMessage = "You have provided the dockerreceipt_inject parameter. In this case, the --dockerreceipt-address is required as well, and must have as a value the address from your docker recept.\n"
                exceptionMessage += "You also may want to use the --documentroot-suffix parameter to custom the virtualhost prefix."
                raise ArgumentsNotValid(exceptionMessage)
    return True
    