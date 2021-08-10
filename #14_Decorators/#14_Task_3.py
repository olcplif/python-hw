# 3. def get_names_page(names_list):
#         template_head = "<h3> User names: </h3>"
#         template = "<p> {} </p>"
#
# Допишіть дану функцію так, щоб коли на вхід приходить names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
# функція повертала таку строку
#
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
#
# До даної функції напишіть декоратор який загорне отриману строку в div блок.
# style_class - це аргумент який приймається
# декоратором, тобто декоратор або в 3 рівні, або функтор (краще зробіть через функтор)
#
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>

class MakeDivTag:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(*args):
            result = f"<div class = {self.style_class}>" + "\n" + func(*args) + "<div>"
            return result

        return wrap


@MakeDivTag('*style_class*')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>"
    template = ""
    for name in names_list:
        template = template + f"<p> {name} </p>" + "\n"
    return template_head + "\n" + template


print(get_names_page(["Misha", "Olya", "Vitaliy", "Vita"]))
