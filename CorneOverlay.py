
import tkinter
import tkinter.font
import json

app  = tkinter.Tk()

jfile = open('config.json', 'r')
jconfig = json.load(jfile)

win    = jconfig['window']
keymap = jconfig['keymap']
font   = jconfig['font']

# 左右上下の余白
margin_w = win['width'] / 50
margin_h = win['height'] / 14

# 中央の余白
center_gap = win['width'] / 16

# キーとキーのスキマ
offset_w = (win['width'] - margin_w) / 100
offset_h = (win['height'] - margin_h) / 30

# キーの縦軸をずらす数値
indent = { 0:3, 1:3, 2:1, 3:0, 4:1, 5:2, 6:2, 7:1, 8:0, 9:1, 10:3, 11:3 }

keysize_w = (win['width'] - (offset_w * 11) - (margin_w * 2) - center_gap) / 12
keysize_h = (win['height'] - (offset_h * 5) - (margin_h * 2)) / 3

# ウィンドウ初期設定
app.title("CorneOverlay")
app.width  = jconfig['window']['width']
app.height = jconfig['window']['height']
app.font   = tkinter.font.Font(app, family = font['name'], size = font['size'], weight = font['weight'])
app.geometry(str(app.width) + "x" + str(app.height))  # 画面サイズ
app.attributes("-alpha", win['alpha'])                # 画面透過度
app.resizable(False, False)                           # 画面サイズ変更不可
app.attributes("-topmost", win['allwaysTop'])         # 最前列表示
app.config(bg="gray")                                 # 背景をグレーに
app.attributes("-transparentcolor", "gray")           # グレーだけ透過


def drawKeyLane(lane, canvas, yy):
    for i in range(len(keymap[lane])):
        canvas.append(tkinter.Canvas(app, width = keysize_w, height = keysize_h, bg='white', relief='groove', borderwidth=0, highlightbackground='black', highlightthickness = 1))
        canvas[i].create_text(keysize_w / 2 + 1, keysize_h / 2 - 1, font = app.font, text = keymap[lane][i])
        x = i * keysize_w + margin_w + offset_w * i
        x = x if i < 6 else x + center_gap
        if i in indent:
            y = yy + offset_w * indent[i]
        canvas[i].place(x = x, y = y)
        
    
key_top = []
y = margin_h
drawKeyLane('top', key_top, y)

key_mid = []
y = margin_h + keysize_h + offset_h
drawKeyLane('mid', key_mid, y)

key_bot = []
y = margin_h + keysize_h * 2 + offset_h * 2
drawKeyLane('bot', key_bot, y)


app.mainloop()