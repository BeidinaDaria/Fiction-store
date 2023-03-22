from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import base64
import os


#   MODEL OF ITEMS TABLE
Base = declarative_base()
class Items(Base):
    __tablename__ = "items"
    id          = Column(Integer, primary_key=True)
    title       = Column(String(100), nullable=False)
    price       = Column(Float, nullable=False)
    description = Column(String(1000), nullable=False)
    images      = Column(JSON)
    color       = Column(JSON)
    sciense     = Column(String(50))
    production  = Column(String(100))
    comments    = Column(JSON)


#   FILLING ITEMS TABLE ROWS
def fillItems():
    # 1 row
    images = { }
    images['1'] = base64.encodebytes(open(os.getcwd()+"/Images/test1.png", mode="rb").read()).decode("utf-8")
    images['2'] = base64.encodebytes(open(os.getcwd()+"/Images/test2.png", mode="rb").read()).decode("utf-8")
    comments = { }
    comments['1'] = {
        "name": "Vasya",
        "date": "12.07.2022",
        "score": "5",
        "text": "Вполне ничё такое устройство да"
    }
    comments['2'] = {
        "name": "Dima",
        "date": "18.07.2022",
        "score": "4",
        "text": "Ну не знаю не знаю..."
    }
    item_1 = Items(
        title = "Portal",
        price = 100.0,
        description = "структура, позволяющая игроку попадать в другие измерения. Благодаря такому прибору и вы могли бы повстречать другие версии себя, узнать, как на вашу жизнь и на жизнь вашего ребенка повлиял тот или иной ваш выбор, и увидеть, что бы произошло, если бы вы поступили иначе.",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Portal%20(1).png", mode="rb").read()).decode("utf-8"),
        color       = {'1': "silver"}
        sciense = "Физика",
        production  = "Unknown"
    )

    # 2 row
    images['1'] = base64.encodebytes(open(os.getcwd()+"/Images/test3.png", mode="rb").read()).decode("utf-8")
    comments = { }
    comments['1'] = {
        "name": "Misha",
        "date": "07.12.2020",
        "score": "3",
        "text": "Я упал в межпортальное измерение и вишу здесь уже второй год чёртова гладос"
    }
    item_2 = Items(
        title = "Neuralyzer",
        price = 100.0,
        description = "специальное устройство, созданное с помощью инопланетных технологий и используемое агентами ЛВЧ в целях конспирации. Устройство выдает сильную вспышку, воздействующую на мозг и 'стирающую' память.",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Neuralyzer%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
        color = { '1': "silver" },
        sciense = "Физика",
        production = "Люди в чёрном",
    )
    item_3 = Items(
        title = "Multifunctional boots",
        price = 100.0,
        description = "обычные ботинки — прошлый век! Обувь четыре-в-одном — вот что выбирает новое поколение. Легким движением руки кроссовки превращаются в ролики, коньки или технологичные пружинящие ботинки. С помощью специальных креплений можно поменять вид подошвы за считанные минуты, чтобы веселиться, не теряя времени на переодевание.",
        science = "Инженерия",
        images =base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Multifunctional%20boots%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
        production = "Unknown"

    )
    item_4 = Items(
        title = "Health monitoring rings",
        price = 100.0,
        description = "Ученые обнаружили, что микрофлора кишечника — по сути, второй мозг человека.Кольца состояния микрофлоры содержат точную копию микрофлоры кишечника своего владельца. Каждый раз, когда вы находитесь в среде, которая негативно влияет на микрофлору, кольцо меняет цвет, намекая, что вам лучше уйти или хотя бы помыть руки.",
        science = "Биоинженерия",
        production = "Unknown",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Health%20monitoring%20rings%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
    )
    item_5 = Items(
        title = "Flying car",
        price = 100.0,
        descriprion = "транспортное средство, сочетающее в себе свойства автомобиля и летательного аппарата. Причём, соотношение этих свойств у различных моделей может быть различным.",
        production = "Unknown",
        science = "Физика",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Flying%20car%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
    )
    item_6 = Items(
        title = "Clone robot",
        price = 100.0,
        description = "если вы не успеваете реализовать свои грандиозные планы, вам поможет ваша роботизированная копия. Вы точно сможете придумать немало дел для таких помощников.",
        production = "Финес и Ферб",
        science = "Роботостроение",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/%D0%A1lone%20robot%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
    )
    item_7 = Items(
        title = "Water of eternal life",
        price = 100.0,
        description = "Ученые предполагают, что, возможно, на свет уже появился первый человек, который сможет жить вечно. Волшебная вода даст каждому шанс стать бессмертным. Чтобы не допустить проблему перенаселенности планеты, в воде содержится особый ингредиент, который навсегда стерилизует того, кто ее выпьет.",
        production = "Unknown",
        science = "Биотехнология",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Water%20of%20eternal%20life%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),

    )
    item_8 = Items(
        title = "Umbrella filter",
        price = 100.0,
        description = "изобретение, которое спасет вас от жажды во время дождя. Стоит только нажать на специальную кнопку, и в зонтике откроется карман для сбора дождевой воды. По трубочке жидкость попадет прямо в стакан, предварительно пройдя фильтрацию.",
        production = "Unknown",
        science = "Инженерия",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Umbrella%20filter%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
    )
    item_9 = Items(
        title = "Thought-reading implants",
        price = 100.0,
        description = "специальные импланты, которые позволят им читать мысли друг друга. Больше не придется спрашивать, как настроение у вашей жены или мужа — вы будете просто о нем знать.",
        production = "Unknown",
        science = "Физика, Биотехнология",
        images = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Thought-reading%20implants%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
    )
    item_10 = Items(
        title       = "Tardis",
        price       = 77.0,
        description = "Путешествуйте с комфортом во времени и пространтстве. Благодаря TARDIS это сделать будет еще проще. Известная машина времени и космический корабль из фантастического сериала 'Доктор Кто' теперь и в нашем магазине. Выращена на планете повелителей времени Галифрей по всем строгостям временных законов. Снаружи выглядит как обычная синяя полицейская будка, но внутри она гораздо больше, чем снаружи. Сколько там места на самом деле, никто не знает, но поговаривают, что ТАРДИС бесконечна. Внутри можно обнаружить: библиотеку, бассейн, медицинский отсек, несколько складов с кирпичными стенами, многоуровневую гардеробную комнату, спальные помещения для Доктора и компаньонов. Основные функции: /n Перемещение в пространстве и времени; /n Телепатические функции; /n Компьютерные функции; /n Способность переводить все существующие языки, кроме древнегаллифрейского; /n Защита от внешних врагов при закрытых дверях; /n При материализации в вакууме ТАРДИС создаёт вокруг себя поле, удерживающее атмосферу /n Осадный режим при внешней опасности.",
        images      = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/Thought-reading%20implants%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
        color       = { '1': "blue" },
        sciense     = "Физика",
        production  = "Доктор Кто",
    )
    item_11 = Items(
        title       = "A device to combat improper eating",
        price       = 100.0,
        description = "Гаджет показывает биометрические данные о человеке с помощью дополненной реальности. Стоит вам только потянуться к шоколадке, как устройство заметит начавшееся слюноотделение и усиленное сердцебиение, и тут же отправит вам предупреждение. Помимо этого, он отслеживает и легкие наркотики, например, может рассказать, что с вами случится от одной затяжки.",
        images      = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/A%20device%20to%20combat%20improper%20eating%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
        color       = {'1': "white"},
        sciense     = "Биоинженерия",
        production  = "Unknown"

    )
    item_12 = Items(
        title       = "A device that changes people's behavior",
        price       = 100.0,
        description = "прибор, заставляющий людей вести себя не так, как обычно. Благодаря воздействию этого устройства ребенок точно бы не стал выпрашивать новые игрушки в магазине или отказываться убирать в своей комнате.",
        images      = base64.encodebytes(open(os.getcwd()+"https://github.com/BeidinaDaria/Fiction-store/blob/main/templates/styles/img/A%20device%20that%20changes%20people's%20behavior%20(1).png?raw=true", mode="rb").read()).decode("utf-8"),
        color       = {'1': "white"},
        sciense     = "Психология",
        production  = "Финес и Ферб"
    )

    # add rows to database
    session.add(item_1)
    session.add(item_2)
    session.add(item_3)
    session.add(item_4)
    session.add(item_5)
    session.add(item_6)
    session.add(item_7)
    session.add(item_8)
    session.add(item_9)
    session.add(item_10)
    session.add(item_11)
    session.add(item_12)
    session.commit()


#   DELETING ALL ROWS FROM ITEMS TABLE
def deleteAllItems():
    session.query(Items).delete()
    session.commit()


#   ENTRY POINT
if __name__ == "__main__":
    # create sqlite database
    engine = create_engine("sqlite:///fiction_store.db")  
    Base.metadata.create_all(engine)

    # create session
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # fill the rows
    fillItems()
    # delete all rows
    # deleteAllItems()

    # print items ID
    print("items ID:", ", ".join(str(item.id) for item in session.query(Items).all()))