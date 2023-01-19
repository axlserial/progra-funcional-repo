from functools import reduce
import json


def read_stopwords(file_name: str) -> list[str]:
    with open(file_name, errors="ignore") as file:
        return list(map(lambda line: line.replace('\n', ''), file.readlines()))


def count_words(file_name: str, stopwords: list[str]) -> float:
    with open(file_name) as file:
        # obtenemos las palabras de cada registro (lista de listas de palabras)
        words = map(
            lambda record: filter(
                lambda word: word not in stopwords,
                json.loads(record)["short_description"].split()), file)

        # obtenemos la cantidad de palabras de cada registro (lista de enteros)
        words_count = map(lambda r_words: [len(w) for w in r_words], words)

        # sumamos la cantidad de palabras de cada registro
        # y obtenemos la longitud total de palabras

        initial_data = (0, 0)  # (total_len_words, total_words)

        data = reduce(
            lambda counters, data_words:
            (counters[0] + sum(data_words), counters[1] + len(data_words)),
            words_count, initial_data)

        return data[0] / data[1]


def main():
    file_news = "News_Category_Dataset_v3.json"
    file_stopwords = "stopwords-en.txt"

    # read stopwords
    stopwords = read_stopwords(file_stopwords)

    # count words
    words_mean = count_words(file_news, stopwords)
    print(
        f'La longitud promedio en caracteres de las palabras es: {words_mean}')


if __name__ == "__main__":
    main()