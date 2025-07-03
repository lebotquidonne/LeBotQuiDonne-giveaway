from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx import FadeIn, FadeOut

# Paramètres généraux
W, H = 720, 1280
BG_COLOR = (0, 0, 0)
FONT = "/usr/share/fonts/gdouros-symbola/Symbola.ttf"
FONT_SIZE = 55                 # un peu plus petit pour éviter débordement
DURATION_PER_LINE = 3.0
FADE_DURATION = 0.7
OUTPUT = "presentation_lebotquidonne.mp4"

MAX_TEXT_WIDTH = int(W * 0.80)  # réduire encore la largeur max

BASE_TIME = 1.5       # Durée minimale par phrase (en secondes)
TIME_PER_LINE = 1.2   # Durée supplémentaire par ligne

lines = [
    "Salut,\nici LeBotQuiDonne 👋",
    "Je redistribue\nune partie\n de mes revenus\nà ma communauté 💸",
    "Chaque tirage\nest automatique\net 100% transparent 🎲",
    "Pour participer,\nil suffit de\ncommenter\ncette vidéo 📝",
    "Seuls les abonnés\nYouTube\npeuvent gagner\n(preuve demandée) ✅",
    "Le tirage est visible\nen animation,\npour que\ntout soit clair 🎬",
    "Rejoins la communauté\nsur Discord\npour suivre\nles résultats ! 🚀",
    "Prêt à tenter\nta chance ?\nCommente vite ! ✨"
]

clips = []
t = 0

for line in lines:
    # Nombre de lignes dans la phrase (count '\n' + 1)
    n_lines = line.count('\n') + 1
    duration = BASE_TIME + TIME_PER_LINE * n_lines

    txt_clip = (
        TextClip(
            text=line,
            font=FONT,
            font_size=FONT_SIZE,
            color="white",
            size=(MAX_TEXT_WIDTH, H),
            method="caption"
        )
        .with_position(("center", "center"))
        .with_start(t)
        .with_duration(duration)
    )
    txt_clip = FadeIn(FADE_DURATION).apply(txt_clip)
    txt_clip = FadeOut(FADE_DURATION).apply(txt_clip)
    clips.append(txt_clip)
    t += duration

background = ColorClip(size=(W, H), color=BG_COLOR, duration=t)

final = CompositeVideoClip([background, *clips], size=(W, H))

final.write_videofile(OUTPUT, fps=30, codec="libx264", audio=False)

print(f"Vidéo générée → {OUTPUT}")
