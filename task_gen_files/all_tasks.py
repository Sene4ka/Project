# -*- coding: utf-8 -*-
import json
sl = {"00000001": ["Информатика. Максимальное количество цветов в палитре снимка размером ixj", "Камера делает фотоснимки {} на {} пикселей. При этом объём файла с изображением не может превышать {} {}байт, упаковка данных не производится. Какое максимальное количество цветов можно использовать в палитре изображения?", "Переводим {}Байты в Биты: {}\nНаходим количество пикселей: {}\nНаходим сколько бит можно выделить на пиксель(с округлением в меньшую сторону): {}\nНаходим количество цветов: {}", "1"],
      "00000002": ["Информатика. Степени и системы счисления. Количество символов 'n' в числе y в i системе счисления", "Значение арифметического выражения: {}^{} {} {}^{} записали в системе счисления с основанием {}. Сколько символов «{}» в этой записи?", "Считаем значение выражения: {}\nПереводим в {} систему счисления: {} в 10 = {} в {}\nСчитаем количество символов «{}»: {}", "2"],
      "00000003": ["Информатика. Обьем растрового изображения n * m пикселей с палитрой из k цветов", "Какой минимальный объём памяти (в {}байт) нужно зарезервировать, чтобы можно было сохранить любое растровое изображение размером {} на {} пикселов при условии, что в изображении могут использоваться {} различных цветов?", "Найдем количество пикселей: {} * {} = {} пикселей\nНайдем количество бит информации на пиксель: {} цветов =  2 ^ {} цветов -> {} бит на пиксель\nНайдем вес изображения в битах: {} * {} = {} бит\nПереведем размер изображения в {}Байты: {} = {} {}Байт -> Зарезервировать нужно {} {}Байт", "1"],
      "00000004": ["Информатика. Количество цветов в изображении n*m пикселей размером k КБайт", "Изображение размером {} на {} пикселей занимает в памяти {} {}байт (без учёта сжатия). Найдите максимально возможное количество цветов в палитре изображения.", "Найдем количество пикселей в изображении: {} * {} = {} пикселей\nНайдем вес изображения: {} = {} бит\nНайдем количество бит информации на пиксель: {} / {} = {} бит на пиксель\nНайдем количесво цветов: 2 ** {} = {} цветов", "1"],
      "00000005": ["Информатика. Нахождение оригинального размера файла изображения через изменение объема путем изменения количества цветов.", "После преобразования растрового {}-цветного графического файла в файл с палитрой из {} цветов его размер {} на {} Кбайт. Каков был размер исходного файла в Кбайтах?", "Найдем количество бит информации на пиксель у первого и второго файлов:\n1){} = 2 ** {} -> {} бит на пиксель\n2){} = 2 ** {} -> {} бит на пиксель\nТогда их объемы будут равны:\nV1 = k * {};V2 = k * {}, где k - количество пикселей в изображении\nПо условию V2 = V1 {} {} -> {} * k - {} * k = {} * 1024 * 8;\n{} * k = {} * 1024 * 8;\nk = {}\nТогда V1 = {} * {} = {}", "2"]}
with open("all_tasks.json", "w+") as f:
    json.dump(sl, f)