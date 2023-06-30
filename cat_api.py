from flask import Flask, jsonify

app = Flask(__name__)

gatos = {
    "Dante": {
        "nome": "Dante",
        "raça": "Siamês",
        "imagem": "https://i.pinimg.com/564x/b3/61/e2/b361e2e19880e62f7cb7fd5170181836.jpg"
    },
    "Zeze": {
        "nome": "Zeze",
        "raça": "Persa",
        "imagem": "https://i.pinimg.com/564x/cf/17/36/cf17361f248c43aca7eb466a851f31d3.jpg"
    },
    "Star": {
        "nome": "Star",
        "raça": "Maine Coon",
        "imagem": "https://i.pinimg.com/564x/ee/15/cb/ee15cb91ee9a09bfd3e711352e3703a4.jpg"
    }
}


@app.route('/gatos/<nome>', methods=['GET'])
def obter_detalhes_gato(nome):
    try:
        gato = gatos[nome]
        return jsonify(gato)
    except KeyError:
        return jsonify(({"erro": "Gato não encontrado."}), 404)
    except Exception as e:
        return jsonify(({"erro": str(e)}), 500)


if __name__ == '__main__':
    app.run()
