# encoding=utf8

#****************** ОПРЕДИЛЕНИЕ ФУНКЦИЙ ШИФРОВАНИЯ-РАСШИФРОВАНИЯ ****************

# функция шифрования  цезаря

cezar_encode=lambda message,shift,alphabet: (message.lower().translate(str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift]) ))

cezar_decode=lambda message,shift,alphabet: (message.lower().translate(str.maketrans(alphabet[shift:] + alphabet[:shift],alphabet) ))
#****************** ОПРЕДИЛЕНИЕ АЛФАВИТОВ ****************
ab="абвгдежзийклмнопрстуфхцчшщъыьэюя" # алфавит
abp=len(ab)# мощьность алвавита

# функция шифрования метод подмены
exchange_encode=lambda message,new_alphabet,alphabet:(message.lower().translate(str.maketrans(alphabet,new_alphabet)))

exchange_decode=lambda message,new_alphabet,alphabet:(message.lower().translate(str.maketrans(new_alphabet,alphabet)))