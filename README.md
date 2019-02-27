# Информация ФНС об уплаченных налогах по компаниям

Домашняя страница набора данных: <https://www.nalog.ru/opendata/7707329152-paytax>

Пресс-релиз: <https://www.nalog.ru/rn77/news/activities_fts/8165638>

## Как использовать

Вывести словарь со значениями уплаченных компаниями налогов. 

```python 
from pprint import pprint
from paytax import from_file, is_nil

FILENAME = '361db.xml'
xs = [x for x in from_file(FILENAME) if not is_nil(x)]
pprint(xs)
```

Результат:

```
[
 # ... 
 {'inn': '8903023469',
  'org': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "РЕСУРС ТЕРРИТОРИАЛЬНОГО '
         'РАЗВИТИЯ"',
  'simple': 8099.0,
  'trans': 1130.0},
 {'inn': '8603107277',
  'org': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "АВТО-ГАЗОВЫЕ СИСТЕМЫ"',
  'vmen': 19418.0},
 {'imed': 48855.45,
  'inn': '8603112492',
  'ipens': 236861.77,
  'isoc': 8621.01,
  'org': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "СТАЛЬСТРОЙ"',
  'profit': 30869.0,
  'prop': 606.0,
  'vat': 1359776.0}]
```

Обозначения переменных
---------------------- 

| Ключ | Вид налога |
|:----:| --- |
| **imed** |  Страховые взносы на обязательное медицинское страхование работающего населения, зачисляемые в бюджет Федерального фонда обязательного медицинского страхования |
| **isoc** |  Страховые взносы на обязательное социальное страхование на случай временной нетрудоспособности и в связи с материнством |
| **ipens** |  Страховые и другие взносы на обязательное пенсионное страхование, зачисляемые в Пенсионный фонд Российской Федерации |
| **legacy** |  Задолженность и перерасчеты по ОТМЕНЕННЫМ НАЛОГАМ  и сборам и иным обязательным платежам (кроме ЕСН, страх. Взносов) |
| **nontax** |  НЕНАЛОГОВЫЕ ДОХОДЫ, администрируемые налоговыми органами |
| **vat** |  Налог на добавленную стоимость |
| **profit** |  Налог на прибыль |
| **prop** |  Налог на имущество организаций |
| **land** |  Земельный налог |
| **trans** |  Транспортный налог |
| **vmen** |  Единый налог на вмененный доход для отдельных видов деятельности |
| **simple** |  Налог, взимаемый в связи с применением упрощенной системы налогообложения |
