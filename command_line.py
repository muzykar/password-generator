import argparse
from passwordgenerators import PasswordGenerator
from configuration import PasswordGeneratorConfiguration

parser = argparse.ArgumentParser(description='Generate random password')
parser.add_argument('--words', type=int, help='Number of words in password. Range of words: 2-19.')
parser.add_argument('--separator', type=str, default='/', help='Type of words separator.')
parser.add_argument('--prefix', type=str, help='First letter of words. Number of words is ignore.')
parser.add_argument('--chain', action='store_true', help='Chain of words.')
parser.add_argument('--length', type=int, help='Length of password. Range of password length: 12-127.')
parser.add_argument('--sentence', action='store_true', help='Adjective + noun + verb. Number of words is ignore.')
parser.add_argument('--language', type=str, choices=['en'], default='en', help='Select language.')
args = parser.parse_args()

config = PasswordGeneratorConfiguration(args.words, args.separator, args.prefix, args.chain, args.length, args.sentence,
                                        args.language)
generator = PasswordGenerator(config)
print(generator.generate_password())
