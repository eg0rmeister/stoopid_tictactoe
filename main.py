import pygame
import tictactoe
import math

def draw_cross(screen, pos, width, length):
    pygame.draw.line(screen,
                    (255, 0, 0),
                   (pos[0] - length/2, pos[1] - length/2),
                   (pos[0] + length/2, pos[1] + length/2),
                   width)

    pygame.draw.line(screen,
                    (255, 0, 0),
                   (pos[0] + length/2, pos[1] - length/2),
                   (pos[0] - length/2, pos[1] + length/2),
                   width)

pygame.font.init()

pygame.init()




board_size = 600
size = 4#Вот это значение - размер доски
a = 1
screen = pygame.display.set_mode((board_size, board_size))
screen.fill((255, 255, 255))
pygame.Surface.blit(screen, pygame.font.SysFont("Comic Sans", 40).render("wanna play first?", True, (0,0,0)), (board_size/2-100, board_size/4))
pygame.Surface.blit(screen, pygame.font.SysFont("Comic Sans", 40).render("yes", True, (0,255,0)), (board_size/4, board_size/2))
pygame.Surface.blit(screen, pygame.font.SysFont("Comic Sans", 40).render("no", True, (255,0,0)), (board_size*3/4, board_size/2))
pygame.draw.line(screen, (0, 0, 0), (board_size/2, board_size/4+50), (board_size/2, board_size), 3)
pygame.draw.line(screen, (0, 0, 0), (0, board_size/4+50), (board_size, board_size/4+50), 3)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            a = math.ceil(event.pos[0]*2/board_size) - 1




screen.fill((255, 255, 255))
for i in range(1, size):
    pygame.draw.line(screen, (0,0,0), (0, i*board_size/size), (board_size, i*board_size/size), 3)
    pygame.draw.line(screen, (0,0,0), (i*board_size/size, 0), (i*board_size/size, board_size), 3)





# Variable to keep the main loop running
running = True
tictac = tictactoe.TicTacToe(size, memory_filename="mem4.txt")

try:
    tictac.remember()
    print("ss")
except tictactoe.NoMemoryError:
    tictac.memorize_to_file()

if a == 1:
    a = tictac.do_turn()
    pygame.draw.circle(screen, (0,0, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-10)
    pygame.draw.circle(screen, (255, 255, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-20)


# Main loop
pygame.display.flip()
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            i, j = (math.floor(_*size/board_size) for _ in event.pos)
            print(i, j)
            if tictac.player_turn(j, i):
                draw_cross(screen, ((i+1)*board_size/size-board_size/(2*size), (j+1)*board_size/size-board_size/(2*size)), 5, board_size/size-10)
            else:
                continue
            a = tictac.do_turn()
            if tictac.check_win() != 0 and not isinstance(a, int):
                pygame.draw.circle(screen, (0,0, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-10)
                pygame.draw.circle(screen, (255, 255, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-20)
                pygame.display.flip()
                a = tictac.check_win()
            if not a:
                print("bad")
                a = tictac.do_bad_move()
                if not a:
                    print("draw")
                    running = False
                    break
            elif isinstance(a, int):
                print(a, "won")
                running = False
                break
            if tictac.detect_draw():
                print("draw")
                pygame.draw.circle(screen, (0,0, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-10)
                pygame.draw.circle(screen, (255, 255, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-20)
                pygame.display.flip()
                
                running = False
                break
            pygame.draw.circle(screen, (0,0, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-10)
            pygame.draw.circle(screen, (255, 255, 255), ((a[1]+1)*board_size/size-board_size/(2*size), (a[2]+1)*board_size/size-board_size/(2*size)), board_size/(2*size)-20)
    pygame.display.flip()

a = tictac.how_did_win()
if a:
    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        ((a[0][0]+1)*board_size/size-board_size/(2*size), (a[0][1]+1)*board_size/size-board_size/(2*size)),
                        ((a[1][0]+1)*board_size/size-board_size/(2*size), (a[1][1]+1)*board_size/size-board_size/(2*size)),
                        3
                    )
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False