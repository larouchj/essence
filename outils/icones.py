# Génère les icônes de l'app (pompe à essence stylisée) : python3 outils/icones.py
from PIL import Image, ImageDraw
def icone(t):
    s = 4  # suréchantillonnage pour des bords lisses
    T = t * s
    im = Image.new("RGB", (T, T), (14, 90, 60))
    d = ImageDraw.Draw(im)
    u = T / 100
    blanc = (255, 255, 255)
    # corps de la pompe
    d.rounded_rectangle([28*u, 22*u, 60*u, 80*u], radius=6*u, fill=blanc)
    # fenêtre (afficheur du prix)
    d.rounded_rectangle([34*u, 29*u, 54*u, 42*u], radius=2.5*u, fill=(14, 90, 60))
    # socle
    d.rounded_rectangle([24*u, 78*u, 64*u, 84*u], radius=2*u, fill=blanc)
    # boyau + pistolet
    d.line([(60*u, 36*u), (70*u, 36*u), (74*u, 42*u), (74*u, 66*u)], fill=blanc, width=int(5*u), joint="curve")
    d.ellipse([70*u, 63*u, 78*u, 71*u], fill=blanc)
    d.rounded_rectangle([67*u, 24*u, 76*u, 34*u], radius=2*u, fill=blanc)
    return im.resize((t, t), Image.LANCZOS)
for t in (180, 192, 512):
    icone(t).save(f"icone-{t}.png")
print("ok")
