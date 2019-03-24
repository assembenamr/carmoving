from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle=0
x=0
right = True
def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
              0,0,0,
             0,1,0)
    glClearColor(0,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)

def linesxyz():
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    glVertex(-10, 0, 0)
    glVertex(10, 0, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex(0, 10, 0)
    glVertex(0, -10, 0)
    glEnd()
    glBegin(GL_LINES)
    #glColor3f(1, 0, 0)
    glVertex(0, 0, 10)
    glVertex(0, 0, -10)
    glEnd()


    glFlush()

def drawother ():
    glColor3f(.8,.9,.9)
    glLoadIdentity()

    glTranslate(3, 0, -14)
    glScale(10,.5,1)
    glutSolidCube(3)
    glFlush()

    glColor3f(.8, 0.9, 0.9)
    glLoadIdentity()

    glTranslate(3, 0, 9)
    glScale(8, 1, 5)
    glutSolidCube(2)
    glFlush()




    glLoadIdentity()
    glColor3f(1,1,.1)
    #glutSolidSphere(2,2,2)
    glFlush()







def draw():
    global angle
    global x
    global right




    #glTranslate(x, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0,0,0,1)


    glClear(GL_COLOR_BUFFER_BIT)




    glLoadIdentity()
    glColor3f(.2,.2 ,.3 )
    glTranslate(1, 0, 0)
    glScale(5, .01, 4)
    glutSolidCube(6)
    glFlush()

    glColor3f(0,1,1)

    #linesxyz()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, 0, 0)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(4, 0, -5)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-4, 0, -5)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()


    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(1,1,.1)
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glTranslate(0,5*0.25,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x, 0, 0)
    glColor3f(0,0,1)
    glTranslate(5*0.5,-5*0.25*0.5,0.5*5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125,.5,12,10)

    glLoadIdentity()
    glTranslate(x-5*0.5,-5*.25*.5,0.5*5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125,.5,12,10)

    glLoadIdentity()
    #glTranslate(x-5*.5, -5*.5*.25, -5*.5*.5)
    #glRotate(angle, 0, 0, 1)
    #glutWireTorus(.125, .5, 12, 10)


    glLoadIdentity()
    glTranslate(x+5 * 0.5, -5 * 0.25 * 0.5, -0.5 * 5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)
    ##################################3333
    #############################################33
    ########anothercar
    glLoadIdentity()
    glColor3f(.2,.1 ,.4 )
    glTranslate(-x, 0, 0-5)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(.4, .1, .2)
    glLoadIdentity()
    glTranslate(-x, 0, 0)
    glTranslate(0, 5 * 0.25, 0-5)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(-x, 0, 0)
    glColor3f(0, 0, 1)
    glTranslate(5 * 0.5, -5 * 0.25 * 0.5, (0.5 * 5 * 0.5)-5)
    glRotate(-angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)

    glLoadIdentity()
    glTranslate(-x - 5 * 0.5, -5 * .25 * .5, (0.5 * 5 * .5)-5)
    glRotate(-angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)

    glLoadIdentity()
    #glTranslate(-x-5*.5, -5*.5*.25, (-5*.5*.5)-5)
    #glRotate(-angle, 0, 0, 1)
    #glutWireTorus(.125, .5, 12, 10)

    glLoadIdentity()
    glTranslate(-x + 5 * 0.5, -5 * 0.25 * 0.5, (-0.5 * 5 * 0.5)-5)
    glRotate(-angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)





    drawother()


    glutSwapBuffers()

    if right :
       angle-=1
       x+=.02
       if x>5:
           right=False
    else:
        angle+=1
        x-=.02
        if x < -5:
           right = True





    drawother()






glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"movingcar")
myinit()
glutIdleFunc(draw)
glutDisplayFunc(draw)
glutMainLoop()