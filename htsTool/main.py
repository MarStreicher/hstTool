from src.EstimateGenomeCoverage import getReadLength, countReadAmount
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Tool for the hts module.")

    actionChoices = {
        'get-GenomeCoverage': 'Get the estimates genome coverage from a specific file.'
    }

    parser.add_argument('action', choices=actionChoices.keys(), help=''.join(actionChoices[key] for key in actionChoices))
    parser.add_argument('fqgz', nargs='?', help='File path for a *.fq.gz file.')

    args = parser.parse_args()

    if args.action in actionChoices:
        print("Action:", args.action)
        print("Description:", actionChoices[args.action])

        if args.action == 'get-GenomeCoverage' and args.fqgz:
            readLength, readAmount = getReadLength(args.fqgz)

            print(f"Read length: {readLength}")
            print(f"Amount of reads: {readAmount}")
            
        elif args.action == 'other-action':
            print("in progress")
    else:
        parser.print_help()



if __name__ == '__main__':
    main()
