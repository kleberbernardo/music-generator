# Music Generator

Este projeto é um gerador de músicas automatizado que utiliza a API da Suno para criar músicas com base em um prompt e tags fornecidas. O script também baixa e salva a música gerada localmente.

## Funcionalidades

- Gera um título aleatório para a música
- Faz requisições para gerar música utilizando a API da Suno
- Obtém os detalhes do clipe gerado
- Baixa o arquivo de áudio e salva localmente

## Tecnologias Utilizadas

- Python
- Biblioteca `requests` para fazer requisições HTTP

## Configuração do Ambiente

1. Clone o repositório:
    ```sh
    git clone https://github.com/kleberbernardo/music-generator.git
    cd music-generator
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Edite o arquivo `music_generator.py` para incluir sua chave de API e parâmetros desejados:
    ```python
    api_key = "sua_chave_de_api"
    prompt = "texto"
    tags = "estilo"
    ```

2. Execute o script:
    ```sh
    python music_generator.py
    ```

3. As músicas geradas serão salvas na pasta `musics/`.

## Estrutura do Código

- **generate_random_title**: Função para gerar um título aleatório.
- **generate_music**: Função para gerar a música utilizando a API da Suno.
- **get_generated_music**: Função para obter os detalhes do clipe gerado.
- **download_audio**: Função para baixar o arquivo de áudio.
- **generate_random_filename**: Função para gerar um nome de arquivo aleatório baseado no tempo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

