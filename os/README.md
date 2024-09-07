# Opis skryptu

Ten skrypt dostarcza funkcje do uzyskiwania informacji o sieci, generowania tekstu w kolorach tęczy oraz wyszukiwania największej liczby w podanym ciągu tekstowym. Poniżej znajduje się opis każdej z funkcji.

## Funkcje

### 1. `network_info()`

Funkcja `network_info` służy do uzyskania szczegółowych informacji o sieci. Zbiera ona dane dotyczące:
- **Nazwa hosta (Hostname)**: Zwraca nazwę hosta urządzenia.
- **Lokalny adres IP (Local IP)**: Zwraca lokalny adres IP przypisany do hosta.
- **Interfejsy sieciowe (Network Interfaces)**: Zwraca listę interfejsów sieciowych z przypisanymi adresami IP (IPv4 oraz IPv6).
- **Statystyki sieci (Network Stats)**: Zwraca statystyki dotyczące sieci, takie jak liczba bajtów wysłanych i odebranych na każdym interfejsie sieciowym.

#### Przykład użycia:
```python
info = network_info()
print(info)
```
``sekretne funkcje tez sa``