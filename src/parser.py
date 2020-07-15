import argparse
from datetime import datetime

from utils import valid_date


def transaction_parser(subparser, transaction_type):
    transaction_parser = subparser.add_parser(transaction_type)

    transaction_parser.add_argument("amount", type=int, help="Money amount (e.g. -500)")
    transaction_parser.add_argument(
        "tags", type=str, nargs="+", help="Transaction tags, separated by spaces (e.g. burger beer pub)"
    )
    transaction_parser.add_argument("--comment", type=str, help="Additional information about transaction")
    transaction_parser.add_argument(
        "--date",
        type=str,
        required=False,
        help="Transaction date in one of the formats: YYYY-MM-DD/YYYY-MM-DD@HH-mm/HH-mm (or just leave empty if transaction is happening now)",
        default=datetime.now().strftime("%s")
    )


def stats_parser(subparser):
    stats_parser = subparser.add_parser("stats")
    stats_parser.add_argument("date", type=valid_date)


def get_parser():
    parser = argparse.ArgumentParser(description="Money store argument parser")
    subparser = parser.add_subparsers(dest="action")

    transaction_parser(subparser, "tx")
    stats_parser(subparser)

    return parser
