from tkinter import *
import pygame
import tkinter.ttk as ttk
import os
import sys, time, random
import numpy as np
import pyglet
from pygame.locals import *
from PIL import Image , ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
from tkinter.ttk import Progressbar
from random import randint
from tkinter import ttk


def Rock_Paper_Scissor():

    root = Toplevel(Home_Page)

    root.title('Rock, Paper, Scissors')
    # root.iconbitmap('')
    root.geometry("600x600")
    root.config(bg = "white")
    root.resizable(False, False)

    Bg = PhotoImage(file=r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\GAMER_2.png')
    # CREATING LABEL
    my_label = Label(root, image = Bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define our images
    rock = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\ROCK_5.png')
    paper = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\PAPER_5.png')
    scissors = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\SCISSORS_5.png')

    # Add Images to a list
    image_list = [rock, paper, scissors]

    # Pick random number between 0 and 2
    pick_number = randint(0, 2)

    # Throw up an image when the program starts
    image_label = Label(root, image=image_list[pick_number], bd=0)
    image_label.pack(pady=20)

    # SPIN FUNCTION
    def spin():
        # Pick random numnber
        pick_number = randint(0, 2)
        # Show image
        image_label.config(image=image_list[pick_number])

        # Convert Dropdown choice to a number

        if user_choice.get() == "Rock":
            user_choice_value = 0
        elif user_choice.get() == "Paper":
            user_choice_value = 1
        elif user_choice.get() == "Scissors":
            user_choice_value = 2

        # Determine WIN OR LOSE

        if user_choice_value == 0:  # Rock
            if pick_number == 0:
                win_lose_label.config(text = " IT'S A TIE !!! ")
            elif pick_number == 1:  # Paper
                win_lose_label.config(text = " PAPER COVERS ROCK !!! You Lose... ")
            elif pick_number == 2:  # Scissors
                win_lose_label.config(text = " ROCK SMASHES SCISSORS !!!  You Win... ")

        # If USer Picks Paper
        if user_choice_value == 1:  # Paper
            if pick_number == 1:
                win_lose_label.config(text=" IT'S A TIE !!! ")
            elif pick_number == 0:  # Rock
                win_lose_label.config(text=" PAPER COVERS ROCK !!! You Win... ")
            elif pick_number == 2:  # Scissors
                win_lose_label.config(text=" SCISSORS CUTS PAPER !!! You Lose...")

        # If User Pics Scissors
        if user_choice_value == 2:  # Scissors
            if pick_number == 2:
                win_lose_label.config(text=" IT'S A TIE !!! ")
            elif pick_number == 0:  # Rock
                win_lose_label.config(text=" ROCK SMASHES SCISSORS !!! You Lose...")
            elif pick_number == 1:  # Paper
                win_lose_label.config(text=" SCISSORS CUTS PAPER !!! You Win!!!")

    # MAKING CHOICE

    user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
    user_choice.current(0)
    user_choice.pack(pady=20)

    # SPIN BOX
    spin_button = Button(root, text="Spin!", command = spin, font=("Impact",12),fg="white", bg="black")
    spin_button.pack(pady=10)

    # RESULTS
    win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
    win_lose_label.pack(pady=50)

    root.mainloop()

###############################################################################

def snake():

    Home_Page.resizable(False, False)

    # Difficulty settings
    # Easy      ->  10
    # Medium    ->  25
    # Hard      ->  40
    # Harder    ->  60
    # Impossible->  120
    difficulty = 10

    # Window size
    frame_size_x = 720
    frame_size_y = 480

    check_errors = pygame.init()

    # second number in tuple gives number of errors
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} error found, exiting..')
        sys.exit(-1)
    else:
        print('>> Hard Work of Team Sounzonix :)')

    # This is the game window
    pygame.display.set_caption('Snake Eater')
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

    # Colors (R, G, B)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # FPS controller
    fps_controller = pygame.time.Clock()

    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

    food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x / 10, 15)
        else:
            score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
        game_window.blit(score_surface, score_rect)
        # pygame.display.flip()

    def game_over():
        my_font = pygame.font.SysFont('Impact', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Main logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # snake direction
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body grow
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
            game_over()
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)
###############################################################################

