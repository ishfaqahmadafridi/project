import pygame    # type: ignore
import os




pygame.init()

def play_music(file):
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

def stop_music():
  pygame.mixer.music.stop()

def pause_music():
  pygame.mixer.music.pause()

def resume_music():
  pygame.mixer.music.unpause()

def main():
  music_file="Music.mp3"

  if not os.path.exists(music_file):
    print("music file is not found! ")
    return
  
  print("WELCOME TO THE PYTHON MUSIC PLAYER! ")
  print("commands:PLAY,PAUSE,RESUME,STOP,EXIT")


  while True:
    command= input("ENTER COMMAND : ").strip().lower()
    
    if command == "play":
      play_music(music_file)
      print("PLAYING MUSIC...")
    elif command == "stop":
      stop_music()
      print("MUSIC IS STOP")
    
    elif command == "pause":
      pause_music()
      print("MUSIC IS PAUSE")
    
    elif command == "resume":
      resume_music()
      print("MUSIC IS RESUME")
    
    elif command == "exist":
      stop_music()
      print("EXITING music player. GOODBYE! ")
      break
    else:
      print("invalid command . try again.")


if __name__ == "_main_":
  main()
