def digital_root(n):

    if type(n) != str:

        if n < 0:
            return "O numero não pode ser negativo"

        while n > 9:
            n = sum(int(x) for x in str(n))
        return n
    else:
        return "Um numero deverá ser enviado"

print(digital_root(16))
