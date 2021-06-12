# Наша "База данных"
# name (англ. "имя") - название мороженого
# description (англ. "описание") - описание мороженого
from django.db import models


class Icecream(models.Model):
    name = models.CharField(verbose_name="Название мороженого", max_length=100)
    description = models.TextField(verbose_name="Описание мороженого", max_length=200, blank=True)


    class Meta:
        verbose_name_plural = "Список Мороженого"

    def __str__(self):
        return self.name


class Friend(models.Model):
    friend_name = models.CharField(verbose_name="Имя друга", max_length=50)
    friend_city = models.CharField(verbose_name="Город проживания", max_length=100)
    friend_icecream = models.ForeignKey(Icecream, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name="Любимые сорта мороженого", related_name="friends")

    def __str__(self):
        return self.friend_name



    class Meta:
        verbose_name_plural = "Список Друзей"


icecream_db = [
    {
    'name': 'Золотое мороженое',
    'description': ('Шарики таитянского ванильного мороженого, шоколад '
                    '"Amedei Porcelana" и груда экзотических фруктов.'
                    'Всё это покрыто золотой фольгой, '
                    'её тоже полагается съесть.'),
    },
    {
    'name': 'Готическое мороженое',
    'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                    'true black goths. Состав: сливочное мороженое, '
                    'миндаль, активированный уголь, чернота, мрак, отрицание.'),
    },
    {
    'name': 'Мороженое паста карбонара',
    'description': ('Порция макарон под тёмным соусом. '
                    'Паста — из ванильного мороженого, '
                    'продавленного через пресс с дырочками, '
                    'соус — ликёр с орехами. Buon appetito!'),
    },
    {
    'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
    'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                    'яичный порошок из куриных яиц, патока карамельная. '
                    'Общее количество микробов в 1 мл мороженого: '
                    'не более 250 тыс.'),
    },
    {
    'name': 'Люминесцентное мороженое',
    'description': ('Сливочное мороженое с белками, активированными кальцием. '
                    'Светится, если облизнуть. '
                    'Можно подавать в тыкве на Хэллоуин '
                    'или кормить собаку Баскервилей.'),
    },
    {
    'name': 'Жареное мороженое',
    'description': ('Шарики мороженого обваливают яйце и в панировке, '
                    'сильно замораживают и быстро обжаривают '
                    'в растительном масле. Едят быстро.'),
    },
    {
    'name': 'Томатное мороженое',
    'description': ('Сливки, помидоры, чеснок, лавровый лист, '
                    'молотый перец. Если растает — '
                    'можно подавать к обеду как первое блюдо.'),
    },
]
