from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0, 0, 0, 0)

    gluPerspective(60,1,.1,50)
    gluLookAt(20,20,20,0,0,0,0,1,0)
    glClear(GL_COLOR_BUFFER_BIT)
def oneCube(N,x,y,z,w,t,u):

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScale( x , y , z)
    glTranslate(w,t,u)
    glutWireCube(N)
def Chair ():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor(1, 1, 1)
#1st Char
    oneCube(4,1,1.5,0.25,2.55,4,0)
    oneCube(4, 1, 0.25, 1,3.1,12,2.1)
    oneCube(4, 0.125, -1.6, 0.125, 38, 0.5, 2.1)
    oneCube(4, 0.125, -1.6, 0.125, 38, 0.5, 30)
    oneCube(4, 0.125, -1.6, 0.125, 10, 0.5, 30)
    oneCube(4, 0.125, -1.6, 0.125, 10, 0.5, 2.1)
#2nd Char
    oneCube(4, 1, 1.5, 0.25, -6.55, 4, 0)
    oneCube(4, 1, 0.25, 1, -5.9, 12, 2.1)
    oneCube(4, 0.125, -1.6, 0.125, -34, 0.5, 2.1)
    oneCube(4, 0.125, -1.6, 0.125, -34, 0.5, 30)
    oneCube(4, 0.125, -1.6, 0.125, -62, 0.5, 30)
    oneCube(4, 0.125, -1.6, 0.125, -62, 0.5, 2.1)



    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(800, 800)
glutCreateWindow(b"Chair")
myInit()
glutDisplayFunc(Chair)
glutMainLoop()
