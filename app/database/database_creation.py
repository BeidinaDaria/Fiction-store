from app.models import Items
from app import app, db

import os


#   filling all rows
def fill_db():
    comments = {
        '1': {
        "name": "Misha",
        "date": "07.12.2020",
        "score": "3",
        "text": "Я упал в межпортальное измерение и вишу здесь уже второй год чёртова гладос"
        }
    }
    item_2 = Items(
        title = "Neuralyzer",
        price = 100.0,
        description = "специальное устройство, созданное с помощью инопланетных технологий и используемое агентами ЛВЧ в целях конспирации. Устройство выдает сильную вспышку, воздействующую на мозг и 'стирающую' память.",
        images = { 1: open(os.getcwd() + "/app/static/img/Neuralyzer (1).png", mode="rb").read().__str__() },
        color = { '1': "silver" },
        science = "Физика",
        comments=comments
    )
    item_3 = Items(
        title = "Multifunctional boots",
        price = 100.0,
        description = "обычные ботинки — прошлый век! Обувь четыре-в-одном — вот что выбирает новое поколение. Легким движением руки кроссовки превращаются в ролики, коньки или технологичные пружинящие ботинки. С помощью специальных креплений можно поменять вид подошвы за считанные минуты, чтобы веселиться, не теряя времени на переодевание.",
        science = "Инженерия",
        images = { 1: open(os.getcwd() + "/app/static/img/Multifunctional boots (1).png", mode="rb").read().__str__() }
    )
    item_4 = Items(
        title = "Health monitoring rings",
        price = 100.0,
        description = "Ученые обнаружили, что микрофлора кишечника — по сути, второй мозг человека.Кольца состояния микрофлоры содержат точную копию микрофлоры кишечника своего владельца. Каждый раз, когда вы находитесь в среде, которая негативно влияет на микрофлору, кольцо меняет цвет, намекая, что вам лучше уйти или хотя бы помыть руки.",
        science = "Биоинженерия",
        images = { 1: open(os.getcwd() + "/app/static/img/Health monitoring rings (1).png", mode="rb").read().__str__() }
    )
    item_5 = Items(
        title = "Flying car",
        price = 100.0,
        description = "транспортное средство, сочетающее в себе свойства автомобиля и летательного аппарата. Причём, соотношение этих свойств у различных моделей может быть различным.",
        science = "Физика",
        images = { 1: open(os.getcwd() + "/app/static/img/Flying car (1).png", mode="rb").read().__str__() }
    )
    item_6 = Items(
        title = "Clone robot",
        price = 100.0,
        description = "если вы не успеваете реализовать свои грандиозные планы, вам поможет ваша роботизированная копия. Вы точно сможете придумать немало дел для таких помощников.",
        science = "Роботостроение",
        images = { 1: open(os.getcwd() + "/app/static/img/Clone robot (1).png", mode="rb").read().__str__() },
    )
    item_7 = Items(
        title = "Water of eternal life",
        price = 100.0,
        description = "Ученые предполагают, что, возможно, на свет уже появился первый человек, который сможет жить вечно. Волшебная вода даст каждому шанс стать бессмертным. Чтобы не допустить проблему перенаселенности планеты, в воде содержится особый ингредиент, который навсегда стерилизует того, кто ее выпьет.",
        science = "Биотехнология",
        images = { 1: open(os.getcwd() + "/app/static/img/Water of eternal life (1).png", mode="rb").read().__str__() },

    )
    item_8 = Items(
        title = "Umbrella filter",
        price = 100.0,
        description = "изобретение, которое спасет вас от жажды во время дождя. Стоит только нажать на специальную кнопку, и в зонтике откроется карман для сбора дождевой воды. По трубочке жидкость попадет прямо в стакан, предварительно пройдя фильтрацию.",
        science = "Инженерия",
        images = { 1: open(os.getcwd() + "/app/static/img/Umbrella filter (1).png", mode="rb").read().__str__() },
    )
    item_9 = Items(
        title = "Thought-reading implants",
        price = 100.0,
        description = "специальные импланты, которые позволят им читать мысли друг друга. Больше не придется спрашивать, как настроение у вашей жены или мужа — вы будете просто о нем знать.",
        science = "Физика, Биотехнология",
        images = { 1: open(os.getcwd() + "/app/static/img/Thought-reading implants (1).png", mode="rb").read().__str__() },
    )
    item_10 = Items(
        title       = "Tardis",
        price       = 77.0,
        description = "Путешествуйте с комфортом во времени и пространтстве. Благодаря TARDIS это сделать будет еще проще. Известная машина времени и космический корабль из фантастического сериала 'Доктор Кто' теперь и в нашем магазине. Выращена на планете повелителей времени Галифрей по всем строгостям временных законов. Снаружи выглядит как обычная синяя полицейская будка, но внутри она гораздо больше, чем снаружи. Сколько там места на самом деле, никто не знает, но поговаривают, что ТАРДИС бесконечна. Внутри можно обнаружить: библиотеку, бассейн, медицинский отсек, несколько складов с кирпичными стенами, многоуровневую гардеробную комнату, спальные помещения для Доктора и компаньонов. Основные функции: /n Перемещение в пространстве и времени; /n Телепатические функции; /n Компьютерные функции; /n Способность переводить все существующие языки, кроме древнегаллифрейского; /n Защита от внешних врагов при закрытых дверях; /n При материализации в вакууме ТАРДИС создаёт вокруг себя поле, удерживающее атмосферу /n Осадный режим при внешней опасности.",
        images      = { 1: open(os.getcwd() + "/app/static/img/1.jpg", mode="rb").read().__str__() },
        color       = { '1': "blue" },
        science     = "Физика"
    )
    item_11 = Items(
        title       = "A device to combat improper eating",
        price       = 100.0,
        description = "Гаджет показывает биометрические данные о человеке с помощью дополненной реальности. Стоит вам только потянуться к шоколадке, как устройство заметит начавшееся слюноотделение и усиленное сердцебиение, и тут же отправит вам предупреждение. Помимо этого, он отслеживает и легкие наркотики, например, может рассказать, что с вами случится от одной затяжки.",
        images      = { 1: open(os.getcwd() + "/app/static/img/A device to combat improper eating (1).png", mode="rb").read().__str__() },
        color       = {'1': "white"},
        science     = "Биоинженерия"
    )
    item_12 = Items(
        title       = "A device that changes people's behavior",
        price       = 100.0,
        description = "прибор, заставляющий людей вести себя не так, как обычно. Благодаря воздействию этого устройства ребенок точно бы не стал выпрашивать новые игрушки в магазине или отказываться убирать в своей комнате.",
        images      = { 1: open(os.getcwd() + "/app/static/img/A device that changes people's behavior (1).png", mode="rb").read().__str__() },
        color       = {'1': "white"},
        science     = "Психология"
    )

    # add rows to database
    with app.app_context():
        db.session.add(item_2)
        db.session.add(item_3)
        db.session.add(item_4)
        db.session.add(item_5)
        db.session.add(item_6)
        db.session.add(item_7)
        db.session.add(item_8)
        db.session.add(item_9)
        db.session.add(item_10)
        db.session.add(item_11)
        db.session.add(item_12)
        db.session.commit()


#   deleting all rows
def clear_db():
    with app.app_context():
        db.session.query(Items).delete()
        db.session.commit()

def create_db():
    with app.app_context():
        db.create_all()