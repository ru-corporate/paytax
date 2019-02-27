from pprint import pprint 
import xml.etree.ElementTree as etree    

def get_tree(filename):
    return etree.parse(filename)  

def extract_company_data(tree):
    root = tree.getroot()                    
    for child in root: 
        entity = {}
        for grandson in child:   
            add = parse_attribs(grandson.attrib)
            entity.update(add)
        yield entity
            
             # ЕСН
NAMER = dict(imed = 'Страховые взносы на обязательное медицинское страхование работающего населения, зачисляемые в бюджет Федерального фонда обязательного медицинского страхования',
             isoc = 'Страховые взносы на обязательное социальное страхование на случай временной нетрудоспособности и в связи с материнством',
             ipens = 'Страховые и другие взносы на обязательное пенсионное страхование, зачисляемые в Пенсионный фонд Российской Федерации',
             # Пустые
             legacy = 'Задолженность и перерасчеты по ОТМЕНЕННЫМ НАЛОГАМ  и сборам и иным обязательным платежам (кроме ЕСН, страх. Взносов)',
             nontax = 'НЕНАЛОГОВЫЕ ДОХОДЫ, администрируемые налоговыми органами',
             # Обычные налоги
             vat = 'Налог на добавленную стоимость',
             profit = 'Налог на прибыль', 
             prop = 'Налог на имущество организаций',
             land = 'Земельный налог',
             trans = 'Транспортный налог',
             # Спецрежимы
             vmen = 'Единый налог на вмененный доход для отдельных видов деятельности',
             simple = 'Налог, взимаемый в связи с применением упрощенной системы налогообложения',
             )

TAX_NAMES = list(NAMER.keys())
ORG = 'org'
INN = 'inn'
ALL_NAMES = TAX_NAMES + [ORG, INN]

def total(company, selected_keys=TAX_NAMES):
    keys = [k for k in company.keys() if k in selected_keys]
    return sum([company[k] for k in keys])

def paid_something(company):
    return total(company) != 0 

def no_space(s):
    return s.lower().replace(" ", "") 

RENAMER = {no_space(v):k for k,v in NAMER.items()} 

def rename_tax(long_name, renamer=RENAMER):
    return renamer.get(no_space(long_name), long_name) 
            
def is_zero(s: str):
    return s == "0.00"

def parse_attribs(attribs):            
    d = {}
    if 'НаимОрг' in attribs.keys():
        d[ORG] = attribs['НаимОрг']
        d[INN] = attribs['ИННЮЛ']
        return d
    if 'НаимНалог' in attribs.keys():
        value_str = attribs.get('СумУплНал')
        if not is_zero(value_str):        
            tax_name = rename_tax(attribs.get('НаимНалог'))
            value = float(attribs.get('СумУплНал'))
            d[tax_name] = float(value_str)
    return d 

def from_file(filename):
    tree = get_tree(filename) 
    xs = extract_company_data(tree) 
    return list(xs)


def inspect(filename):
    tree = get_tree(filename)
    root = tree.getroot()                    
    print(root)
    for child in root:    
        print()
        for grandson in child:   
            d = grandson.attrib
            if 'НаимОрг' in d.keys():
                print (d['НаимОрг'])
                print (d['ИННЮЛ'])            
            else: 
                print(d.get('НаимНалог'), d.get('СумУплНал'))

# Псевдокод:
# =========    
# скачать один и распаковать много файлов
# собрать поток словарей
# записать в CSV
# записать в Excel 
# файлы: all, nonempty

# Отдельные задания:
# =========

# ---    
    
# проверить закон последних чисел - подозрительные целые 

# ---    

# состыковать налог ан прибыль
# кто в каких режимах, планки по размеру 
# связь с базами (ФОТ, объем активов)

# ---    

# налоговая нагрузка по отраслям 
# больше фирма - больше налогов?

# ---    

    
if __name__ == "__main__":
    FILENAME = '361db.xml'
    alls = from_file(FILENAME)
    xs = list(filter(paid_something, alls))
    pprint(xs)
    print(len(alls), len(xs)) 

