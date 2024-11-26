with open('teste1.txt') as f:

    mat = []

    for line in f:
        linha = (line.strip())
        tam = len(linha)
        vet = []
        i = 0
        while i < tam:
               
            if linha[i] != ' ' and linha[i] != ',':
                if 47 < ord(linha[i]) < 58:
                    if i+1 < tam and 47 < ord(linha[i+1]) < 58:
                        var = linha[i] + linha[i+1]
                        vet.append(var)
                        i += 1
                    else:
                        vet.append(linha[i])
                else:
                    vet.append(linha[i])
            i += 1
        
        mat.append(vet)

tam = len(mat)
i = 0

while i < tam:
    tam2 = len(mat[i])
    if tam2 == 1:
        a = mat[i+1]
        b = mat[i+2]
        tam_a = len(a)
        tam_b = len(b)
        if mat[i][0] == 'U':
            resp = a * 1
            for j in range(0,tam_b):
                uniao = 0
                for k in range(0,tam_a):
                    if b[j] == a[k]:
                        uniao = 1
                if uniao == 0:
                    resp.append(b[j])
            print("União: conjunto 1 {", ', '.join(a), "}, conjunto 2 {", ', '.join(b),"}. Resultado: {", ', '.join(resp),"}" )

        if mat[i][0] == 'I':
            resp = []
            for j in range(0,tam_b):
                inter = 0
                for k in range(0,tam_a):
                    if b[j] == a[k]:
                        inter = 1
                        resp.append(b[j])
            print("Interseção: conjunto 1 {", ', '.join(a), "}, conjunto 2 {", ', '.join(b),"}. Resultado: {", ', '.join(resp),"}" )


        if mat[i][0] == 'D':
            resp = []
            for k in range(0,tam_a):
                difer = 0
                for j in range(0,tam_b):
                    if a[k] == b[j]:
                        difer = 1
                if difer == 0:
                    resp.append(a[k])

            print("Diferença: conjunto 1 {", ', '.join(a), "}, conjunto 2 {", ', '.join(b),"}. Resultado: {", ', '.join(resp),"}" )
        
        if mat[i][0] == 'C':
            resp = []
            for k in range(0,tam_a):
                for j in range(0,tam_b):
                    cartesiano = "( " + a[k]
                    resp.append(cartesiano)
                    cartesiano = b[j] + " )"
                    resp.append(cartesiano)

            print("Produto Cartesiano: conjunto 1 {", ', '.join(a), "}, conjunto 2 {", ', '.join(b),"}. Resultado: {",', '.join(resp),"}" )


    i += 1
