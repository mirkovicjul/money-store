import parser


def main():
    p = parser.get_parser()
    args = vars(p.parse_args())

    print(args)


if __name__ == "__main__":
    main()
