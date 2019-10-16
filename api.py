import requests


def api():

    resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9')
    resp.json()['squares'][0]

    lista = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]

    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista
