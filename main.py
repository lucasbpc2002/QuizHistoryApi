from re import I
from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    # idade antiga
    {
        "id":
        1,
        "age":
        2,
        "difficulty":
        1,
        "question":
        "Qual foi a principal contribuição dos fenícios para as civilizações posteriores?",
        "options": [
            "Construção de pirâmides", "Criação do alfabeto fonético",
            "Desenvolvimento da filosofia", "Descoberta da pólvora"
        ],
        "answer":
        "Criação do alfabeto fonético"
    },
    {
        "id": 2,
        "age": 2,
        "difficulty": 1,
        "question": "Em qual rio se desenvolveu a civilização egípcia?",
        "options": ["Tigre", "Eufrates", "Nilo", "Ganges"],
        "answer": "Nilo"
    },
    {
        "id":
        3,
        "age":
        2,
        "difficulty":
        1,
        "question":
        "Qual império dominou grande parte do Oriente Médio antes da ascensão de Roma?",
        "options": [
            "Império Persa", "Império Babilônico", "Império Hitita",
            "Império Sumério"
        ],
        "answer":
        "Império Persa"
    },
    {
        "id": 4,
        "age": 2,
        "difficulty": 2,
        "question": "Quem foi o primeiro imperador de Roma?",
        "options": ["César", "Augusto", "Nero", "Trajano"],
        "answer": "Augusto"
    },
    {
        "id": 5,
        "age": 2,
        "difficulty": 2,
        "question":
        "A escrita cuneiforme foi desenvolvida por qual civilização? ",
        "options": ["Egípcia ", "Mesopotâmica", "Chinesa", "Grega"],
        "answer": "Mesopotâmica"
    },
    {
        "id": 6,
        "age": 2,
        "difficulty": 1,
        "question":
        "Qual das seguintes civilizações foi responsável pela criação do Código de Hamurabi, um dos primeiros conjuntos de leis escritas? ",
        "options": ["Egípcia", "Babilônica", "Grega", "Romana"],
        "answer": "Babilônica"
    },
    {
        "id":
        7,
        "age":
        2,
        "difficulty":
        1,
        "question":
        "Qual foi a principal característica do governo espartano? ",
        "options": [
            "Democracia", "Oligarquia militar", "Teocracia",
            "Monarquia absoluta"
        ],
        "answer":
        "Oligarquia militar"
    },
    {
        "id":
        8,
        "age":
        2,
        "difficulty":
        3,
        "question":
        "Qual foi o impacto da Batalha de Qadesh entre egípcios e hititas na história política do Oriente Próximo?",
        "options": [
            "A conquista definitiva do território hitita pelo Egito",
            " A consolidação do primeiro tratado de paz conhecido na história",
            "A expansão do Império Egípcio até o rio Eufrates",
            "O declínio simultâneo dos impérios egípcio e hitita devido às perdas na batalha"
        ],
        "answer":
        " A consolidação do primeiro tratado de paz conhecido na história"
    },
    {
        "id": 9,
        "age": 2,
        "difficulty": 1,
        "question": "Quem era o deus principal da mitologia egípcia? ",
        "options": ["Rá", "Zeus", "Osíris", "Hórus"],
        "answer": "Rá"
    },
    {
        "id": 10,
        "age": 2,
        "difficulty": 1,
        "question":
        "Qual é o nome do grande poema épico atribuído a Homero que conta as aventuras de Odisseu? ",
        "options": ["Ilíada", "Eneida", "Odisseia", "Mahabharata"],
        "answer": "Odisseia"
    },
    {
        "id": 11,
        "age": 2,
        "difficulty": 2,
        "question": "A invenção da pólvora é atribuída a qual civilização? ",
        "options": ["Indiana", "Egípcia", "Chinesa", "Mesopotâmica"],
        "answer": "Chinesa"
    },
    {
        "id":
        12,
        "age":
        2,
        "difficulty":
        2,
        "question":
        "Quem foi o líder que conquistou um dos maiores impérios da Antiguidade, estendendo-se da Grécia à Índia? ",
        "options":
        ["Júlio César", "Alexandre, o Grande", "Dario I ", "Nabucodonosor "],
        "answer":
        "Alexandre, o Grande"
    },
    {
        "id": 13,
        "age": 2,
        "difficulty": 2,
        "question":
        "Qual era o principal material usado para a escrita pelos sumérios? ",
        "options": ["Papiro", "Pedra", "Argila", "Madeira"],
        "answer": "Argila"
    },
    {
        "id": 14,
        "age": 2,
        "difficulty": 2,
        "question":
        "Qual era a principal atividade econômica da civilização cretense?",
        "options":
        ["Agricultura", "Comércio marítimo ", "Mineração ", "Pastoril"],
        "answer": "Comércio marítimo"
    },
    {
        "id":
        15,
        "age":
        2,
        "difficulty":
        1,
        "question":
        "O que marcou a transição entre a Pré-História e a Idade Antiga? ",
        "options": [
            " Descoberta do fogo", "Domesticação de animais",
            "Invenção da escrita ", "Uso de ferramentas de pedra polida "
        ],
        "answer":
        "Invenção da escrita"
    },
    {
        "id": 16,
        "age": 2,
        "difficulty": 2,
        "question":
        "Quem foi o filósofo grego que ensinou Alexandre, o Grande?",
        "options": [" Sócrates", "Platão", "Aristóteles", "Heráclito"],
        "answer": "Aristóteles"
    },
    {
        "id": 17,
        "age": 2,
        "difficulty": 1,
        "question":
        "Qual cidade foi destruída pela erupção do Monte Vesúvio em 79 d.C.? ",
        "options": [" Atenas", "Pompeia", "Cartago", "Roma"],
        "answer": "Pompeia"
    },
    {
        "id": 18,
        "age": 2,
        "difficulty": 1,
        "question": "Quem era o deus principal da mitologia romana?",
        "options": ["Apolo", "Júpiter", "Saturno", "Plutão"],
        "answer": "Júpiter"
    },
    {
        "id": 19,
        "age": 2,
        "difficulty": 2,
        "question":
        "Qual cidade foi conhecida por seus jardins suspensos, uma das sete maravilhas do mundo antigo? ",
        "options": ["Babilônia", "Roma", "Alexandria", "Atenas"],
        "answer": "Babilônia"
    },
    {
        "id": 20,
        "age": 2,
        "difficulty": 1,
        "question": "Qual povo é considerado o criador da democracia? ",
        "options": ["Egípcios", "Romanos", "Gregos", "Fenícios"],
        "answer": "Gregos"
    },
    {
        "id": 21,
        "age": 2,
        "difficulty": 1,
        "question": "Quem foi o deus da guerra na mitologia grega?",
        "options": ["Ares", "Hermes", "Poseidon", "Hades"],
        "answer": "Ares"
    },
    {
        "id":
        22,
        "age":
        2,
        "difficulty":
        3,
        "question":
        "Qual foi a principal inovação arquitetônica dos romanos, que influenciou diversas civilizações posteriores? ",
        "options": [
            "Arco e abóbada", "Estilo coríntio", "Uso de colunas dônicas",
            "Construção de zigurates"
        ],
        "answer":
        "Arco e abóbada"
    },
    {
        "id":
        23,
        "age":
        2,
        "difficulty":
        3,
        "question":
        "Em qual batalha os gregos derrotaram os persas, consolidando a hegemonia ateniense no período clássico?",
        "options": [
            "Batalha de Salamina", " Batalha de Maratona",
            "Batalha de Plateia", "Batalha de Queroneia"
        ],
        "answer":
        "Batalha de Salamina"
    },
    {
        "id":
        24,
        "age":
        2,
        "difficulty":
        3,
        "question":
        "Qual foi o maior legado do Código de Hamurabi para o desenvolvimento jurídico? ",
        "options": [
            "A aplicação da pena de morte",
            "O princípio de talão (olho por olho, dente por dente)",
            "A codificação escrita das leis",
            "A separação entre leis religiosas e civis "
        ],
        "answer":
        "A codificação escrita das leis"
    },
    {
        "id": 25,
        "age": 2,
        "difficulty": 3,
        "question":
        "Qual filósofo pré-socrático foi o primeiro a propor que a água era o princípio fundamental (arché) de todas as coisas? ",
        "options":
        ["Parmênides", "Anaximandro", "Tales de Mileto", "Empédocles"],
        "answer": "Tales de Mileto"
    },
    {
        "id":
        26,
        "age":
        2,
        "difficulty":
        3,
        "question":
        "Qual foi o objetivo principal da construção do Farol de Alexandria?",
        "options": [
            "Servir como templo ao deus Rá",
            "Orientar as embarcações e fortalecer o comércio",
            " Guardar tesouros da dinastia ptolemaica",
            "Proteger o porto contra ataques navais"
        ],
        "answer":
        "Orientar as embarcações e fortalecer o comércio"
    },

    # idade media
    {
        "id":
        27,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "Qual evento marcou o início da Idade Média? ",
        "options": [
            "Queda de Roma", "Descobrimento da América",
            "Revolução Industrial", "Coroação de Carlos Magno"
        ],
        "answer":
        "Queda de Roma"
    },
    {
        "id":
        28,
        "age":
        3,
        "difficulty":
        2,
        "question":
        "Quem foi o líder militar que unificou os francos no século VIII? ",
        "options": [
            "Carlos Magno", "Pepino, o breve", "Clóvis",
            "Ricardo Coração de Leão"
        ],
        "answer":
        "Clóvis"
    },
    {
        "id":
        29,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "O que foi o feudalismo? ",
        "options": [
            "Um sistema político e econômico baseado na terra",
            "Uma religião medieval", "Um estilo arquitetônico da Idade Média",
            "Um sistema de comércio marítimo "
        ],
        "answer":
        "Um sistema político e econômico baseado na terra"
    },
    {
        "id":
        30,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "Qual foi a principal motivação das Cruzadas?",
        "options": [
            "Expansão comercial",
            "Reconquista de territórios cristãos no Oriente Médio",
            "Defesa contra os vikings", "Combate às heresias na Europa"
        ],
        "answer":
        "Reconquista de territórios cristãos no Oriente Médio"
    },
    {
        "id": 31,
        "age": 3,
        "difficulty": 1,
        "question": "Qual o nome do escritor  de A Divina Comédia? ",
        "options": ["Dante Alighieri", "Maquiavel", "Boccaccio", "Petrarca"],
        "answer": "Dante Alighieri"
    },
    {
        "id":
        32,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "Qual foi o papel principal da Igreja Católica durante a Idade Média?",
        "options": [
            "Promover as Cruzadas e expandir seu território",
            "Controlar a vida política, cultural e espiritual",
            "Reduzir os impostos sobre os camponeses",
            "Liderar os movimentos de reforma religiosa"
        ],
        "answer":
        "Controlar a vida política, cultural e espiritual"
    },
    {
        "id":
        33,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "O que eram os servos no sistema feudal?",
        "options": [
            "Trabalhadores livres em busca de terras",
            "Agricultores dependentes que deviam obrigações ao senhor feudal",
            "Soldados treinados para proteger os feudos",
            "Nobres que controlavam as terras"
        ],
        "answer":
        "Agricultores dependentes que deviam obrigações ao senhor feudal"
    },
    {
        "id":
        34,
        "age":
        3,
        "difficulty":
        2,
        "question":
        "Qual documento, assinado em 1215, limitou o poder do rei na Inglaterra? ",
        "options": [
            "Tratado de Verdum", "Declaração de Direitos Humanos",
            "Magna Carta", " Pacto de Paz"
        ],
        "answer":
        "Magna Carta"
    },
    {
        "id": 35,
        "age": 3,
        "difficulty": 1,
        "question":
        "Quem liderou a França na Batalha de Orléans durante a Guerra dos Cem Anos? ",
        "options": ["Joana d'Arc", "Carlos Magno", "Henrique V", " Luís XI"],
        "answer": "Joana d'Arc"
    },
    {
        "id":
        36,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "O que foi a peste negra? ",
        "options": [
            "Uma guerra religiosa na Europa ",
            " Uma doença devastadora que matou milhões de pessoas",
            "Uma rebelião de camponeses contra os senhores feudais",
            "Uma praga de gafanhotos que arrasou colheitas"
        ],
        "answer":
        " Uma doença devastadora que matou milhões de pessoas"
    },
    {
        "id":
        37,
        "age":
        3,
        "difficulty":
        2,
        "question":
        "Qual foi a principal rota de comércio entre a Europa e a Ásia durante a Idade Média?",
        "options": [
            "Rota da Seda", "Caminho das Especiarias", "Estrada do Ferro",
            "Via Transatlântica"
        ],
        "answer":
        "Rota da Seda"
    },
    {
        "id":
        38,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "Qual foi a principal função dos castelos medievais? ",
        "options": [
            "Serem residências de luxo ", "Fortalezas para proteção militar",
            "Centros religiosos", "Palcos de festivais e torneios"
        ],
        "answer":
        "Fortalezas para proteção militar"
    },
    {
        "id": 39,
        "age": 3,
        "difficulty": 1,
        "question":
        "Qual era o idioma utilizado pela Igreja e pela educação na Idade Média?",
        "options": ["Latim", "Grego", "Francês", "Inglês"],
        "answer": "Latim"
    },
    {
        "id": 40,
        "age": 3,
        "difficulty": 2,
        "question":
        "Quem foi o primeiro imperador do Sacro Império Romano-Germânico? ",
        "options": ["Carlos Magno", "Otão I", "Frederico II ", "Henrique IV"],
        "answer": "Carlos Magno"
    },
    {
        "id":
        41,
        "age":
        3,
        "difficulty":
        2,
        "question":
        "O que foi o Cisma do Oriente, ocorrido em 1054?",
        "options": [
            "Divisão entre as Igrejas Católica e Ortodoxa",
            "Divisão entre os reinos do norte e do sul da França",
            "Separação entre o feudalismo e a monarquia",
            "Criação das Cruzadas"
        ],
        "answer":
        "Divisão entre as Igrejas Católica e Ortodoxa"
    },
    {
        "id": 42,
        "age": 3,
        "difficulty": 1,
        "question":
        "Qual povo invadiu a Europa na Alta Idade Média e era conhecido por sua habilidade em navegação? ",
        "options": ["Mongóis", "Saxões", "Vikings", "Hunos"],
        "answer": "Vikings"
    },
    {
        "id":
        43,
        "age":
        3,
        "difficulty":
        2,
        "question":
        "Quem foi o autor da obra A Cidade de Deus, amplamente lida na Idade Média?",
        "options":
        ["Santo Agostinho", "São Tomás de Aquino", "Pedro Abelardo", "Boécio"],
        "answer":
        "Santo Agostinho"
    },
    {
        "id":
        44,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "A Guerra dos Cem Anos foi travada entre quais países? ",
        "options": [
            "Inglaterra e França", "Espanha e Portugal", "França e Alemanha",
            "Itália e Espanha"
        ],
        "answer":
        "Inglaterra e França"
    },
    {
        "id": 45,
        "age": 3,
        "difficulty": 2,
        "question": "Qual rei inglês ficou conhecido como Coração de Leão?",
        "options":
        ["Ricardo I", "João sem terra", "Henrique VIII", "Eduardo III"],
        "answer": "Ricardo I"
    },
    {
        "id":
        46,
        "age":
        3,
        "difficulty":
        1,
        "question":
        "O que foram as Cruzadas? ",
        "options": [
            "Expedições militares e religiosas para conquistar territórios islâmicos ",
            "Movimentos religiosos contra a Igreja Católica ",
            "Viagens de exploração marítima ", "Guerras civis na Inglaterra"
        ],
        "answer":
        "Expedições militares e religiosas para conquistar territórios islâmicos "
    },
    {
        "id":
        47,
        "age":
        3,
        "difficulty":
        3,
        "question":
        "O que foi a Querela das Investiduras?",
        "options": [
            "Um conflito entre feudos pelo controle de terras férteis",
            " A disputa entre Igreja e reinos pela nomeação de bispos",
            "A luta pela posse de relíquias sagradas entre cruzados",
            "Um movimento contra a expansão muçulmana na Península Ibérica "
        ],
        "answer":
        "A disputa entre Igreja e reinos pela nomeação de bispos"
    },
    {
        "id":
        48,
        "age":
        3,
        "difficulty":
        3,
        "question":
        "Qual foi o impacto da Batalha de Hastings, em 1066?",
        "options": [
            "A fundação do Sacro Império Romano-Germânico ",
            "A unificação dos reinos escandinavos ",
            "O estabelecimento do domínio normando na Inglaterra ",
            "A expansão do cristianismo na Europa Central "
        ],
        "answer":
        "O estabelecimento do domínio normando na Inglaterra "
    },
    {
        "id":
        49,
        "age":
        3,
        "difficulty":
        3,
        "question":
        "Durante o reinado de Carlos Magno, qual instituição foi reformada para fortalecer o governo? ",
        "options": [
            "O exército feudal", "A educação e o sistema monástico",
            "A economia agrícola", "As relações entre vassalos e suseranos"
        ],
        "answer":
        "A educação e o sistema monástico"
    },
    {
        "id":
        50,
        "age":
        3,
        "difficulty":
        3,
        "question":
        "O que foi a Liga Hanseática?",
        "options": [
            "Uma aliança militar formada para combater os vikings ",
            "Uma confederação de cidades comerciais no norte da Europa",
            "Um tratado entre os reinos germânicos e o Império Bizantino",
            " Uma organização religiosa para promover as Cruzadas "
        ],
        "answer":
        "Uma confederação de cidades comerciais no norte da Europa"
    },
    {
        "id":
        51,
        "age":
        3,
        "difficulty":
        3,
        "question":
        "Qual fator contribuiu para a queda da Ordem dos Templários no século XIV? ",
        "options": [
            "A derrota nas Cruzadas", "A rivalidade com os Hospitalários ",
            "As acusações de heresia e perseguição pelo rei Felipe IV da França",
            "O declínio da autoridade papal no Ocidente"
        ],
        "answer":
        "As acusações de heresia e perseguição pelo rei Felipe IV da França"
    },

    # idade contemporanea
    {
        "id":
        52,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi a principal causa da Revolução Francesa?",
        "options": [
            "Expansão colonial", "Desigualdade social e econômica",
            " Reformas protestantes", "Ascensão do comunismo"
        ],
        "answer":
        "Desigualdade social e econômica"
    },
    {
        "id":
        53,
        "age":
        5,
        "difficulty":
        2,
        "question":
        "Quem liderou a independência das colônias espanholas na América? ",
        "options":
        ["Simon Bolívar", "Dom Pedro I", "George Washington", "Fidel Castro"],
        "answer":
        "Simon Bolívar"
    },
    {
        "id":
        54,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o estopim da Primeira Guerra Mundial? ",
        "options": [
            "A invasão da Polônia",
            "A morte do arquiduque Francisco Ferdinando",
            "O ataque a Pearl Harbor", "O tratado de Versalhes"
        ],
        "answer":
        "A morte do arquiduque Francisco Ferdinando"
    },
    {
        "id":
        55,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o objetivo da Revolução Industrial?",
        "options": [
            "Substituir o feudalismo ", "Modernizar as práticas agrícolas",
            "Automatizar a produção industrial", "Proteger as artes manuais"
        ],
        "answer":
        "Automatizar a produção industrial"
    },
    {
        "id":
        56,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Quem foi o líder da Alemanha nazista durante a Segunda Guerra Mundial? ",
        "options": [
            "Benito Mussolini", "Adolf Hitler", "Joseph Stalin",
            "Winston Churchill"
        ],
        "answer":
        "Adolf Hitler"
    },
    {
        "id":
        57,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o principal líder da Revolução Russa de 1917?",
        "options": [
            "Vladimir Lenin", "Joseph Stalin", "Leon Trotsky",
            "Nikita Khrushchev"
        ],
        "answer":
        "Vladimir Lenin"
    },
    {
        "id":
        58,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "O que foi o Tratado de Versalhes?",
        "options": [
            "Um acordo que encerrou a Primeira Guerra Mundial",
            " Um tratado entre Napoleão e seus inimigos",
            "O fim da Guerra dos Trinta Anos",
            "Um pacto de cooperação entre EUA e URSS"
        ],
        "answer":
        "Um acordo que encerrou a Primeira Guerra Mundial"
    },
    {
        "id":
        59,
        "age":
        5,
        "difficulty":
        2,
        "question":
        "Quem foi o presidente dos EUA durante a maior parte da Segunda Guerra Mundial?",
        "options": [
            "Franklin D. Roosevelt", "Harry Truman", "Dwight Eisenhower",
            "John F. Kennedy"
        ],
        "answer":
        "Franklin D. Roosevelt"
    },
    {
        "id":
        60,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual evento marcou simbolicamente o início da Idade Contemporânea?",
        "options": [
            "A Revolução Francesa", "A Primeira Guerra Mundial",
            "A Queda de Constantinopla", "A Revolução Industrial "
        ],
        "answer":
        " A Revolução Francesa "
    },
    {
        "id":
        61,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi a principal causa da Guerra Fria? ",
        "options": [
            " Rivalidade ideológica entre EUA e URSS ",
            "Disputas territoriais na Europa ",
            " Conflitos entre França e Inglaterra",
            "A corrida pela exploração espacial"
        ],
        "answer":
        " Rivalidade ideológica entre EUA e URSS "
    },
    {
        "id":
        62,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o principal objetivo da Organização das Nações Unidas (ONU)?",
        "options": [
            "Promover a paz e a segurança internacional",
            "Controlar as economias globais",
            " Liderar campanhas de exploração espacial ",
            "Expandir o comércio marítimo"
        ],
        "answer":
        "Promover a paz e a segurança internacional"
    },
    {
        "id":
        63,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Quem foi Nelson Mandela?",
        "options": [
            "Líder da luta contra o apartheid na África do Sul",
            "Presidente dos Estados Unidos durante a Guerra do Vietnã",
            "Primeiro-ministro britânico na Segunda Guerra Mundial ",
            "Líder da Revolução Cubana"
        ],
        "answer":
        "Líder da luta contra o apartheid na África do Sul"
    },
    {
        "id":
        64,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o impacto do Plano Marshall? ",
        "options": [
            "Reconstrução econômica da Europa após a Segunda Guerra Mundial",
            "Expansão do comunismo na América Latina",
            "Fortalecimento do comércio entre Ásia e Europa", "Criação da OTAN"
        ],
        "answer":
        "Reconstrução econômica da Europa após a Segunda Guerra Mundial"
    },
    {
        "id": 65,
        "age": 5,
        "difficulty": 1,
        "question": "Quem foi o líder da Revolução Cubana? ",
        "options":
        ["Che Guevara", "Fidel Castro", "Hugo Chávez", "Simon Bolívar"],
        "answer": "Fidel Castro"
    },
    {
        "id":
        66,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi a principal consequência da Revolução Industrial? ",
        "options": [
            "Urbanização e aumento da produção industrial",
            "Expansão do feudalismo", "Declínio das grandes navegações",
            "Domínio europeu na Ásia"
        ],
        "answer":
        "Urbanização e aumento da produção industrial"
    },
    {
        "id":
        67,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi o impacto do ataque a Pearl Harbor? ",
        "options": [
            "Entrada dos EUA na Segunda Guerra Mundial",
            " Declaração de independência dos EUA ",
            "Derrota do Japão na Primeira Guerra Mundial",
            "Formação da Liga das Nações"
        ],
        "answer":
        "Entrada dos EUA na Segunda Guerra Mundial"
    },
    {
        "id":
        68,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Quem foi o principal líder da independência da Índia?",
        "options": [
            "Jawaharlal Nehru", "Mahatma Gandhi", "Indira Gandhi",
            "Subhas Chandra Bose"
        ],
        "answer":
        "Mahatma Gandhi"
    },
    {
        "id":
        69,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "Qual foi a principal causa da crise de 1929? ",
        "options": [
            "Queda da bolsa de valores de Nova York",
            "A Primeira Guerra Mundial", "A Revolução Russa",
            "A ascensão do nazismo"
        ],
        "answer":
        "Queda da bolsa de valores de Nova York"
    },
    {
        "id":
        70,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "O que foi o D-Day, durante a Segunda Guerra Mundial?",
        "options": [
            "O desembarque das tropas aliadas na Normandia",
            "A criação da ONU", "A invasão do Japão pelos EUA",
            "A libertação de Berlim"
        ],
        "answer":
        "O desembarque das tropas aliadas na Normandia"
    },
    {
        "id":
        71,
        "age":
        5,
        "difficulty":
        1,
        "question":
        "O que a queda do Muro de Berlim simobolizou?",
        "options": [
            "O fim da Segunda Guerra Mundial",
            "A unificação da Alemanha e o fim da Guerra Fria ",
            "A criação da União Europeia",
            "O início da construção do Eurotúnel"
        ],
        "answer":
        " A unificação da Alemanha e o fim da Guerra Fria  "
    },
    {
        "id":
        72,
        "age":
        5,
        "difficulty":
        3,
        "question":
        "Qual foi o maior desafio político enfrentado pela União Europeia após a sua criação?",
        "options": [
            "A crise da dívida soberana de 2008", "A reunificação da Alemanha",
            "A inclusão de países do leste europeu",
            "O aumento do protecionismo comercial"
        ],
        "answer":
        "A crise da dívida soberana de 2008"
    },
    {
        "id":
        73,
        "age":
        5,
        "difficulty":
        3,
        "question":
        "Qual foi o principal objetivo da Conferência de Potsdam, realizada em 1945?",
        "options": [
            "Planejar a reconstrução da Europa após a Segunda Guerra Mundial",
            "Dividir a Alemanha entre as potências vencedoras",
            "Firmar alianças militares contra o Japão",
            "Estabelecer o início da Guerra Fria"
        ],
        "answer":
        "Dividir a Alemanha entre as potências vencedoras"
    },
    {
        "id":
        74,
        "age":
        5,
        "difficulty":
        3,
        "question":
        "Qual foi o impacto da Doutrina Truman no contexto da Guerra Fria?",
        "options": [
            "A aceleração da corrida espacial entre EUA e URSS",
            "O aumento da influência dos países do Terceiro Mundo",
            "O estabelecimento de ajuda militar e econômica contra a expansão do comunismo",
            "A dissolução do Pacto de Varsóvia"
        ],
        "answer":
        "O estabelecimento de ajuda militar e econômica contra a expansão do comunismo"
    },
    {
        "id":
        75,
        "age":
        5,
        "difficulty":
        3,
        "question":
        "Durante a Revolução Francesa, o que significava o lema: Liberdade, Igualdade, Fraternidade? ",
        "options": [
            "Um apelo à criação de uma monarquia constitucional ",
            "A justificativa para a expansão territorial francesa ",
            "A base ideológica para a democracia e os direitos civis",
            "A defesa da aliança entre o clero e a nobreza"
        ],
        "answer":
        "A base ideológica para a democracia e os direitos civis"
    },
    {
        "id":
        76,
        "age":
        5,
        "difficulty":
        3,
        "question":
        "Qual foi o papel do Tratado de Tordesilhas no contexto das grandes navegações? ",
        "options": [
            "Dividir as terras da América entre Espanha e Portugal",
            "Estabelecer rotas marítimas entre Europa e Ásia",
            "Criar acordos de comércio com povos indígenas",
            "Iniciar a exploração dos continentes africano e asiático "
        ],
        "answer":
        "Dividir as terras da América entre Espanha e Portugal"
    },
]


@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)


@app.route('/questions/<int:id>', methods=['GET'])
def get_question_by_id(id):
    # Procura a pergunta com o id fornecido
    question = next((q for q in questions if q['id'] == id), None)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    return jsonify(question)


@app.route('/questions/<int:age>/', methods=['GET'])
def get_question_by_age(age):
    # Procura a pergunta com o id fornecido
    lista = []
    lista_option=[]
    for q in questions:
        if (q['age'] == age):
            
            lista.append([q['id'],q['question'], q['answer'],q['options']])
            # lista.append(q['id'])
        # question = next((q for q in questions if q['age'] == age), lista.append(age))

    return jsonify(lista)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
