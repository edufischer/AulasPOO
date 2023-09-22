import csv

# Lista de nomes de jogadores fictícios
nomes_jogadores = [
    "Neymar Jr.", "Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Luka Modrić",
    "Sergio Ramos", "Robert Lewandowski", "Kevin De Bruyne", "Harry Kane", "Virgil van Dijk",
    "Mohamed Salah", "Antoine Griezmann", "Eden Hazard", "Paul Pogba", "Sadio Mané",
    "Raheem Sterling", "Toni Kroos", "Alisson Becker", "Karim Benzema", "Thiago Silva",
    "Ronaldo Oliveira", "Luisa Fernandes", "Marcelo Santos", "Ana Silva", "Giovanni Barbosa",
    "Luana Pereira", "Gabriel Souza", "Sophia Rodrigues", "Lucas Almeida", "Eduarda Costa",
    "Mateus Silva", "Larissa Mendes", "Diego Lima", "Isabel Oliveira", "Pedro Ribeiro",
    "Clara Fernandes", "Enzo Pereira", "Manuela Alves", "Daniel Rodrigues", "Luiza Gonçalves",
    "Matheus Sousa", "Beatriz Ferreira", "João Santos", "Julia Barbosa", "Guilherme Almeida",
    "Laura Fernandes", "Felipe Costa", "Mariana Oliveira", "Rafael Pereira", "Bruna Souza",
    "Thiago Ribeiro", "Leticia Lima", "Arthur Barbosa", "Camila Fernandes", "Vinicius Almeida",
    "Sophie Costa", "Henrique Silva", "Ana Clara Mendes", "Lucas Oliveira", "Isabella Rodrigues",
    "Leonardo Mendes", "Carolina Ribeiro", "Gustavo Alves", "Clara Costa", "Lucas Rodrigues",
    "Nicole Souza", "Matheus Almeida", "Valentina Pereira", "Murilo Fernandes", "Sophia Lima",
    "Pedro Santos", "Lara Barbosa", "Samuel Oliveira", "Yasmin Silva", "Heitor Ribeiro",
    "Clara Lima", "Enzo Costa", "Ana Beatriz Fernandes", "Lucas Lima", "Maria Eduarda Almeida",
    "Cauã Barbosa", "Isadora Santos", "Rafael Souza", "Maria Clara Rodrigues", "Gael Oliveira",
    "Luiza Lima", "Lucas Fernandes", "Lavinia Pereira", "Vicente Alves", "Clara Mendes",
    "Davi Rodrigues", "Leticia Almeida", "Benjamin Costa", "Ana Luiza Ribeiro", "Joaquim Barbosa",
    "Lorena Lima", "Enzo Pereira", "Eloá Souza", "Caio Almeida", "Helena Ribeiro",
    "Lorenzo Fernandes", "Melissa Costa", "Antonio Oliveira", "Ana Clara Mendes", "Augusto Rodrigues",
    "Alice Lima", "Leonardo Alves", "Marina Costa", "Bernardo Pereira", "Esther Fernandes",
    "Francisco Ribeiro", "Larissa Barbosa", "Benjamin Lima", "Clara Almeida", "Eduardo Souza",
    "Antonella Silva", "Henrique Barbosa", "Maria Luiza Oliveira", "Daniel Ribeiro", "Leticia Costa",   
    "Luis Suárez", "Sergio Agüero", "Robert Firmino", "Edinson Cavani", "Marco Reus",
    "Gianluigi Buffon", "Ederson Moraes", "Joshua Kimmich", "Thomas Müller", "Angel Di María",
    "Jadon Sancho", "Frenkie de Jong", "Hakim Ziyech", "Timo Werner", "Lorenzo Insigne",
    "Giovanni Reyna", "Kai Havertz", "Federico Chiesa", "Jules Koundé", "Lucas Hernández",
    "Kieran Trippier", "Dayot Upamecano", "Achraf Hakimi", "Wilfred Ndidi", "Declan Rice",
    "Trent Alexander-Arnold", "Riyad Mahrez", "Bruno Fernandes", "Erling Haaland", "Marcus Rashford",
    "N'Golo Kanté", "Mason Mount", "Lautaro Martínez", "Rodri Hernández", "Nicolo Barella"
]

