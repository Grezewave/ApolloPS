import csv

import requests

pacotes = [
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv-python",
    "django",
    "flask",
    "sqlalchemy",
    "beautifulsoup4",
    "requests",
    "scipy",
    "nltk",
    "networkx",
    "pillow",
    "seaborn",
    "plotly",
    "pygame",
    "wxpython",
    "pyaudio",
    "cryptography",
    "pypdf2",
    "pygame",
    "pyautogui",
    "selenium",
    "pytz",
    "arrow",
    "tweepy",
    "pyTelegramBotAPI",
    "pyqtgraph",
    "pytesseract",
    "googletrans",
    "pyinstaller",
    "psutil",
    "pandas-profiling",
    "python-docx",
    "xlrd",
    "xlsxwriter",
    "paramiko",
    "pyqrcode",
    "pymongo",
    "praw",
    "sympy",
    "python-docx",
    "pycrypto",
    "pyodbc",
    "pyusb",
    "pycurl"
]

# Criação do arquivo CSV
with open('informacoes_pacotes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Data de publicacao',
                    'Versao Python mais recente', 'Downloads no ultimo mes'])

    for pacote in pacotes:
        url = f"https://pypi.org/pypi/{pacote}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            name = data["info"]["name"]
            publication_date = data["releases"][data["info"]
                                                ["version"]][0]["upload_time"]
            python_version = data["info"]["requires_python"]
            downloads_last_month = data["info"]["downloads"]["last_month"]

            writer.writerow(
                [name, publication_date, python_version, downloads_last_month])
        else:
            print(f"Erro ao obter informações do pacote {pacote}")
