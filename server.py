from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This key is the blue pill"

@app.route('/')
def survey_page():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_survey():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['best_ta'] = request.form['best_ta']
    selected_skills = request.form.getlist('skills')
    if 'Python' in selected_skills:
        session['python'] = 'Python'
    else:
        session['python'] = ''

    if 'Flask' in selected_skills:
        session['flask'] = 'Flask'
    else:
        session['flask'] = ''

    if 'MySQL' in selected_skills:
        session['mysql'] = 'MySQL'
    else:
        session['mysql'] = ''
    return redirect('/result')


@app.route('/result')
def display_info():
    return render_template('result.html', name = session['name'], dojo_location = session['dojo_location'], language = session['language'], comments = session['comments'], best_ta = session['best_ta'], python = session['python'], flask = session['flask'], mysql = session['mysql'] )

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)