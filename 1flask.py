from flask import Flask, url_for

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
                    <h2><img src= "{url_for('static', filename='img/mars.png')}" alt="Здесь был марс"></h2>
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
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <h1>Жди нас Марс!</h1>
                        <img src= "{url_for('static', filename='img/mars.png')}" alt="Здесь был марс">
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


@app.route('/')
def peizaahi_marsa():
    prof = ''
    img_adress = 'static/img/sci.png'
    if 'инженер' in prof.lower():
        img_adress = 'static/img/ing.png'
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <title></title>
                          </head>
                          <body>
                            <h1 align='center'>Миссия колонизация Марса</h1>
                            <p>И на Марсе будут яблони цвести</p>
                            <img src={img_adress} alt='Некорректно введена специальность'>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='')
