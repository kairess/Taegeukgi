from PIL import Image, ImageDraw

class Taegeukgi():
    def draw(self, w=1200, h=800):
        # White background: Brightness, purity, and peace
        img = Image.new('RGB', (w, h), color='white')

        # Taegeuk shape = Yin + Yang
        taegeuk = Image.new('RGB', (h // 2, h // 2), color='white')
        draw = ImageDraw.Draw(taegeuk)

        draw.pieslice((0, 0, h // 2, h // 2), start=180, end=360, fill='red')
        draw.pieslice((0, 0, h // 2, h // 2), start=0, end=180, fill='blue')

        draw.ellipse((0, h // 8, h // 4, h * 3 // 8), fill='red')
        draw.ellipse((h // 4, h // 8, h // 2, h * 3 // 8), fill='blue')

        taegeuk = taegeuk.rotate(-33.69, fillcolor='white')

        img.paste(taegeuk, (h // 2, h // 4))

        # Heaven 건
        sky = Image.new('RGB', (h // 4, h // 6), color='black')
        draw = ImageDraw.Draw(sky)

        draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill='white')
        draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill='white')

        sky = sky.rotate(90 - 33.69, expand=True, fillcolor='white')

        img.paste(sky, (h * 22 // 96, h * 9 // 96))

        # Earth 곤
        earth = Image.new('RGB', (h // 4, h // 6), color='black')
        draw = ImageDraw.Draw(earth)

        draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill='white')
        draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill='white')
        draw.rectangle((h * 11 // 96, 0, h * 13 // 96, h * 2 // 48), fill='white') # 1
        draw.rectangle((h * 11 // 96, h * 3 // 48, h * 13 // 96, h * 5 // 48), fill='white') # 2
        draw.rectangle((h * 11 // 96, h * 6 // 48, h * 13 // 96, h * 8 // 48), fill='white') # 3

        earth = earth.rotate(90 - 33.69, expand=True, fillcolor='white')

        img.paste(earth, (h * 96 // 96, h * 59 // 96))

        # Water 감
        water = Image.new('RGB', (h // 4, h // 6), color='black')
        draw = ImageDraw.Draw(water)

        draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill='white')
        draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill='white')
        draw.rectangle((h * 11 // 96, 0, h * 13 // 96, h * 2 // 48), fill='white') # 1
        draw.rectangle((h * 11 // 96, h * 6 // 48, h * 13 // 96, h * 8 // 48), fill='white') # 3

        water = water.rotate(90 + 33.69, expand=True, fillcolor='white')

        img.paste(water, (h * 96 // 96, h * 9 // 96))

        # Fire 이
        fire = Image.new('RGB', (h // 4, h // 6), color='black')
        draw = ImageDraw.Draw(fire)

        draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill='white')
        draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill='white')
        draw.rectangle((h * 11 // 96, h * 3 // 48, h * 13 // 96, h * 5 // 48), fill='white') # 2

        fire = fire.rotate(90 + 33.69, expand=True, fillcolor='white')

        img.paste(fire, (h * 22 // 96, h * 59 // 96))

        return img

if __name__ == '__main__':
    t = Taegeukgi().draw(w=1200, h=800)

    t.show()
