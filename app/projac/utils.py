import requests
from urllib.parse import urlparse, parse_qs

def get_lattes_photo_url(lattes_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:

        response = requests.get(lattes_url, allow_redirects=True, headers=headers)
        final_url = response.url
        parsed_url = urlparse(final_url)
        query_params = parse_qs(parsed_url.query)
        
        lattes_id = query_params.get('id', [None])[0]
        
        if lattes_id:
            photo_url = f"https://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id={lattes_id}"
            return photo_url
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar acessar a URL do Lattes: {e}")
        return None