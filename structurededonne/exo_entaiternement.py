#* liste = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#li1 = slice(0,3)
#print(liste[li1])

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(f'Touche {key.char} pressée')
    except AttributeError:
        print(f'Touche spéciale {key} pressée')

def on_release(key):
    print(f'Touche {key} relâchée')
    if key == Key.esc:
        # Arrêter le listener
        return False

# Collecter les événements du clavier
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
