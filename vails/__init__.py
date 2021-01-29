import argparse


def new():
    print('new called')


def generate():
    print('generate called')


def parse():
    # add help for vails command
    parser = argparse.ArgumentParser(
        prog='vails', description='This script is ...')
    subparsers = parser.add_subparsers(metavar='command')

    # add help for 'vails new' command
    parser_new = subparsers.add_parser(
        'new', help='See `new -h`.',  aliases=['n'])
    parser_new.add_argument(
        'project_name', type=str, help='project name what you want to create.')
    parser_new.set_defaults(handler=new)

    # add help for 'vails generate' command
    parser_generate = subparsers.add_parser(
        'generate', help='See `generate -h`.', aliases=['g'])
    parser_generate.add_argument(
        'file_name', type=str, help='File name what you want to create.')
    parser_generate.set_defaults(handler=generate)
    return parser.parse_args()


def main() -> None:
    args = parse()
    args.handler()
