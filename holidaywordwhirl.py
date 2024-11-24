import pygame, random, sys, os

os.chdir('/Users/gabelojo/Coding/CICS 110/CICS 110 FINAL PROJECT')

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 800

words = [
    'christmas', 'bells', 'mistletoe', 'sleigh', 'snow', 'wreath',
    'festive', 'jolly', 'tree', 'presents', 'ornaments', 'star',
    'spirit', 'carols', 'cocoa', 'cookies', 'winter', 'noel',
    'gloves', 'angel', 'snowman', 'rudolph', 'tinsel', 'frosty',
    'coal', 'toys', 'reindeer', 'holly', 'gingerbread', 'white', 
    'lights', 'chimney', 'fireplace', 'gift', 'elves', 'workshop', 
    'eggnog', 'stocking', 'kringle', 'snowflake', 'partridge', 
    'drummer', 'carriage', 'noel', 'krampus', 
    'celebration', 'peace', 'love', 'family', 'joy', 'magic', 
    'tradition', 'candy', 'feast', 'holiday', 'season', 
    'wrapping', 'sled', 'icicle', 'grinch', 'yule', 'blizzard', 
    'peppermint', 'hearth', 'candles', 'evergreen', 
    'scarf', 'tidings', 'advent', 'greetings', 
    'pine', 'log', 'holidays', 'jingle', 'silver', 
    'blessings', 'family', 'midnight', 'traditions', 'wish', 
    'gold', 'chill', 'snowfall', 'polar', 'crisp', 
    'chestnuts', 'roast', 'bells', 'songs', 'celebrate', 
    'santa', 'chimney', 'chill', 'coat', 'beanie', 'hat', 'cold'
]

pygame.mixer.music.load("wwyamcjazzbackground.mp3") # Load Background Music
pygame.mixer.music.set_volume(1) 

clock = pygame.time.Clock()
fps = 120

instfont = pygame.font.Font("arcadeclassic.ttf", 98)
bigfont = pygame.font.Font("arcadeclassic.ttf", 110)
font = pygame.font.Font("arcadeclassic.ttf", 75)
smallerfont = pygame.font.Font("arcadeclassic.ttf", 55)
smallestfont = pygame.font.Font("arcadeclassic.ttf", 48)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_surface = pygame.Surface((WIDTH, HEIGHT))

