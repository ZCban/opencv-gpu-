import os
import time
import pyautogui
import pygetwindow as gw
import tkinter as tk



def update_timer():
    global wait_time
    if wait_time > 0:
        timer_label.config(text=f"Time remaining: {wait_time} seconds")
        wait_time -= 1
        root.lift()
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Waiting complete.")
        root.after(30, root.destroy)  # Chiude la finestra dopo 3 secondi

# Nome della finestra del programma cmake-gui.exe
cmake_gui_window_name = "CMake 3.27.2"

# Percorso completo per il programma cmake-gui.exe
cmake_gui_path = r'C:\Users\wssd\Desktop\Nuova cartella (2)\cmake-3.27.2-windows-x86_64\bin\cmake-gui.exe'  # Inserisci il percorso corretto

# Percorso completo per il file "path_conf.txt"
path_conf_file = r'C:\Users\wssd\Desktop\Nuova cartella (2)\path_conf.txt'  # Inserisci il percorso corretto

try:
    # Avvia cmake-gui.exe
    os.startfile(cmake_gui_path)

    # Aspetta un po' di tempo per il programma per avviarsi completamente
    time.sleep(2)

    # Trova la finestra del programma cmake-gui.exe
    cmake_gui_window = gw.getWindowsWithTitle(cmake_gui_window_name)
    if cmake_gui_window:
        cmake_gui_window[0].maximize()

    # Aspetta un po' di tempo
    time.sleep(1)

    with open(path_conf_file, 'r') as file:
        # Leggi la prima riga
        first_line = file.readline().strip()
        # Leggi la seconda riga
        second_line = file.readline().strip()
        # Leggi la terza riga
        third_line = file.readline().strip()
        # Leggi la quarta riga
        fourth_line = file.readline().strip()
        # Leggi la quinta riga
        fifth_line = file.readline().strip()
        # Leggi la sesta riga
        sixth_line = file.readline().strip()
        # Leggi la settima riga
        seventh_line = file.readline().strip()
        # Leggi l'ottava riga
        eighth_line = file.readline().strip()
        # Leggi la nona riga
        ninth_line = file.readline().strip()
        # Leggi la decima riga
        tenth_line = file.readline().strip()
        # Leggi la undicesima riga
        eleventh_line = file.readline().strip()

        # Incolla il contenuto della prima riga alla posizione (583, 62)
        pyautogui.click(x=583, y=62)  # Fai clic sulla posizione
        pyautogui.write(first_line)   # Scrivi il testo

        # Incolla il contenuto della seconda riga alla posizione (608, 117)
        pyautogui.click(x=608, y=117)  # Fai clic sulla posizione
        pyautogui.click(button='right')
        pyautogui.click(x=638, y=283)
        pyautogui.press('backspace')
        pyautogui.keyUp('backspace')
        pyautogui.click(x=608, y=117)
        pyautogui.write(second_line)
        pyautogui.click(x=608, y=117)

    # Aspetta un po' di tempo
    time.sleep(2)
    # Premi configura
    pyautogui.click(x=47, y=853)
    # Crea la cartella build
    pyautogui.click(x=1057, y=565)
    # Seleziona il menu piattaforma
    pyautogui.click(x=1190, y=503)
    time.sleep(1)
    # Seleziona x64
    pyautogui.click(x=926, y=582)
    # Seleziona finish
    pyautogui.click(x=1082, y=683)

    wait_time = 180
    root = tk.Tk()
    root.title("Timer")
    timer_label = tk.Label(root, text="", font=("Helvetica", 24))
    timer_label.pack(pady=50)
    update_timer()
    root.mainloop()



    ##WITH_CUDA
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(third_line)
    pyautogui.click(x=330, y=197)
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    pyautogui.click(button='right')
    pyautogui.click(x=539, y=310)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')

    ##OPENCV_DNN_CUDA
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(fourth_line)
    pyautogui.click(x=330, y=197)
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    pyautogui.click(button='right')
    pyautogui.click(x=539, y=310)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')

    ##ENABLE_FAST_MATH
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(fifth_line)
    pyautogui.click(x=330, y=197)
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    pyautogui.click(button='right')
    pyautogui.click(x=539, y=310)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')

    ##BUILD_opencv_world
    #premi barra di ricerca
    #pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    #pyautogui.write(sixth_line)
    #pyautogui.click(x=330, y=197)
    #premi barra di ricerca
    #pyautogui.click(x=491, y=149)
    #pyautogui.click(button='right')
    #pyautogui.click(x=539, y=310)
    #pyautogui.press('backspace')
    #pyautogui.keyUp('backspace')

    ##OPENCV_EXTRA_MODULES_PATH
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(seventh_line)
    pyautogui.click(x=1425, y=196)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')
    pyautogui.write(eighth_line)
    pyautogui.click(x=1425, y=196)
    pyautogui.click(x=491, y=149)
    pyautogui.click(button='right')
    pyautogui.click(x=539, y=310)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')

    time.sleep(1)
    ##premi configura
    pyautogui.click(x=44, y=854)

    wait_time = 70
    root = tk.Tk()
    root.title("Timer")
    timer_label = tk.Label(root, text="", font=("Helvetica", 24))
    timer_label.pack(pady=50)
    update_timer()
    root.mainloop()

    ##FAST MAT CUDA
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(ninth_line)
    pyautogui.click(x=329, y=198)
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    pyautogui.click(button='right')
    pyautogui.click(x=539, y=310)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')

    
    ##CUDA ARCH
    #premi barra di ricerca
    pyautogui.click(x=491, y=149)
    #scrivi la terza riga
    pyautogui.write(tenth_line)
    pyautogui.click(x=413, y=196)
    pyautogui.press('backspace')
    pyautogui.keyUp('backspace')
    pyautogui.write(eleventh_line)
    pyautogui.click(x=413, y=196)

    #premi GENERATE
    pyautogui.click(x=126, y=857)
    print('pronto per essere montato con visual studio')

    

except:
    print('Errore: controlla il codice')


