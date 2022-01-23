# "Камера делает фотоснимки {} на {} пикселей. При этом объём файла с изображением не может превышать {} {}байт, упаковка данных не производится. Какое максимальное количество цветов можно использовать в палитре изображения?"
import json
resolutions = ["3840:2160", "2560:1440", "1920:1080", "1600:900", "1440:864", "1366:768", "1280:720", "1136:640", "1024:576", "960:540", "854:480", "640:360", "426:240", "256:144"]
# resolutions = reversed(resolutions)
data = {}
c = 1
for i in resolutions:
    res = i.split(":")
    pix = int(res[0]) * int(res[1])
    for j in range(1, 1024):
        mb = 1024 * 1024 * 8 * j
        kb = 1024 * 8 * j
        if 1 <= mb // pix <= 16 and len(str(mb / pix).split(".")[-1]) <= 16:
            data[str(c).rjust(8, "0")] = (str(res[0]), str(res[1]), str(j), "М"), ("Мега", f"{j} * 1024 * 1024 * 8 = {mb}МБайт.", f"{res[0]} * {res[1]} = {pix} пикселей.", f"{kb} // {pix} = {kb // pix} бит на пиксель.", f"2 ^ {kb // pix} цветов."), str(2 ** (mb // pix))
            c += 1
        if 1 <= kb // pix <= 16 and len(str(kb / pix).split(".")[-1]) <= 4:
            data[str(c).rjust(8, "0")] = (str(res[0]), str(res[1]), str(j), "К"), ("Кило", f"{j} * 1024 * 8 = {kb}КБайт.", f"{res[0]} * {res[1]} = {pix} пикселей.", f"{kb} // {pix} = {kb // pix} бит на пиксель.", f"2 ^ {kb // pix} цветов."), str(2 ** (kb // pix))
            c += 1
with open("00000001.json", "w+") as f:
    json.dump(data, f)
