INSTAGRAM_USERNAME = "" 
INSTAGRAM_PASSWORD = ""
INSTAGRAM_URL = "https://www.instagram.com/"

MAIN_PATH = "C:/data/"
VIDEOS_DIRECTORY = MAIN_PATH + "videos/"
OUTPUT_DIRECTORY = MAIN_PATH + "outputs/"
URLS_DIRECTORY = MAIN_PATH + "urls/"
ARCHIVE_DIRECTORY = MAIN_PATH + "archives/"
COOKIES_PATH = MAIN_PATH + "cookies.txt"

VIDEO_MIN_DURATION = 5 * 60
VIDEO_MAX_DURATION = 10 * 60
CLIP_MIN_DURATION = 6
CLIP_MAX_DURATION = 30
INSTAGRAM_VIDEO_MAX_DOWNLOAD_SIZE = "15M"

DAILY_SCHEDULED_TIME = "20:00"

CHAT_GPT_API_KEY = ""


#  gere uma lista de 10 hashtags para um video sobre peixes no youtube e gere uma descrição genérica no maximo 50 palavras para um video sobre peixes engraçados e incríveis

DESCRIPTION_END_TEMPLATE = """

Não clique aqui:
URL

Se inscreva no canal para mais vídeos e não se esqueça de deixar seu Like. Obrigado.
URL

Para fazer compilações, usamos vídeos enviados pelos autores (conforme reivindicado).
Se você é o autor do vídeo e não enviou o vídeo para o nosso canal, envie-nos uma mensagem privada e removeremos imediatamente o seu vídeo.
"""