# Lista de descrições fictícias para as figurinhas
descricoes = [
    "Meio-campista talentoso com visão de jogo excepcional.",
    "Atacante habilidoso com dribles desconcertantes.",
    "Zagueiro sólido que lidera a defesa com maestria.",
    "Goleiro com reflexos rápidos e ótimo posicionamento.",
    "Meio-campista defensivo que protege bem a área.",
    "Atacante rápido e finalizador letal.",
    "Defensor versátil que pode atuar em várias posições.",
    "Meio-campista criativo que dita o ritmo do jogo.",
    "Atacante oportunista que marca gols importantes.",
    "Goleiro seguro e confiável.",
    "Zagueiro com excelente capacidade de marcação.",
    "Meio-campista com passes precisos e lançamentos longos.",
    "Atacante veloz que cria chances de gol.",
    "Defensor experiente com grande presença de campo.",
    "Meio-campista com habilidades de dribble.",
    "Atacante com faro de gol incrível.",
    "Goleiro com grandes defesas de pênalti.",
    "Defensor que bloqueia muitos chutes ao gol.",
    "Meio-campista versátil que contribui defensivamente.",
    "Atacante com chute potente de fora da área.",
    "Meio-campista que domina o meio do campo.",
    "Atacante jovem e promissor com grande futuro.",
    "Zagueiro que ganha a maioria das bolas aéreas.",
    "Meio-campista habilidoso com dribles curtos.",
    "Atacante com grande presença na área.",
    "Goleiro com ótima capacidade de reposição de bola.",
    "Defensor físico que recupera muitas bolas.",
    "Meio-campista com chutes de longa distância.",
    "Atacante com capacidade de marcar de cabeça.",
    "Meio-campista que dita o ritmo do jogo.",
    "Atacante com grande velocidade e agilidade.",
    "Defensor que impõe respeito na zaga.",
    "Meio-campista com excelente visão de jogo.",
    "Atacante que cria oportunidades para a equipe.",
    "Zagueiro que antecipa jogadas com precisão.",
    "Goleiro que realiza defesas espetaculares.",
    "Meio-campista que distribui passes com maestria.",
    "Atacante com faro de gol em jogadas aéreas.",
    "Defensor que bloqueia chutes perigosos.",
    "Meio-campista versátil que se adapta a diferentes funções.",
    "Atacante com grande técnica individual.",
    "Meio-campista com grande habilidade de drible.",
    "Goleiro que mantém a calma em situações de pressão.",
    "Defensor que impede avanços adversários com eficiência.",
    "Meio-campista que lidera o time com inteligência.",
    "Atacante com presença constante na área.",
    "Zagueiro que corta cruzamentos com precisão.",
    "Goleiro com grande agilidade e reflexos.",
    "Meio-campista com passes decisivos.",
    "Atacante que finaliza com precisão.",
    "Defensor que protege bem a área.",
    "Meio-campista com grande energia e resistência.",
    "Atacante com velocidade incrível.",
    "Goleiro que defende pênaltis com maestria.",
    "Defensor que desarma oponentes com facilidade.",
    "Meio-campista com visão periférica do jogo.",
    "Atacante que faz gols em jogadas individuais.",
    "Zagueiro que é um líder na defesa.",
    "Goleiro que inspira confiança à equipe.",
    "Meio-campista que lê o jogo com precisão.",
    "Atacante com instinto de artilheiro.",
    "Defensor que marca com firmeza.",
    "Meio-campista que distribui assistências incríveis.",
    "Atacante que cria oportunidades do nada.",
    "Zagueiro que bloqueia cruzamentos com determinação.",
    "Goleiro que se destaca em defesas de um contra um.",
    "Meio-campista com habilidades de cobrança de falta.",
    "Atacante que finaliza com frieza nas situações de um contra um.",
    "Defensor que impede avanços adversários com segurança.",
    "Meio-campista com inteligência tática excepcional.",
    "Atacante com movimentação impressionante.",
    "Goleiro com grande confiança na área.",
    "Defensor que não dá espaço aos atacantes.",
    "Meio-campista que controla o ritmo do jogo.",
    "Atacante com visão para os passes decisivos.",
    "Zagueiro que domina o jogo aéreo.",
    "Goleiro que defende pênaltis com tranquilidade.",
    "Meio-campista que cria oportunidades em jogadas de bola parada.",
    "Atacante que finaliza de forma espetacular.",
    "Defensor que desarma os adversários com destreza.",
    "Meio-campista que distribui assistências precisas.",
    "Atacante que dribla com facilidade.",
    "Zagueiro que bloqueia os chutes adversários com firmeza.",
    "Goleiro que mantém a calma sob pressão.",
    "Defensor que faz desarmes cruciais.",
    "Meio-campista com passes precisos de longa distância.",
    "Atacante que finaliza com eficácia nas situações de um contra um.",
    "Meio-campista que lidera a pressão na defesa adversária.",
    "Atacante com grande presença na área e cabeceio forte.",
    "Zagueiro que é uma rocha na defesa.",
    "Goleiro que brilha em defesas difíceis.",
    "Meio-campista que cria oportunidades com sua visão de jogo.",
    "Atacante que marca gols em momentos cruciais.",
    "Defensor que bloqueia cruzamentos com autoridade.",
    "Meio-campista com visão panorâmica do campo.",
    "Atacante que dribla com maestria os defensores.",
    "Zagueiro que é uma muralha na defesa.",
    "Goleiro que realiza defesas espetaculares.",
    "Meio-campista com passes precisos e visão de jogo incrível.",
    "Atacante que finaliza com precisão cirúrgica.",
    "Defensor que desarma com eficiência os adversários.",
    "Meio-campista que distribui assistências de primeira classe.",
    "Atacante que cria jogadas a partir do nada.",
    "Zagueiro que bloqueia chutes com coragem.",
    "Goleiro que inspira confiança à equipe.",
    "Defensor que não dá espaço aos atacantes adversários.",
    "Meio-campista que domina o jogo no meio de campo.",
    "Atacante com faro de gol aguçado.",
    "Zagueiro que lidera a defesa com autoridade.",
    "Goleiro com reflexos incríveis.",
    "Meio-campista que cria oportunidades com passes decisivos.",
    "Atacante que finaliza com precisão em situações de um contra um.",
    "Defensor que bloqueia chutes com determinação.",
    "Meio-campista que dita o ritmo do jogo com maestria.",
    "Atacante com grande mobilidade e finalização letal.",
    "Goleiro que brilha em defesas difíceis.",
    "Defensor que protege a área com eficácia.",
    "Meio-campista com visão de jogo excepcional.",
    "Atacante que marca gols decisivos.",
    "Zagueiro que corta cruzamentos com precisão.",
    "Goleiro com agilidade e confiança.",
    "Meio-campista que distribui passes precisos de longa distância.",
    "Atacante que dribla com facilidade.",
    "Defensor que bloqueia chutes perigosos com coragem.",
    "Meio-campista que lidera a equipe com inteligência.",
    "Atacante com faro de gol em jogadas aéreas.",
    "Zagueiro que domina o jogo aéreo na defesa.",
    "Goleiro que defende pênaltis com tranquilidade.",
    "Meio-campista com habilidades de cobrança de falta.",
    "Atacante que finaliza com frieza nas situações de um contra um.",
    "Defensor que impede avanços adversários com segurança.",
    "Meio-campista com inteligência tática excepcional.",
    "Atacante com movimentação impressionante.",
    "Goleiro que mantém a calma na área.",
    "Defensor que não dá espaço aos atacantes.",
    "Meio-campista que controla o ritmo do jogo.",
    "Atacante com visão para os passes decisivos.",
    "Zagueiro que domina o jogo aéreo com maestria.",
    "Goleiro que defende pênaltis com tranquilidade.",
    "Meio-campista que cria oportunidades em jogadas de bola parada.",
    "Atacante que finaliza de forma espetacular.",
    "Defensor que desarma os adversários com destreza.",
    "Meio-campista que distribui assistências precisas.",
    "Atacante que dribla com maestria os defensores.",
    "Zagueiro que é uma muralha na defesa.",
    "Goleiro que realiza defesas espetaculares.",
    "Meio-campista com passes precisos e visão de jogo incrível.",
    "Atacante que finaliza com precisão cirúrgica.",
    "Defensor que desarma com eficiência os adversários.",
    "Meio-campista que distribui assistências de primeira classe.",
    "Atacante que cria jogadas a partir do nada.",
    "Zagueiro que bloqueia chutes com coragem.",
    "Goleiro que inspira confiança à equipe.",
    "Defensor que não dá espaço aos atacantes adversários.",
    "Meio-campista que domina o jogo no meio de campo."
]


