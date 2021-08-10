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
# До даної функції напишіть декоратор який загорне отриману строку в div блок. style_class - це аргумент який приймається
# декоратором, тобто декоратор або в 3 рівні, або функтор (краще зробіть через функтор)
#
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>


from functools import wraps


def decor(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        pass
    return wrap


@decor
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>"
    template = "<p> {} </p>"