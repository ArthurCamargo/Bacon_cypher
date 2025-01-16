Implementação da [cifra de bacon](https://pt.wikipedia.org/wiki/C%C3%B3digo_Bacon)

Essa implementação estaganográfica retorna o texto utilizando um alfabeto binário representando os caracteres e os esconde em um texto

usage:
```bash
# Encryption
python3 encrypt.py -a <alphabet file> -t <to be encoded text file> -m <message file> -o <output file>
```


```bash
# Decryption
python3 decrypt.py -a <alphabet file> -t <encoded text file> -o <output file>
```
