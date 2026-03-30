import math
arena_width = 800
arena_height = 600

ship_x = arena_width / 2
ship_y = arena_height / 2
ship_speed_x = 0
ship_speed_y = 0
ship_angle = 0
def update(dt):
    global ship_x
    global ship_y
    global ship_speed_x
    global ship_speed_y
    global ship_angle

    turn_speed = 10

    if keyboard.right:
        ship_angle += turn_speed * dt

    if keyboard.left:
        ship_angle -= turn_speed * dt
    # etc.
    if keyboard.up:
        ship_speed = 100
        ship_speed_x += math.cos(ship_angle) * ship_speed * dt
        ship_speed_y += math.sin(ship_angle) * ship_speed * dt
    ship_x += ship_speed_x * dt
    ship_y += ship_speed_y * dt
    for bullet in bullets.copy():
        bullet['time_left'] -= dt

        if bullet['time_left'] <= 0:
            bullets.remove(bullet)
            continue
        bullet_speed = 500
        bullet['x'] += math.cos(bullet['angle']) * bullet_speed * dt
        bullet['y'] += math.sin(bullet['angle']) * bullet_speed * dt
        bullet['x'] %= arena_width
        bullet['y'] %= arena_height
    ship_x %= arena_width
    ship_y %= arena_height
    
    ship_angle %= 2 * math.pi
    
def draw():
    screen.fill((0, 0, 0))
    for y in range(-1, 2):
        for x in range(-1, 2):
            offset_x = x * arena_width
            offset_y = y * arena_height

            screen.draw.filled_circle(
                (ship_x + offset_x, ship_y + offset_y),
                30, color=(0, 0, 255)
            )

            ship_circle_distance = 20
            screen.draw.filled_circle((
                ship_x + offset_x +
                    math.cos(ship_angle) * ship_circle_distance,
                ship_y + offset_y +
                    math.sin(ship_angle) * ship_circle_distance),
                5, color=(0, 255, 255)
            )

    screen.draw.text(
        'ship_angle: ' + str(ship_angle) + '\n' +
        'ship_x: ' + str(ship_x) + '\n' +
        'ship_y: ' + str(ship_y) + '\n' +
        'ship_speed_x: ' + str(ship_speed_x) + '\n' +
        'ship_speed_y: ' + str(ship_speed_y),
    (0, 0))
    # Temporary
    screen.draw.text('ship_angle: ' + str(ship_angle), (0, 0))

bullets = []
ship_radius = 30

def on_key_down(key):
    if key == keys.S:
        bullets.append({
            'x': ship_x + math.cos(ship_angle) * ship_radius,
            'y': ship_y + math.sin(ship_angle) * ship_radius,
            'angle': ship_angle,
        })

def draw():
    screen.fill((0, 0, 0))

    for y in range(-1, 2):
        for x in range(-1, 2):

            # etc.
            screen.draw.filled_circle(
                (ship_x + offset_x, ship_y + offset_y),
                ship_radius, color=(0, 0, 255)
            )

            for bullet in bullets:
                screen.draw.filled_circle(
                    (bullet['x'] + offset_x, bullet['y'] + offset_y),
                    5, color=(0, 255, 0)
                )