def Tic_Tak_Toe():

    Home_Page.resizable(False, False)

    # initializes pygame
    check_errors = pygame.init()
    # error check
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} error found, exiting...')
        sys.exit(-1)
    else:
        print('>> Hard work of team soundzonix :)')

    # CONSTANTS
    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 200
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55

    # rgb
    RED = (255, 0, 0)
    BG_COLOR = (28, 170, 156)
    LINE_COLOR = (23, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (239, 231, 200)
    BLACK_COLOR = (0,0,0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    screen.fill(BLACK_COLOR)

    # CONSOLE BOARD
    board = np.zeros((BOARD_ROWS, BOARD_COLS))

    def draw_lines():
        # 1 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        # 2 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        # 1 vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 2 vertical
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     CROSS_WIDTH)

    def mark_square(row, col, player):
        board[row][col] = player

    def available_square(row, col):
        return board[row][col] == 0

    def is_board_full():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    return False

        return True

    def check_win(player):
        # vertical
        for col in range(BOARD_COLS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vertical_winning_line(col, player)
                return True

        # horizontal
        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_winning_line(row, player)
                return True

        # asc diagonal
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True

        # desc diagonal
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player)
            return True

        return False

    def draw_vertical_winning_line(col, player):
        posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(row, player):
        posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

    def restart():
        screen.fill(BG_COLOR)
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = 0

    draw_lines()

    player = 1
    game_over = False

    # main Logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):

                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

        pygame.display.update()

###############################################################################

def Select_game():

    game_selection = Toplevel(Home_Page)
    global img2
    game_selection.title("Select Your Game")
    game_selection.geometry("600x600+330-50")
    game_selection.resizable(False, False)
    game_selection.iconbitmap(r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\icon_3.ico')
    
    img1 = Image.open(r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\GAMER_1.png')
    img2 = ImageTk.PhotoImage(img1)

    my_label_2 = Label(game_selection, image=img2)
    my_label_2.place(x=0,y=0)
    
    my_Label_1 = Label(game_selection, text="Enjoy Gaming!!", font=("Impact",40),fg="white", bg="black")
    my_Label_1.pack(pady=10)


    btn1=Button(game_selection, text = "Play Snake", command=snake, font = ("Impact",12),fg="white", bg="black")
    btn1.place(x=23, y=480)

    btn2 = Button(game_selection, text = "Play Tic Tac Toe", command=Tic_Tak_Toe, font = ("Impact",12),fg="white", bg="black")
    btn2.place(x=250, y=480)

    btn3 = Button(game_selection, text = "Play RPS", command = Rock_Paper_Scissor, font = ("Impact",12),fg="white", bg="black")
    btn3.place(x=497, y=480)

###############################################################################

def mp3():

    root = Toplevel(Home_Page)

    root.title('Soundzie')
    root.iconbitmap(r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\icon_3.ico')
    root.geometry("1000x500+145-20")
    root.resizable(False, False)

    # Initialze Pygame Mixer
    pygame.mixer.init()

    # BACKGROUND IMAGE
    Bg = PhotoImage(file="C:/Users/Pransh Gupta/Downloads/CSE PROJECT/GUI/images/music_bg_5.png")

    # CREATING LABEL
    my_label = Label(root, image = Bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    # GET SONG LENGTH
    def play_time():

        # GET CURRENT SONG ELAPSED TIME
        current_time = pygame.mixer.music.get_pos() / 1000
        # CONVERT TO TIME FORMAT
        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
        # Get the current playing song
        song = song_box.get(ACTIVE)
        # add directory structure and mp3 to song title
        song = f'C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio/{song}.mp3'

        # GET SONG LENGTH WITH MUTAGEN
        song_mut = MP3(song)
        song_length = song_mut.info.length

        # CHANGE TO TIME FORMAT
        converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

        # OUTPUT
        status_bar.config(text = f'Time Elapsed : {converted_current_time}  of  {converted_song_length}   ')
        status_bar.after(1000, play_time)

    # Add Song Function
    def add_song():
        song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

        # strip out the directory info and .mp3 extension from the song name
        song = song.replace("C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio", "")
        song = song.replace(".mp3", "")

        # Add song to listbox
        song_box.insert(END, song)

    # Add many songs to playlist
    def add_many_songs():
        songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

        # Loop through song list and replace directory info and mp3
        for song in songs:
            song = song.replace("C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio", "")
            song = song.replace(".mp3", "")
            # Insert into playlist
            song_box.insert(END, song)

    # PLAY SELECTED SONG
    def play():
        song = song_box.get(ACTIVE)
        song = f'C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        play_time()

    # STOP SELECTED SONG
    def stop():
        pygame.mixer.music.stop()
        song_box.selection_clear(ACTIVE)
        status_bar.config(text='')

    # Create Global Pause Variable
    global paused
    paused = False

    # PAUSE AND UNPAUSE THE CURRENT SONG
    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            # Unpause
            pygame.mixer.music.unpause()
            paused = False
        else:
            # Pause
            pygame.mixer.music.pause()
            paused = True

    # PLAY NEXT SONG IN THE PLAYLIST
    def next_song():

        # Get the current song tuple number
        next_one = song_box.curselection()
        # Add one to the current song number
        next_one = next_one[0] + 1
        # Grab song title from playlist
        song = song_box.get(next_one)
        # add directory structure and mp3 to song title
        song = f'C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio/{song}.mp3'
        # Load and play song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in playlist listbox
        song_box.selection_clear(0, END)

        # Activate new song bar
        song_box.activate(next_one)

        # Set Active Bar to Next Song
        song_box.selection_set(next_one, last=None)

    # PLAY PREVIOUS SONG IN THE PLAYLIST

    def previous_song():

        # Get the current song tuple number
        next_one = song_box.curselection()
        # Subtract one from the current song number
        next_one = next_one[0] - 1
        # Grab song title from playlist
        song = song_box.get(next_one)
        # add directory structure and mp3 to song title
        song = f'C:/Users/Pransh Gupta/Downloads/CSE PROJECT/audio/{song}.mp3'
        # Load and play song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in playlist listbox
        song_box.selection_clear(0, END)

        # Activate new song bar
        song_box.activate(next_one)

        # Set Active Bar to Next Song
        song_box.selection_set(next_one, last=None)

    # VOLUME INCREASE AND DECREASE

    def vol_up():
        vol = pygame.mixer.music.get_volume()
        if (vol >= vol * 100):
            pygame.mixer.music.set_volume(vol + 0.1)
        else:
            pygame.mixer.music.set_volume(vol + 0.01)
        ProgressbarVolumeLabel.config(text='{}%'.format(int(pygame.mixer.music.get_volume() * 100)))
        ProgressbarVolume['value'] = pygame.mixer.music.get_volume() * 100

    def vol_down():
        vol = pygame.mixer.music.get_volume()
        if (vol <= vol * 100):
            pygame.mixer.music.set_volume(vol - 0.01)
        else:
            pygame.mixer.music.set_volume(vol - 0.05)
        ProgressbarVolumeLabel.config(text='{}%'.format(int(pygame.mixer.music.get_volume() * 100)))
        ProgressbarVolume['value'] = pygame.mixer.music.get_volume() * 100

        # DELETE A SONG

    def delete_song():
        stop()
        # Delete Currently Selected Song
        song_box.delete(ANCHOR)
        # Stop Music if it's playing
        pygame.mixer.music.stop()

    # Delete All Songs from Playlist
    def delete_all_songs():
        stop()
        # Delete All Songs
        song_box.delete(0, END)
        # Stop Music if it's playing
        pygame.mixer.music.stop()

    # INTERFACE :-

    # Create Master Frame
    master_frame = Frame(root)
    master_frame.pack(pady = 60)

    # Create Playlist Box
    song_box = Listbox(master_frame, bg="black", fg="red", width=110, selectbackground = "green", selectforeground = "black")
    song_box.grid(row = 0, column = 0)

    # Create Player Control Frame
    controls_frame = Frame(master_frame)
    controls_frame.grid(row = 1, column = 0, pady = 20, padx = 0)

    # Define Player Control Button Images
    back_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\BACKWARD.png')
    forward_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\FORWARD.png')
    play_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\PLAY.png')
    pause_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\PAUSE.png')
    stop_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\STOP.png')
    vol_increase_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\VOL_UP.png')
    vol_decrease_btn_img = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\VOL_DOWN.png')

    # Create Player Control Buttons
    back_button = Button(controls_frame, image = back_btn_img, borderwidth = 0, command = previous_song)
    forward_button = Button(controls_frame, image = forward_btn_img, borderwidth = 0, command = next_song)
    play_button = Button(controls_frame, image = play_btn_img, borderwidth = 0, command = play)
    pause_button = Button(controls_frame, image = pause_btn_img, borderwidth = 0, command =lambda: pause(paused))
    stop_button = Button(controls_frame, image = stop_btn_img, borderwidth = 0, command = stop)
    vol_increase_button = Button(controls_frame, image = vol_increase_btn_img, borderwidth = 0, command = vol_up)
    vol_decrease_button = Button(controls_frame, image = vol_decrease_btn_img, borderwidth = 0, command = vol_down)

    back_button.grid(row=0, column=0, padx=20)
    forward_button.grid(row=0, column=1, padx=20)
    play_button.grid(row=0, column=2, padx=20)
    pause_button.grid(row=0, column=3, padx=20)
    stop_button.grid(row=0, column=4, padx=20)
    vol_increase_button.grid(row=0, column=5, padx=20)
    vol_decrease_button.grid(row=0, column=6, padx=20)

    # PROGRESS BAR VOLUME

    ProgressbarLabel = Label(master_frame, text="", bg="red")
    ProgressbarLabel.grid(row=0, column=1, rowspan=1, padx=25, pady=0)

    ProgressbarVolume = Progressbar(ProgressbarLabel, orient=VERTICAL, mode="determinate", value=100, length=150)
    ProgressbarVolume.grid(row=0, column=0, ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel, text="100%", bg="red", width=3)
    ProgressbarVolumeLabel.grid(row=0, column=0)

    # PROGRESS BAR MUSIC

    ProgressbarMusicLabel = Label(controls_frame, text='', bg="red")
    ProgressbarMusicLabel.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

    ProgressbarMusic_START_Label = Label(ProgressbarMusicLabel, text='00:00', bg="red")
    ProgressbarMusic_START_Label.grid(row=0, column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel, orient=HORIZONTAL, mode="determinate", value = 0)
    ProgressbarMusic.grid(row=0, column=1, ipadx=240, ipady=5)

    ProgressbarMusic_END_Label = Label(ProgressbarMusicLabel, text='00:00', bg="red")
    ProgressbarMusic_END_Label.grid(row=0, column=2)

    # Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # ABOUT MENU
    about_menu = Menu(my_menu)
    my_menu.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="This is a music player, build using Python & Tkinter by Team Soundzonix")

    # ADD SONG MENU
    add_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
    add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
    add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

    # DELETE SONG MENU
    remove_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
    remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
    remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

    # Create Status Bar
    status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=2)

    root.mainloop()

###############################################################################

def mp4():

    Video1 = Toplevel(Home_Page)

    Video1.title("MP4 Player")
    Video1.geometry("150x100+400-300")
    Video1.resizable(False, False)
    Video1.iconbitmap(r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\icon_3.ico')

    bg = PhotoImage(file=r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\1.png')

    intro = Label(Video1, image =bg)
    intro.place(x=0, y=0, relwidth=1, relheight=1, )

    Select_Video = Button(Video1, text="Select Your Video", command=add_video, font=("Impact",12),fg="white", bg="black")
    Select_Video.place(x = 10, y = 30)

    Video1.mainloop()

    ###############################################################################

def add_video():

    video11 = filedialog.askopenfilename(initialdir=r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\video', title="Choose A Video", filetypes=(("mp4 Files", "*.mp4"),))

    vidPath = video11
    # print(vidPath)

    window = pyglet.window.Window(fullscreen=True)
    player = pyglet.media.Player()

    MediaLoad = pyglet.media.load(vidPath)

    player.queue(MediaLoad)
    player.play()

    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(50, 50)

    pyglet.app.run()

###############################################################################

Home_Page = Tk()
Home_Page.title("Main Menu")
Home_Page.geometry("600x600+330-50")
Home_Page.resizable(False, False)
Home_Page.iconbitmap(r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\icon_3.ico')

bg = PhotoImage(file = r'C:\Users\Pransh Gupta\Downloads\CSE PROJECT\GUI\images\6.png')

intro = Label(Home_Page, image=bg)
intro.place(x = 0,y = 0, relwidth = 1, relheight = 1)

my_text = Label(Home_Page, text="Welcome to Soundzie", font=("Impact",40),fg="white", bg="black")
my_text.pack(pady=10)

btn1 = Button(Home_Page, text="Open MP3", command=mp3, font = ("Impact",12),fg="white", bg="black")
btn1.place(x = 265, y = 360)

btn2 = Button(Home_Page, text="Open MP4", command=mp4, font = ("Impact",12),fg="white", bg="black")
btn2.place(x = 265, y = 260)

btn3 = Button(Home_Page, text="Play Games", command=Select_game, font = ("Impact",12),fg="white", bg="black")
btn3.place(x = 264, y = 460)

mainloop()


