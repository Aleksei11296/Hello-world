from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   """
   value: значение, к которому нужно применить фильтр
   """
   list = ['команда', 'оружие', 'жизнь']
   for word in value.split():
      if word in list:
         value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
   return value