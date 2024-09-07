from setuptools import setup, find_packages

setup(
    name='fraee',                # Nazwa pakietu
    version='0.1.0',                  # Wersja pakietu
    author='Franek S',               # Twoje imię i nazwisko
    author_email='franekmeme@gmail.com',  # Twój e-mail
    description='A simple package',  # Opis pakietu
    long_description=open('README.md').read(),  # Długi opis (zwykle zawarty w pliku README.md)
    long_description_content_type='text/markdown',  # Typ zawartości długiego opisu
    url='https://github.com/BottleOfSugar/Fraee',  # URL do repozytorium (jeśli jest)
    packages=find_packages(),         # Automatyczne znajdowanie wszystkich pakietów w projekcie
    classifiers=[                     # Klasyfikatory, które pomagają w kategoryzacji pakietu
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.12',          # Wymagana wersja Pythona
    install_requires=[                # Lista wymaganych pakietów
        'requests',                 
        'colorama',
        'psuntil' # Przykładowy pakiet, który może być wymagany
    ],
    extras_require={                  # Opcjonalne zależności
        'dev': ['pytest', 'sphinx'],  # Przykład pakietów używanych w trybie dewelopera
    },
)