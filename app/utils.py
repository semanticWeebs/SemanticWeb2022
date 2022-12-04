import pandas as pd
import itertools
import numpy as np


def conteins_sub_string(srting, sub_string):
    try:
        return srting.lower().find(sub_string.lower()) != -1
    except:
        return False


def subset(
    name_film="",
    year="",
    year_op="",
    lang="",
    actor="",
    produser="",
    country="",
    genre="",
    data="",
):
    if name_film != "":
        data = data[
            data["name_film"].apply(lambda x: conteins_sub_string(x, name_film))
        ]
    if year != "":
        if year_op == "=":
            data = data[data["data"] == int(year)]
        if year_op == ">":
            data = data[data["data"] > int(year)]
        if year_op == "<":
            data = data[data["data"] < int(year)]
    if lang != "":
        if len(lang[0]) < 3:
            data = data[
                data["langw"].apply(
                    lambda x: len([1 for l in lang if conteins_sub_string(x, l)]) > 0
                )
            ]
        else:
            data = data[
                data["long_lengw"].apply(
                    lambda x: len([1 for l in lang if conteins_sub_string(x, l)]) > 0
                )
            ]

    if actor != "":
        data = data[
            data["actor"].apply(
                lambda x: len([1 for l in actor if conteins_sub_string(x, l)]) > 0
            )
        ]

    if produser != "":
        data = data[
            data["produser"].apply(
                lambda x: len([1 for l in produser if conteins_sub_string(x, l)]) > 0
            )
        ]

    if country != "":
        data = data[
            data["country"].apply(
                lambda x: len([1 for l in country if conteins_sub_string(x, l)]) > 0
            )
        ]

    if genre != "":
        data = data[
            data["genre"].apply(
                lambda x: len([1 for l in genre if conteins_sub_string(x, l)]) > 0
            )
        ]

    return data


class selecter:
    def __init__(self) -> None:
        self.data_film = pd.read_csv("data_film_preprocesing_data_2.csv")


# data_film = pd.read_csv("data_film_preprocesing_data_1.csv")
# code = pd.read_csv("code.csv", sep="\t", index_col=False)


# data_film = pd.read_csv("data_film_preprocesing_data_2.csv")
# print(data_film)

# data = subset(
#     name_film="",
#     year="2000",
#     year_op=">",
#     lang="",
#     actor="",
#     produser="",
#     country=["france"],
#     data=data_film,
# )


# print(data["country"])
