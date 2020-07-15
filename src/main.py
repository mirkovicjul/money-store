import parser
import service
# import database

services = {"tx": service.transact, "stats": service.stats}


def main():
    p = parser.get_parser()
    args = vars(p.parse_args())
    print(args)
    services[args["action"]](args)


if __name__ == "__main__":
    # database.drop_tables()
    # database.create_tables()
    main()
