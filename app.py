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


@app.route('/save', methods=['POST'])
def save_card():
    suit=request.form['suit']
    rank=request.form['rank']
    f = open('card.txt', 'w')
    f.write("%s%s" % (rank, suit))
    f.close()
    return redirect('/set')




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")