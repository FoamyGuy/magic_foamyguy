from flask import Flask, request, render_template, redirect
from cards import card_dict
# set the project root directory as the static folder, you can set others.

app = Flask(__name__, static_url_path='')
app._static_folder = "static/"


@app.route('/')
def root():
    f = open("card.txt", 'r')
    cur_card = f.read()
    f.close()
    return render_template('index.html', card=card_dict[cur_card])


@app.route('/set', methods=['GET'])
def set_card():
    ranks = ['2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'j',
             'q', 'k', 'a']
    return render_template('set_card.html', ranks=ranks)


@app.route('/save', methods=['GET'])
def save_card():
    suits = ['h', 'd', 'c', 's']
    ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

    bin = request.args.get("bin")
    if bin:
        suit_val = bin[:2]
        rank_val = bin[2:]

        suit = suits[int(suit_val, 2)]
        rank = ranks[int(rank_val, 2)]

        f = open('card.txt', 'w')
        f.write("%s%s" % (rank, suit))
        f.close()



    else:

        f = open('card.txt', 'w')
        f.write("%s%s" % (rank, suit))
        f.close()


    return redirect('/set')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)
