import pyglet
song = pyglet.media.load('/home/pi/Desktop/teste.ogg')
song.play()
pyglet.app.run()