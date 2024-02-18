from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivymd.app import MDApp
import math

# Объединение файлов проекта
from kivy.lang import Builder
Builder.load_string('''

#:import get_color_from_hex kivy.utils.get_color_from_hex

<Container>:
    rows: 7
    padding: '5sp'
    spacing: '5sp'
    label_data: label_data

    AnchorLayout:
        anchor_y: 'top'
        size_hint: 1, 0.28
        padding: 10

        MDLabel:
            text: '0'
            id: label_data
            font_size: self.width/10
            halign: 'right'
            valign: 'center'
            theme_text_color: "Custom"
            text_color: get_color_from_hex("#07006e")
            bold: True

    GridLayout:
        cols: 2
        size_hint: 1, 0.12
        # padding: [0, 0, 0, 0]

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1
            spacing: '5sp'

            MDRectangleFlatButton:
                text: "C"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: label_data.text = str(0)

            MDRectangleFlatButton:
                text: "<<"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check("bs")

    GridLayout:
        cols: 4
        size_hint: 1, 0.12

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: '5sp'

            MDRectangleFlatButton:
                text: "1/X"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "X**2"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "Sqrt"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: '/'
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

    GridLayout:
        cols: 4
        size_hint: 1, 0.12

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: '5sp'

            MDRectangleFlatButton:
                text: "7"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "8"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "9"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "*"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

    GridLayout:
        cols: 4
        size_hint: 1, 0.12

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: '5sp'

            MDRectangleFlatButton:
                text: "4"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "5"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "6"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "-"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

    GridLayout:
        cols: 4
        size_hint: 1, 0.12

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: '5sp'

            MDRectangleFlatButton:
                text: "1"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "2"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "3"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "+"
                md_bg_color: get_color_from_hex("#daecff")
                size_hint: 1, 1
                on_press: root.check(self.text)

    GridLayout:
        cols: 4
        size_hint: 1, 0.12

        MDBoxLayout:
            spacing: '5sp'
            orientation: 'horizontal'

            MDRectangleFlatButton:
                text: "+/-"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "0"
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRectangleFlatButton:
                text: "."
                size_hint: 1, 1
                on_press: root.check(self.text)

            MDRaisedButton:
                text: '='
                size_hint: 1, 1
                on_release:
                    root.calc()

''')

# Размер окна
Window.size = (320, 470)
Window.minimum_height = 470
Window.minimum_width = 320


class Container(GridLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(
            self.keyboard_closed, self, 'text'
        )
        self.keyboard.bind(on_key_down=self.on_keyboard_down)

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard = None

    def on_keyboard_down(self, keyboard, key, text, modifiers):
        if key == 'backspace':
            self.check('bs')
        elif text and (text.isdigit() or text in ['+', '-', '*', '/', '.', 'enter']):
            self.check(text)
        elif key == 'escape':
            self.label_data.text = "0"
            return True  # Подтверждаем, что событие было обработано

    def check(self, el):
        text = str(self.label_data.text)

        # Обрабатываем нажатые кнопки
        if el == "bs":
            if len(text) == 1:
                self.label_data.text = "0"
            else:
                self.label_data.text = text[:-1]

        elif el == "+/-":
            # Проверка наличия операторов в строке
            operators = {'+', '-', '*', '/'}
            has_operators = any(op in text for op in operators)

            # Проверка наличия символа "-" в начале строки
            has_minus_at_start = text.startswith('-')

            if not has_operators:
                # Если в строке нет операторов, устанавливаем "-" в начало строки
                self.label_data.text = "-" + text
            elif not any(op in text for op in ['+', '*', '/']) and has_minus_at_start:
                # Если в строке только "-" и он стоит в начале строки, убираем его
                self.label_data.text = text[1:]
            else:
                # Иначе находим последний оператор в строке и выполняем замену
                index = len(text) - 1
                while index >= 0 and text[index] not in operators:
                    index -= 1

                if index >= 0:
                    # Найден оператор, выполняем замену
                    operator = text[index]
                    if operator == '-':
                        self.label_data.text = text[:index] + '+' + text[index + 1:]
                    elif operator == '+':
                        self.label_data.text = text[:index] + '-' + text[index + 1:]
                    elif operator == '*':
                        self.label_data.text = text[:index] + '*-' + text[index + 1:]
                    elif operator == '/':
                        self.label_data.text = text[:index] + '/-' + text[index + 1:]
                else:
                    # Нет операторов, добавляем "-"
                    self.label_data.text = "-" + text

        elif el == ".":
            if (text.split("+")[-1].find('.') < 0 or text.split("-")[-1].find('.') < 0 or
                    text.split("*")[-1].find('.') < 0 or text.split("/")[-1].find('.') < 0):
                self.label_data.text += "."

        elif el == "1/X":
            if text != "0" and (not any(op in text for op in ['-', '+', '/', '*']) or (
                    text.startswith('-') and text.count('-') == 1)):
                try:
                    result = 1 / float(text)
                    result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 6)
                    self.label_data.text = str(result)
                except ZeroDivisionError:
                    self.label_data.text = self.label_data.text

        elif el == "X**2":
            if text != "0" and (not any(op in text for op in ['-', '+', '/', '*']) or (
                    text.startswith('-') and text.count('-') == 1)):
                result = float(text) ** 2
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 6)
                self.label_data.text = str(result)

        elif el == "Sqrt":
            if not any(op in text for op in ['-', '+', '/', '*']):
                result = math.sqrt(float(text))
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 6)
                self.label_data.text = str(result)

        elif el == "+" or el == "-" or el == "*" or el == "/":
            if text[-1] != "+" and text[-1] != "-" and text[-1] != "*" and text[-1] != "/":
                self.label_data.text += el
            else:
                self.label_data.text = text[:-1] + el

        elif self.label_data.text == "0" or self.label_data.text == "-0":
            self.label_data.text = el

        elif text[-1] != "0":
            self.label_data.text += el

        elif text.endswith("0") and text[-2] in ["*", "/", "+", "-"]:
            self.label_data.text += "." + el

        else:
            self.label_data.text += el

    def calc(self):
        expression = self.label_data.text
        if expression and expression[-1] not in ['+', '-', '*', '/']:
            try:
                result = eval(expression)
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 6)
            except ZeroDivisionError:
                result = expression
        else:
            result = expression
        self.label_data.text = str(result)


class CalcApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Калькулятор"
        self.icon = 'icon.png'
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.container = Container()
        Window.bind(on_keyboard=self.on_keyboard)  # Привязываем обработчик нажатия клавиш
        return self.container

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Код клавиши Esc
            self.container.label_data.text = "0"  # Сбрасываем значение на экране
            return True  # Подтверждаем, что событие было обработано
        elif key == 13 or key == 61:  # Код клавиши Enter или "="
            self.calculate_result()
            return True
        elif key == 8:  # Код клавиши Backspace
            self.handle_backspace()
            return True
        return False  # Позволяем другим обработчикам обработать событие

    def calculate_result(self):
        expression = self.container.label_data.text
        if expression and expression[-1] not in ['+', '-', '*', '/']:
            try:
                result = eval(expression)
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 6)
            except ZeroDivisionError:
                result = expression
        else:
            result = expression
        self.container.label_data.text = str(result)

    def handle_backspace(self):
        text = self.container.label_data.text
        if len(text) == 1:
            self.container.label_data.text = "0"
        else:
            self.container.label_data.text = text[:-1]


if __name__ == "__main__":
    CalcApp().run()
