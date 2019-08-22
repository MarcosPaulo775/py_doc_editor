import os
from docx import Document

caminho = '/home/usuario/Área de Trabalho'  #Alterar aqui
arquivo = 'Certificado_Exemplo.docx'
docword = os.path.join(caminho, arquivo)

nomes = ['Pedro', 'Maria', 'Marcos']

for i in range(len(nomes)):
	nomes[i] = nomes[i].upper()

for novo_nome in nomes:
    doc = Document(docword)
    for paragrafo in doc.paragraphs:
        palavra = 'NOME'
        if palavra in paragrafo.text:
        	paragrafo.text = paragrafo.text.replace(palavra,novo_nome)

    new_docword = os.path.join(caminho, novo_nome+ '.docx')
    doc.save(new_docword)
