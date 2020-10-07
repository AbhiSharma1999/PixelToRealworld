import numpy as np

quad_coords = {
    "realworld": np.array([
        [6.602018, 52.036769], # Third lampost top right
        [6.603227, 52.036181], # Corner of white rumble strip top left
        [6.603638, 52.036558], # Corner of rectangular road marking bottom left
        [6.603560, 52.036730] # Corner of dashed line bottom right
    ]),
    "pixel": np.array([
        [1200, 278], # Third lampost top right
        [87, 328], # Corner of white rumble strip top left
        [36, 583], # Corner of rectangular road marking bottom left
        [1205, 698] # Corner of dashed line bottom right
    ])
}