pygame.display.set_caption('Holiday Word Whirl')
mainmenu = pygame.image.load("mainmenubackground.jpg")
mainmenu = pygame.transform.scale(mainmenu, (WIDTH, HEIGHT))
background = pygame.image.load("holidaybackground.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
gameover = pygame.image.load("holidaygameover.gif")
gameover = pygame.transform.scale(gameover, (WIDTH, HEIGHT))

word_speed = 1
score = 0
missed_words = 0
max_misses = 5
active_words = []

#colors
white = (255, 255, 255)
black = (0, 0, 0)
darkred = (139, 0, 0)
red = (255, 0, 0)
darkgreen = (0, 139, 0)
green = (0, 255, 0)
lightblue = (0, 122, 193)
darker_lightblue = (20, 100, 160)
navyblue = (0, 0, 130)


def mainmenuscreen(screen): # Main Menu Screen

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(loops = -1)

    run = True
    while run:

        screen.blit(mainmenu, (0, 0))  # Display the background for the main menu

        header = pygame.Rect(300, 50, 620, 210)
        pygame.draw.rect(screen, darkred, header.inflate(6, 6)) 
        pygame.draw.rect(screen, red, (300, 50, 620, 210))
        pygame.draw.rect(screen, darkred, header, 8)
        
        # Title
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = bigfont.render("Ho    iday", True, black)
            screen.blit(outline_surface, (385 + dx, 50 + dy))
        title1 = bigfont.render("Ho    iday", True, white)
        screen.blit(title1, (385, 50))
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = bigfont.render("L", True, black)
            screen.blit(outline_surface, (512 + dx, 50 + dy))
        title1part2 = bigfont.render("L", True, white)
        screen.blit(title1part2, (512, 50)) # Place L separate because font spaces it weirdly
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = bigfont.render("Word  Whirl", True, black)
            screen.blit(outline_surface, (335 + dx, 150 + dy))
        title2 = bigfont.render("Word  Whirl", True, white)
        screen.blit(title2, (335, 150))

        MOUSE_POS = pygame.mouse.get_pos() # Get position of the mouse cursor

        # Start button
        start_button = pygame.Rect(487, 285, 230, 70)
        mouse_over_start = start_button.collidepoint(MOUSE_POS)  # Check if the mouse is over the start button
        # Draw the Start button with a color change on hover
        pygame.draw.rect(screen, darker_lightblue, start_button.inflate(6, 6)) 
        pygame.draw.rect(screen, darker_lightblue if mouse_over_start else lightblue, (487, 287, 230, 66))
        pygame.draw.rect(screen, darker_lightblue, start_button, 5)

        start_text = font.render("START", True, white)
        screen.blit(start_text, (507, 285))

        # Instructions button
        instruct_button = pygame.Rect(352, 400, 520, 70)
        mouse_over_instruct = instruct_button.collidepoint(MOUSE_POS)  # Check if the mouse is over the Instructions button
        # Draw the Instructions button with a color change on hover
        pygame.draw.rect(screen, darker_lightblue, instruct_button.inflate(6, 6)) 
        pygame.draw.rect(screen, darker_lightblue if mouse_over_instruct else lightblue, (352, 402, 520, 66))
        pygame.draw.rect(screen, darker_lightblue, instruct_button, 5)

        instruct_text = font.render("INSTRUCTIONS", True, white)
        screen.blit(instruct_text, (365, 400))

        # Fullscreen button
        fullscreen_button = pygame.Rect(395, 517, 440, 70)
        mouse_over_fullscreen = fullscreen_button.collidepoint(MOUSE_POS)  # Check if the mouse is over the start button
        # Draw the Quit button with a color change on hover
        pygame.draw.rect(screen, darker_lightblue, fullscreen_button.inflate(6, 6)) 
        pygame.draw.rect(screen, darker_lightblue if mouse_over_fullscreen else lightblue, (395, 519, 440, 66))
        pygame.draw.rect(screen, darker_lightblue, fullscreen_button, 5)

        fullscreen_text = font.render("FULLSCREEN", True, white)
        screen.blit(fullscreen_text, (410, 515))

        # Quit button
        quit_button = pygame.Rect(500, 634, 200, 70)
        mouse_over_quit = quit_button.collidepoint(MOUSE_POS)  # Check if the mouse is over the start button
        # Draw the Quit button with a color change on hover
        pygame.draw.rect(screen, darker_lightblue, quit_button.inflate(6, 6)) 
        pygame.draw.rect(screen, darker_lightblue if mouse_over_quit else lightblue, (500, 636, 200, 66))
        pygame.draw.rect(screen, darker_lightblue, quit_button, 5)

        quit_text = font.render("QUIT", True, white)
        screen.blit(quit_text, (523, 632))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if start_button.collidepoint(MOUSE_POS):  # Start button clicked
                    gamescreen(word_speed, score, missed_words, max_misses, active_words)  # Start the game
                    run = False
                elif instruct_button.collidepoint(MOUSE_POS):  # Instructions button clicked
                    instructscreen()  # Go to Instructions
                    run = False
                elif fullscreen_button.collidepoint(MOUSE_POS):  # Fullscreen button clicked
                    # if screen.get_flags() & pygame.FULLSCREEN:  # Check if currently in fullscreen
                    #     screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
                    # else:
                    #     native_width, native_height = pygame.display.Info().current_w, pygame.display.Info().current_h # Get the display's native resolution
                    #     screen = pygame.display.set_mode((native_width, native_height), pygame.FULLSCREEN)
                    return
                elif quit_button.collidepoint(MOUSE_POS):
                    run = False

        pygame.display.update()

def instructscreen():
    run = True
    while run:

        screen.blit(mainmenu, (0, 0))
        scaled_mainmenu = pygame.transform.scale(mainmenu, screen.get_size())
        screen.blit(scaled_mainmenu, (0, 0))

        header = pygame.Rect(15, 120, 1175, 350)
        pygame.draw.rect(screen, darkred, header.inflate(6, 6)) 
        pygame.draw.rect(screen, red, (15, 120, 1175, 350))
        pygame.draw.rect(screen, darkred, header, 8)

        header2 = pygame.Rect(50, 550, 1100, 100)
        pygame.draw.rect(screen, darkgreen, header2.inflate(6, 6)) 
        pygame.draw.rect(screen, green, (50, 550, 1100, 100))
        pygame.draw.rect(screen, darkgreen, header2, 8)

        # Line 1
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = instfont.render("get  the  highest  score", True, black)
            screen.blit(outline_surface, (75 + dx, 150 + dy))
        instructions = instfont.render("get  the  highest  score", True, white)
        screen.blit(instructions, (75, 150))

        # Line 2
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = instfont.render("by  typing  each  word", True, black)
            screen.blit(outline_surface, (135 + dx, 250 + dy))
        instructions = instfont.render("by  typing  each  word", True, white)
        screen.blit(instructions, (135, 250))

        # Line 3
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = instfont.render("that  drops  from  the  top", True, black)
            screen.blit(outline_surface, (35 + dx, 350 + dy))
        instructions = instfont.render("that  drops  from  the  top", True, white)
        screen.blit(instructions, (35, 350))

        # Line 4
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = instfont.render("Color does not matter", True, black)
            screen.blit(outline_surface, (95 + dx, 550 + dy))
        instructions = instfont.render("Color does not matter", True, white)
        screen.blit(instructions, (95, 550))

        MOUSE_POS = pygame.mouse.get_pos()

        back_button = pygame.Rect(1100, 30, 70, 70)
        mouse_over_back = back_button.collidepoint(MOUSE_POS)
        pygame.draw.rect(screen, darkred, back_button.inflate(6, 6))
        pygame.draw.rect(screen, darkred if mouse_over_back else red, (1100, 32, 70, 66))
        pygame.draw.rect(screen, darkred, back_button, 4)
        back_text = font.render("x", True, white)
        screen.blit(back_text, (1115, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if back_button.collidepoint(MOUSE_POS):  # Back button clicked
                    mainmenuscreen(screen)  # Back to main menu
                    run = False

        pygame.display.update()


def gamescreen(word_speed, score, missed_words, max_misses, active_words): # Game Screen
    time = 2250
    pygame.time.set_timer(pygame.USEREVENT, time)
    user_input = ""

    # Countdown
    for x in range(3, 0, -1):
            screen.blit(background, (0, 0))
            for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
                outline_surface = bigfont.render(f"{x}", True, black)
                screen.blit(outline_surface, (590+dx, 355+dy))
            countdown = bigfont.render(f"{x}", True, white)
            screen.blit(countdown, (590, 355))
            pygame.display.update()
            pygame.time.wait(1000)

    run = True
    while run:

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                word = random.choice(words)
                word_length = font.size(word)[0]  # Get the width of the word
                max_x_position = WIDTH - word_length - 50  # Ensure the word fits on the screen
                x_position = random.randint(50, max_x_position)  # Ensure no word is placed off the screen
                color = [red, green, white]
                active_words.append({"word": word, "x": x_position, "y": 0, "color": random.choice(color)})
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isalpha():
                    user_input += event.unicode

        # Move words down
        for word_obj in active_words:
        # Calculate the progress of the word where it is 0 at the top and 1 at the bottom
            progress = word_obj["y"] / HEIGHT
        # Adjust the speed where it isfaster at the top (small progress) and slower at the bottom (large progress)
            dynamic_speed = word_speed * (5 - 4 * progress)
            dynamic_speed = max(dynamic_speed, word_speed * 0.005) #Minimum speed
        # Updating position of word
            word_obj["y"] += dynamic_speed

        # Check for the user input
        for word_obj in active_words[:]:
            if user_input.strip().lower() == word_obj["word"].lower():  
                score += 1
                active_words.remove(word_obj) # Removes the word from the active words list
                user_input = ""

        # Remove words that fall out of the screen
        for word_obj in active_words[:]:
            if word_obj["y"] > HEIGHT:
                active_words.remove(word_obj)
                missed_words += 1
                user_input = ""  # Clear input on miss
                if missed_words >= max_misses:
                    screen.blit(gameover, (0,0))
                    for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
                        outline_surface = font.render("Game Over", True, black)
                        screen.blit(outline_surface, (WIDTH // 2 - 150 + dx, HEIGHT // 2 - 40 + dy))
                    game_over_surface = font.render("Game Over", True, red)
                    for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
                        outline_surface = font.render(f"Final Score {score}", True, black)
                        screen.blit(outline_surface, (WIDTH // 2 - 235 + dx, HEIGHT // 2 + 20 + dy))
                    score_surface = font.render(f"Final Score {score}", True, green)
                    screen.blit(game_over_surface, (WIDTH // 2 - 150, HEIGHT // 2 - 40))
                    screen.blit(score_surface, (WIDTH // 2 - 235, HEIGHT // 2 + 20))
                    pygame.display.update()
                    pygame.time.wait(4000)
                    active_words.clear()
                    word_speed = 1 # Reset Speed
                    score = 0 # Reset Score
                    missed_words = 0 # Reset Misses
                    mainmenuscreen(screen)

        # Increase difficulty over time
        if score > 0:
            word_speed = 1 + (score // 5) * 0.1 # Words speed is faster every 50 points
        if score % 5 == 0:
            time -= 25 # Time between word drops becomes faster every 50 points

        screen.blit(background, (0, 0))

        for word_obj in active_words:
            for dx, dy in [(-5, 0), (5, 0), (5, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
                outline_surface = font.render(word_obj["word"].upper(), True, black)
                screen.blit(outline_surface, (word_obj["x"] + dx, word_obj["y"] + dy)) 

            word_surface = font.render(word_obj["word"].upper(), True, word_obj["color"])
            screen.blit(word_surface, (word_obj["x"], word_obj["y"]))  

        # Display score and missed words
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = smallerfont.render(f"Score  {score}", True, black)
            screen.blit(outline_surface, (485 + dx, 740 + dy))
        score_surface = smallerfont.render(f"Score  {score}", True, white)
        screen.blit(score_surface, (485, 740))

        # Display missed words with black outline
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = smallestfont.render(f"Missed  {missed_words}  out of  {max_misses}", True, black)
            screen.blit(outline_surface, (815 + dx, 745 + dy))
        missed_surface = smallestfont.render(f"Missed  {missed_words}  out of  {max_misses}", True, red)
        screen.blit(missed_surface, (815, 745))

        # Display current input with black outline
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 5), (-5, -5), (5, -5), (-5, 5), (5, 5)]:
            outline_surface = smallestfont.render(f"Typing  {user_input}", True, black)
            screen.blit(outline_surface, (10 + dx, 745 + dy))
        input_surface = smallestfont.render(f"Typing  {user_input}", True, green)
        screen.blit(input_surface, (10, 745))

        pygame.display.update()
        clock.tick(60)
        
mainmenuscreen(screen)
pygame.quit()
sys.exit()