CONTENT_TABLE = [
    {
      "subject": "animals",
      "prompt": "Gere um titulo click bait para um video sobre animais engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['animais', 'natureza', 'vida selvagem', 'fauna', 'biodiversidade', 'ecossistema', 'safari', 'documentário', 'zoologia', 'conservação'],
      "youtube_description": 
"""Prepare-se para dar boas risadas enquanto conhece alguns dos animais mais engraçados e surpreendentes do mundo.
Veja como eles se divertem, interagem e nos surpreendem com suas habilidades únicas.
Assista a este vídeo e encante-se com a vida selvagem de uma forma divertida e emocionante.
""",
    },
    {
      "subject": "birds",
      "prompt": "Gere um titulo click bait para um video sobre pássaros incríveis no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['aves', 'passaros', 'natureza', 'avesincríveis', 'ornitologia', 'observaçãodepássaros', 'avesexóticas', 'vida selvagem', 'biodiversidade', 'documentário'],
      "youtube_description": 
"""Este vídeo apresenta algumas das aves mais impressionantes do mundo, com suas cores vibrantes, voos graciosos e cantos únicos.
Descubra como essas criaturas fascinantes contribuem para a biodiversidade.
Assista e encante-se com a beleza da vida selvagem das aves.
""",
    },
    {
      "subject": "cats",
      "prompt": "Gere um titulo click bait para um video sobre gatos engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['gatos', 'gatosengraçados', 'amomeugato', 'gatopretinho', 'gatobranco', 'miau', 'petlovers', 'catlovers', 'diversãofelina', 'fofura'],
      "youtube_description": 
"""Se você é um amante de gatos, não pode perder este vídeo!
Descubra a personalidade divertida e única desses animais adoráveis, veja suas habilidades impressionantes e ria com suas travessuras.
Assista e se divirta com este vídeo emocionante sobre gatos engraçados e incríveis.
""",
    },
    {
      "subject": "ducks",
      "prompt": "Gere um titulo click bait para um video sobre patos engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['patos', 'patosnadando', 'patosfofos', 'avesaquáticas', 'natureza', 'animais', 'birdwatching', 'pássaros', 'patinhos', 'mundoanimal'],
      "youtube_description": 
"""Prepare-se para se encantar com a personalidade engraçada e as habilidades incríveis dos patos!
Este vídeo apresenta os momentos mais divertidos e fofos dessas aves aquáticas, enquanto elas nadam, interagem e brincam.
Assista e se divirta com este vídeo emocionante sobre patos engraçados e incríveis.
""",
    },
    {
      "subject": "fishes",
      "prompt": "Gere um titulo click bait para um video sobre peixes engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['peixes', 'aquarismo', 'peixesexóticos', 'peixinhos', 'natureza', 'aquariofilia', 'biodiversidade', 'animaisaquáticos', 'mundoanimal', 'peixesdivertidos'],
      "youtube_description": 
"""Assista a este vídeo e conheça os peixes mais engraçados e surpreendentes do mundo aquático.
Descubra como essas criaturas incríveis nadam, se comunicam e interagem, enquanto você se diverte com suas travessuras e personalidades únicas.
Este vídeo é garantia de muita diversão e emoção para todos os amantes de peixes!
""",
    },
    {
      "subject": "germanshepherds",
      "prompt": "Gere um titulo click bait para um video sobre peixes engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['pastoralemão', 'cachorro', 'cães', 'amocachorro', 'pets', 'cachorrosbrasil', 'adestramento', 'melhoramigo', 'companheiro', 'doglovers'],
      "youtube_description": 
"""Se você é fã de pastor alemão, não pode perder este vídeo!
Veja as habilidades incríveis e a personalidade divertida desses cães maravilhosos, e ria com suas travessuras.
Assista e se encante com este vídeo emocionante sobre pastor alemão engraçados e incríveis, que vai conquistar o seu coração!
""",
    },
    {
      "subject": "golden",
      "prompt": "Gere um titulo click bait para um video sobre peixes engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['goldenretriever', 'cachorro', 'cães', 'amocachorro', 'pets', 'cachorrosbrasil', 'adestramento', 'melhoramigo', 'companheiro', 'doglovers'],
      "youtube_description": 
"""Preparado para se encantar com os Golden Retrievers mais engraçados e incríveis do mundo?
Assista a este vídeo e conheça a personalidade encantadora e as habilidades incríveis desses cães maravilhosos.
Ria com suas brincadeiras e se emocione com suas histórias inspiradoras.
Este vídeo é garantia de muita diversão e emoção para todos os amantes de Golden Retrievers!
""",
    },
    {
      "subject": "labrador",
      "prompt": "Gere um titulo click bait para um video sobre labradores engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ["labrador", "dogs", "cachorros", "engraçado", "funny", "fofo", "cachorrinho", "cachorro", "dog", "rir", "brincar", "compilação"],
      "youtube_description": 
"""Este vídeo é uma compilação dos cachorros labradores mais engraçados e fofos que você já viu!
Prepare-se para dar boas gargalhadas e se apaixonar por esses adoráveis cãezinhos de quatro patas.
""",
    },
    {
      "subject": "snakes",
      "prompt": "Gere um titulo click bait para um video sobre cobras engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags": ['cobras', 'animais', 'repteis', 'natureza', 'curiosidades', 'bichos', 'safari', 'biologia', 'herpetologia', 'serpentes'],
      "youtube_description": 
"""Você não vai acreditar no que as cobras são capazes de fazer!
Neste vídeo incrível, você vai conhecer as cobras mais engraçadas e fascinantes do mundo, e descobrir curiosidades surpreendentes sobre esses animais incríveis.
Prepare-se para se divertir e se encantar com as cobras mais incríveis que você já viu!
""",
    },
    {
      "subject": "chickens",
      "prompt": "Gere um titulo click bait para um video sobre galinhas engraçados no youtube, o titulo deve ter entre 4 a 8 palavras e não deve incluir números. Sempre gere um titulo unico.",
      "youtube_tags":  ['galinhas', 'animais', 'aves', 'natureza', 'curiosidades', 'bichos', 'fazenda', 'agricultura', 'ovos', 'galinheiro'],
      "youtube_description": 
"""Quem disse que as galinhas não são animais incríveis e engraçados?
Neste vídeo, você vai se surpreender com as habilidades surpreendentes e as personalidades divertidas desses animais de fazenda tão populares.
Venha conhecer as galinhas mais engraçadas e incríveis que você já viu e se encantar com esses animais maravilhosos!
""",
    },
]