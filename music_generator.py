import os
import time
import random
import string
import requests

# Configurações iniciais
api_key = "sua_chave_de_api"
prompt = "texto"
tags = "estilo"

# Função para gerar um título aleatório
def generate_random_title():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Gerar um título aleatório
title = generate_random_title()

# Função para gerar música
def generate_music(api_key, prompt, tags, title, retries=3, delay=10):
    url = "https://api.sunoapi.com/api/v1/suno/create"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "tags": tags,
        "custom_mode": True,
        "title": title,
        "continue_at": 0,
        "continue_clip_id": ""
    }
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=600)
            if response.status_code == 200:
                task_id = response.json().get('data').get('task_id')
                print("Musica gerada com sucesso!")
                print("Task ID:", task_id)
                print("Iniciando processo de download e tratamento, aguarde...")
                return task_id
            else:
                print("Falha ao iniciar a geracao de musica.")
                print("Codigo de Status:", response.status_code)
                try:
                    print("Retorno JSON:", response.json())
                    print("Mensagem:", response.json().get('message'))
                except requests.exceptions.JSONDecodeError:
                    print("Erro ao decodificar resposta JSON.")
        except requests.exceptions.RequestException as e:
            print(f"Falha na requisicao: {e}")
        
        print(f"Retentativa em {delay} segundos, aguarde...")
        time.sleep(delay)
    
    print("Todas as tentativas falharam.")
    return None

# Função para obter os detalhes do clipe gerado
def get_generated_music(task_id, api_key):
    url = f"https://api.sunoapi.com/api/v1/suno/clip/{task_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        return response.json()
    else:
        print("Falha ao obter detalhes da musica.")
        print("Codigo de Status:", response.status_code)
        try:
            print("Mensagem:", response.json().get('message'))
        except requests.exceptions.JSONDecodeError:
            print("Erro ao decodificar resposta JSON.")
        return None

# Função para baixar o arquivo de áudio
def download_audio(audio_url, file_name):
    response = requests.get(audio_url, timeout=30)
    if response.status_code == 200:
        # Criar a pasta "musics" se não existir
        if not os.path.exists('musics'):
            os.makedirs('musics')
        file_path = os.path.join('musics', file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo de audio salvo como {file_path}")
    else:
        print("Falha ao baixar o arquivo de audio.")
        print("Codigo de Status:", response.status_code)

# Gerar um nome de arquivo aleatório baseado no tempo
def generate_random_filename():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    timestamp = str(int(time.time()))
    return f"{random_string}_{timestamp}_music.mp3"

# Gerar música
task_id = generate_music(api_key, prompt, tags, title)

if task_id:
    # Aguardar 30 segundos para a API gerar a música
    time.sleep(30)
    
    # Obter os detalhes do clipe gerado
    music_details = get_generated_music(task_id, api_key)
    
    if music_details:
        clips = music_details.get('data', {}).get('clips', {})
        if clips:
            clip_id, clip_info = next(iter(clips.items()))
            audio_url = clip_info.get('audio_url')
            if audio_url:
                # Gerar nome de arquivo aleatório
                random_filename = generate_random_filename()
                # Baixar o arquivo de áudio
                download_audio(audio_url, random_filename)
            else:
                print("URL de audio nao encontrada para o clipe:", clip_id)
        else:
            print("Nenhum clipe encontrado.")
