from collections import Counter

texto1 = """Neste artigo, você vai aprender algumas dicas para desenvolver e utilizar testes unitários e de integração no Front-end.
Se você já quebrou a cabeça tentando desenvolver um bom teste unitário ou de integração, boas vindas ao time! Planejar, 
projetar e executar testes automatizados faz parte do dia a dia dev e é muito importante para garantir a qualidade de qualquer aplicação. 
Então, para vocês testers de plantão, nossa prioridade a partir de agora é aprender essa arte. Fique confortável e aproveite a leitura!"""

texto2 = """1 - Uma boa maneira de fortalecer sua experiência profissional é criando um portfólio poderoso. E projetos derivados de cursos não têm tanto peso quanto projetos autorais. 
Aplique o que aprendeu nos cursos em projetos pessoais e os destaque em seu portfólio, além de colocar os repositórios "pinados" no Github;
2 - Ninguém aprende algo de verdade sem prática. Se você praticar todos os dias um pouquinho, verá mais resultado do que praticar um longo 
tempo em dias alternados, pois estará impulsionando sua vivência de aprendizado;
3 - O README dos repositórios do Github existe para que você possa mostrar ao mundo o que você criou. Faça um README bem 
escrito explicando do que se trata o projeto, que tecnologias utilizou, o que aprendeu de novo e quais dificuldades superou. Os recrutadores e equipes técnicas agradecem!"""

def analise_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)

    for caractere, proporcao in mais_comuns:
        print(f"{caractere} => {proporcao*100:.2f}%")

analise_frequencia_de_letras(texto1)