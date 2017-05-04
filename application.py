import argparse
from passwordgenerators import PasswordGenerator

parser = argparse.ArgumentParser(description='Generate random password')
parser.add_argument('--words', type=int, default=4, choices=range(1,7), help='Number of words in password')
parser.add_argument('--separator', type=str, default='/', help='Type of words separator')
parser.add_argument('--prefix', type=str, help='First letter of words. Number of words is ignore.')
parser.add_argument('--chain', action='store_true', help='Chain of words')
args = parser.parse_args()

if args.chain:
    generator = PasswordGenerator('./en_words.txt')
    print(generator.generate_end_begin_password(args.words, args.separator))
elif args.prefix:
    generator = PasswordGenerator('./en_words.txt')
    print(generator.generate_shortcut_password(args.prefix, args.separator))
else:
    generator = PasswordGenerator('./en_words.txt')
    print(generator.generate_simple_password(args.words,args.separator))