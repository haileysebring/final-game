# final-game

  # Frog Adventure Game
  
  ## Overview
  
  Welcome to the Frog Adventure Game! This is a fun and interactive 2D game where you control a frog, catch flies, and try to score as many points as possible before the time runs out. The game is developed using Python and `pygame`.
  
  ## Features
  
  - Different game states: Intro, Gameplay, Pause, Quit
  - User-controlled frog character
  - Multiple computer-controlled flies
  - Collision detection and score tracking
  - Background music and sound effects
  
  ## Prerequisites
  
  - **Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
  - **pygame**: Install the `pygame` library using pip:
  
    ```bash
    pip install pygame


Pseudo-Code
  Initialize pygame
  Load images and sounds
  Start background music

  Define game states: INTRO, GAMEPLAY, PAUSE, QUIT
  Define fonts and colors
  
  Define Frog class (inherits pygame.sprite.Sprite)
      Initialize with image and starting position
      Define update method to handle rotation and movement
  
  Define Fly class (inherits pygame.sprite.Sprite)
      Initialize with image, random position, and random angle
      Define update method to handle movement and random rotation
  
  Define Game class
      Initialize game state, create Frog and Fly objects, create sprite groups, set score and timer
      Define reset method to reinitialize game state
      Define draw_intro method to display the intro screen
      Define draw_gameplay method to display the gameplay screen
      Define draw_pause method to display the pause screen
      Define check_collisions method to handle frog-fly collisions
      Define update_timer method to decrement the timer
      Define run method to start the game loop
  
  In main block
      Create Game object
      Call run method of Game object

Assets
  Images
  forest_background.png (background image)
  frog.png (frog character)
  fly.png (fly character)
  Sounds
  ribbet.wav (sound when frog catches a fly)
  background_music.wav (background music)
