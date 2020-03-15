from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/start')
def first():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def second():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def third():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <h2><img src= "{url_for('static', filename='static/img/mars.png')}" alt="Здесь был марс"></h2>
                    <div>Вот она какая, красная планета.</div>
                  </body>
                </html>"""


@app.route('/promotion_image')
def color():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='static/css/style.css')}" />
                        <h1>Жди нас Марс!</h1>
                        <img src= "{url_for('static', filename='static/img/mars.png')}" alt="Здесь был марс">
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-primary" role="alert">
                            Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-primary" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-primary" role="alert">
                            И начнем с Марса!
                            </div>
                            <div class="alert alert-primary" role="alert">
                            Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def varianty_vibora(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                          <body>
                            <h1><font color="#ffcc00">Моё предложение: <font color="#0000ff"><i>{planet_name}</i></h1>
                            <h4><font color="#000000" align='left'>Эта планета близка к Земле;</h4>
                            <h4 class="alert alert-success" role="alert">На ней много необходимых ресурсов;</h4>
                            <h4 class="alert alert-info" role="alert">На ней есть вода и атмосфера;</h4>
                            <h4 class="alert alert-warning" role="alert">На ней есть небольшое магнитное поле;</h4>
                            <h4 class="alert alert-danger" role="alert">Наконец, она просто красива!</h4>
                          </body>
                        </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result_of_otbor(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h3>Претендент на участие в миссии {nickname}</h3>
                            <h4 class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора составляет</h4>
                            <h4>составляет {rating}!</h4>
                            <h4 class="alert alert-warning" role="alert">Желаем удачи!</h4>
                          </body>
                        </html>'''


@app.route('/static')
def peizaahi_marsa():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <title>Пейзажи Марса</title>
                          </head>
                          <body>
                            <h1 align='center'>Пейзажи Марса</h1>
                            <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                                <div class="carousel-inner">
                                    <div align='center' class="carousel-item active">
                                    <img class="d-block w-50" src="static/img/1.jpg" alt="First slide">
                                    </div>
                                    <div align='center' class="carousel-item">
                                    <img class="d-block w-50" src="static/img/2.jpg" alt="Second slide">
                                    </div>
                                    <div align='center' class="carousel-item">
                                    <img class="d-block w-50" src="static/img/3.jpg" alt="Third slide">
                                    </div>
                                    <div align='center' class="carousel-item">
                                    <img class="d-block w-50" src="static/img/4.jpg" alt="Third slide">
                                    </div>
                                </div>
                            </div>
                          </body>
                        </html>'''


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align='center'>Анкета претендента</h1>
                            <h3 align='center'>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label></label>
                                    <div class="form-group">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Бакалавр Данковский</option>
                                          <option>Ойнон</option>
                                        </select>
                                     </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="1" value="1" checked>
                                          <label class="form-check-label" for="1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="2" value="2">
                                          <label class="form-check-label" for="2">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="3" value="3">
                                          <label class="form-check-label" for="3">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="4" value="4">
                                          <label class="form-check-label" for="4">
                                            Экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="5" value="5">
                                          <label class="form-check-label" for="5">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="6" value="6">
                                          <label class="form-check-label" for="6">
                                            Инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="7" value="7">
                                          <label class="form-check-label" for="7">
                                            Астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="8" value="8">
                                          <label class="form-check-label" for="8">
                                             Специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="9" value="9">
                                          <label class="form-check-label" for="9">
                                             Гляциолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="10" value="10">
                                          <label class="form-check-label" for="10">
                                              Инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="11" value="11">
                                          <label class="form-check-label" for="11">
                                             Оператор марсохода
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="12" value="12">
                                          <label class="form-check-label" for="12">
                                             Киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="13" value="13">
                                          <label class="form-check-label" for="13">
                                             Штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="14" value="14">
                                          <label class="form-check-label" for="14">
                                             Пилот дронов
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="14" value="14">
                                          <label class="form-check-label" for="14">
                                             Да, я просто обязан был написать какую-то странную профессию в список :D
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужчина
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female" checked>
                                          <label class="form-check-label" for="female">
                                            Женщина
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="attacking_helicopter" value="attacking_helicopter" checked>
                                          <label class="form-check-label" for="attacking_helicopter">
                                            Attacking helicopter
                                          </label>
                                        </div>
                                    </div>
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print('Профессия №:', request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        if request.form.get('accept'):
            print('Останусь!')
        else:
            print('Не останусь! :(')
        return "Форма отправлена"

@app.route('/training/<prof>')
def trenirovki_v_polyote(prof):
    return render_template('first.html', prof=prof)

@app.route('/list_prof/<list>')
def spisok_professiy(list):
    return render_template('second.html', type=list)


if __name__ == '__main__':
    app.run(port=8080, host='')
