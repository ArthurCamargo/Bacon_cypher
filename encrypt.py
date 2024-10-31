# Bacon's cypher is an stenography method that utilizes 2 typefaces or different
# types of fonts

# TODO: check if file exists else exit 1

import argparse

parser = argparse.ArgumentParser("encrypt")
_ = parser.add_argument('-a', "--alphabet", help="Input file containing the alphabet that\
    will be utilized in the encryption", type=str, required=True)
_ = parser.add_argument('-t', "--text", help="Input file containing the plaintext that\
    will be encrypted", type=str, required=True)
_ = parser.add_argument('-m', "--message", help="Message that will be sent inside the\
                        plaintext", required=True)
_ = parser.add_argument('-o', "--output", help="Output file that will print the\
    encrypted text", type=str, required=True)
_ = parser.add_argument('-b', "--bin", action='store_true', help="Tells wheter to output the message the\
    binary value being encoded")

args = parser.parse_args()


alphabet = {}

for line in open(args.alphabet):
    line = line.strip()
    tokens = line.split(sep=' ')
    alphabet[tokens[0]] = tokens[1]

text = ''

for line in open(args.text):
    line = line.strip()
    text += line

msg = ''

for line in open(args.message):
    line = line.strip()
    msg += line

def encrypt(msg, alphabet, text):
    bin = ''
    encoded = ''
    msg = msg.upper()
    for letter in msg:
        if letter in alphabet.keys():
            bin += alphabet[letter]

    for i, letter in enumerate(text):
        new_letter = ''
        if (i < len(bin)):
            if bin[i] != '0' and letter != ' ':
                new_letter += '\033[3m'
                new_letter += letter
                new_letter += '\033[0m'
            else:
                new_letter = letter
        else:
            new_letter = letter

        encoded += new_letter


    return bin, encoded

bin, encoded = encrypt(msg, alphabet, text)

if(args.bin):
    file = open(args.output, 'w')
    file.write(bin + '\n')
    file.close()

file = open(args.output, 'w')
file.write( encoded + '\n')
file.close()



print(text)
print(alphabet)
print(args)