# Verifique se as listas têm o mesmo comprimento
if len(nomes_jogadores) == len(descricoes):
    print(f"As duas listas têm {len(nomes_jogadores)} linhas, e a correspondência está correta.")
else:
    print(f"As duas listas têm comprimentos diferentes. Nomes de jogadores: {len(nomes_jogadores)}, Descrições: {len(descricoes)}")



# Verifique se a lista de nomes de jogadores e descrições tem o mesmo comprimento
if len(nomes_jogadores) == len(descricoes):
    # Crie um arquivo CSV para armazenar as informações das figurinhas
    with open('figurinhas.csv', 'w', newline='') as csvfile:
        # Defina os nomes das colunas no arquivo CSV
        fieldnames = ["Numero", "Jogador", "Informacao", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Escreva o cabeçalho no arquivo CSV
        writer.writeheader()
        
        # Escreva as informações das figurinhas no arquivo CSV
        for numero, jogador, informacao in zip(range(1, len(nomes_jogadores) + 1), nomes_jogadores, descricoes):
            writer.writerow({"Numero": numero, "Jogador": jogador, "Informacao": informacao, "Status": 0})
        
    print("Arquivo CSV 'figurinhas.csv' foi criado com sucesso.")
else:
    print("Erro: As listas de nomes de jogadores e descrições têm comprimentos diferentes.")
