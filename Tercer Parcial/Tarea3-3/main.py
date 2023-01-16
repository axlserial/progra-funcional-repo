from functools import reduce
import json


def read_stopwords(file_name: str) -> list[str]:
    with open(file_name, errors="ignore") as file:
        return list(map(lambda line: line.replace('\n', ''), file.readlines()))


def count_words(counters: tuple[int, int], words: map[int]) -> tuple[int, int]:
    words_list = list(words)
    return (counters[0] + sum(words_list), counters[1] + len(words_list))


def count_words(file_name: str, stopwords: list[str]):
    with open(file_name) as file:
        initial_data = (0, 0)  # (total_words, total_len_words)

        # data = reduce(
        #     lambda counters, data_words:
        #     (counters[0] + data_words[0], counters[1] + data_words[1]),
        #     reduce(
        #         lambda words_counter, word:
        #         (words_counter[0] + 1, words_counter[1] + len(word)),
        #         filter(
        #             lambda word: word not in stopwords,
        #             map(
        #                 lambda record: json.loads(record)["short_description"].
        #                 split(), file)), (0, 0)), initial_data)

        # data = reduce(
        #     lambda words_counter, words:
        #     (words_counter[0] + 1, words_counter[1] + len(words)),
        #     map(
        #         lambda record: filter(
        #             lambda word: word not in stopwords,
        #             json.loads(record)["short_description"].split()),
        #         file), (0, 0))

        # print(data)

        # obtenemos las palabras de cada registro (lista de listas de palabras)
        words = map(
            lambda record: filter(
                lambda word: word not in stopwords,
                json.loads(record)["short_description"].split()), file)

        # obtenemos la cantidad de palabras de cada registro (lista de enteros)
        words_count = map(lambda r_words: map(len, r_words), words)

        # print([len(list(w)) for w in words_count][:10])

        # sumamos la cantidad de palabras de cada registro y obtenemos la longitud total de palabras
        # data = reduce(
        #     lambda counters, data_words: (counters[0] + sum(
        #         data_words), counters[1] + len(list(data_words))), words_count,
        #     (0, 0))

        data = reduce(count_words, words_count, (0, 0))

        print(data)

        # return data[1] / data[0]
        return 1


def main():
    file_news = "News_Category_Dataset_v3.json"
    file_stopwords = "stopwords-en.txt"

    # read stopwords
    stopwords = read_stopwords(file_stopwords)

    # count words
    words_mean = count_words(file_news, stopwords)
    print(words_mean)


if __name__ == "__main__":
    main()