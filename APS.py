import random


# parte do calculo
def exp_modular(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # Se exp é ímpar
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


# gerar chaves
def gerar_chaves(primo, base):
    chave_privada = random.randint(1, primo - 2)
    chave_publica = exp_modular(base, chave_privada, primo)
    return chave_publica, chave_privada


# criptografia
def criptografar(frase, primo, base, chave_publica_receptor):
    frase_criptografada = []
    for caractere in frase:
        mensagem = ord(caractere)  # converte para unicode
        k = random.randint(1, primo - 2)
        c1 = exp_modular(base, k, primo)
        s = exp_modular(chave_publica_receptor, k, primo)
        c2 = (mensagem * s) % primo
        frase_criptografada.append((c1, c2))
    return frase_criptografada


# descriptografia
def descriptografar(frase_criptografada, chave_privada_receptor, primo):
    frase_original = ""
    for c1, c2 in frase_criptografada:
        s = exp_modular(c1, chave_privada_receptor, primo)
        s_inv = pow(s, -1, primo)  # multiplicacao inversa
        mensagem = (c2 * s_inv) % primo
        frase_original += chr(mensagem)  # troca de caracteres
    return frase_original


# base do sistema, numero primo grande para ter todos os caracteres da ling port
primo = 65537
base = 3

# puxando chave gerada
chave_publica, chave_privada = gerar_chaves(primo, base)

# colocar frase
frase = input("Digite uma frase para criptografar: ")

# criptografia
frase_criptografada = criptografar(frase, primo, base, chave_publica)
print("Frase Criptografada:", frase_criptografada)

# descriptografia
frase_descriptografada = descriptografar(frase_criptografada, chave_privada, primo)
print("Frase Descriptografada:", frase_descriptografada)
