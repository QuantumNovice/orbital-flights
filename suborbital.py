

# overload this
def stage():
    pass

def get_apoapsis():
    pass

def fire():
    pass


throttle = 1

thrust = (90, 90)

apoapsis = get_apoapsis()

velocity = get_velocity()

# really basic hard coded track.
while apoapsis > 100000:

    if max_thrust = 0:
        stage()
        fire()

    if velocity.mag < 100:
        thrust = (90, 70)

    velocity_intercepts = range(100, 801, 100)
    gimball_track = [80, 70, 60, 50, 40, 30, 20, 10]
    for idx,i in enumerate(velocity_intercepts):
        try:
            if velocity.mag >= velocity_intercepts[idx] and velocity.mag < velocity_intercepts[idx]:
                thrust = (90, 70)
        except IndexError:
            pass
        
  
    
