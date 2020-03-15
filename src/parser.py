import argparse
from datetime import datetime

from utils import valid_date


def transaction_parser(subparser, transaction_type):
    transaction_parser = subparser.add_parser(transaction_type)

    transaction_parser.add_argument("amount", type=int, help="Money amount")
    transaction_parser.add_argument(
        "tags", type=str, nargs="+", help="Tag your transactions"
    )
    transaction_parser.add_argument("--comment", type=str)
    transaction_parser.add_argument(
        "--date",
        type=valid_date,
        required=False,
        help="Date of transaction - format YYYY-MM-DD",
        default=datetime.date.today()
    )


def stats_parser(subparser):
    stats_parser = subparser.add_parser("stats")
    stats_parser.add_argument("date", type=valid_date)


def get_parser():
    parser = argparse.ArgumentParser(description="Money store argument parser")
    subparser = parser.add_subparsers(dest="action")

    transaction_parser(subparser, "+")
    transaction_parser(subparser, "-")
    stats_parser(subparser)

    return parser
