# 4. Допишіть ще один декоратор, який загорне результат роботи з попереднього завдання в теги <body> </body>.
# Щоб отримати ось такий код
#
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
#
# ще один декоратор який приклеїть до існуючого куска html - head блок,
# де *title* це аргумент що отримується декоратором
#
# <head>
# <title>*title*</title>
# </head>
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
#
# Ще один декоратор який загорне все що є в <html> </html> теги
#
# <html>
# <head>
# <title>*title*</title>
# </head>
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
# </html>
#
# Зверніть увагу що у вас на одну функцію повинно назначатись 4 декоратори, тому потрібно не тільки їх написати, а й
# вибрати правильний порядок декорування щоб після всіх декорацій отримати наприклад ось такий html
# Також деякі декоратори доцільно буде робити через функції в "2 рівні", деякі в "3 рівні", деякі через функтори
#
# <html>
# <head>
# <title>Users</title>
# </head>
# <body>
# <div class=users_block>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
# </html>

class MakeDivTag:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(*args):
            opening_tag, closing_tag = f"<div class={self.style_class}>", "</div>"
            result = f"{opening_tag}\n{func(*args)}{closing_tag}"
            return result

        return wrap


class MakeBodyTag:

    def __call__(self, func):
        def wrap(*args):
            opening_tag, closing_tag = "<body>", "</body>"
            result = f"{opening_tag}\n{func(*args)}\n{closing_tag}"
            return result

        return wrap


class MakeHeadTag:
    def __init__(self, title):
        self.title = title

    def __call__(self, func):
        def wrap(*args):
            opening_tag, closing_tag = "<head>", "</head>"
            opening_tag_, closing_tag_ = "<title>", "</title>"
            result = f"{opening_tag}\n{opening_tag_}{self.title}{closing_tag_}\n{closing_tag}\n{func(*args)}"
            return result

        return wrap


class MakeHtmlTag:

    def __call__(self, func):
        def wrap(*args):
            opening_tag, closing_tag = "<html>", "</html>"
            result = f"{opening_tag}\n{func(*args)}\n{closing_tag}"
            return result

        return wrap


@MakeHtmlTag()
@MakeHeadTag('Users')
@MakeBodyTag()
@MakeDivTag('users_block')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>"
    template = ""
    for name in names_list:
        template = template + f"<p> {name} </p>" + "\n"
    return template_head + "\n" + template


page_user_name = get_names_page(["Misha", "Olya", "Vitaliy", "Vita"])
print(page_user_name)

with open("user_name.html", "w") as file:
    print(file.write(page_user_name))
