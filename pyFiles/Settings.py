from screeninfo import get_monitors

#k = 0
def get_monitor_dimensions():
    j = 0#k%2
    monitors = get_monitors()
    for monitor in monitors:
        print(f"Monitor: {monitor.name}")
        print(f"Width: {monitor.width} pixels")
        print(f"Height: {monitor.height} pixels")
        print(f"Width: {monitor.width_mm} mm")
        print(f"Height: {monitor.height_mm} mm")
        print()
        
        a, b =  monitors[j].width_mm*.254, monitors[j].height_mm*.254
        #k += 1
        return a, b

dims = get_monitor_dimensions()

class settings():
    window_width = dims[0]
    window_height = dims[1]
    linewidth = 2
    steps = 10000#can be reduced to 1000
    xmin = -10
    xmax = 10
    ymin = xmin*window_height/window_width
    ymax = xmax*window_height/window_width
    #ymax = 10
    azure = '#006d77'
