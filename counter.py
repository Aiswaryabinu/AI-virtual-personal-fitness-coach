import numpy as np

def calculate_angle(a, b, c):
    """Calculates angle (in degrees) between three 3D points using vector math:
# 1. Converts points to vectors AB and BC
# 2. Computes dot product and magnitudes
# 3. Applies cosine rule: cosθ = (AB·BC) / (|AB||BC|)
# 4. Uses arccos to get angle, then converts to degrees
"""
    A = np.array(a)
    B = np.array(b)
    C = np.array(c)
    vector_ba = B - A
    vector_bc = B - C
    dot_product = np.dot(vector_ba, vector_bc)
    magnitude_ba = np.linalg.norm(vector_ba)
    magnitude_bc = np.linalg.norm(vector_bc)
    cosine_angle = dot_product / (magnitude_ba * magnitude_bc)
    angle_radians = np.arccos(cosine_angle)  # arccos: inverse cosine function
    degrees = np.degrees(angle_radians)
    return degrees

def track_pose(degrees):
    """# Track movement stage and count repetitions:
# - If the angle exceeds the upper threshold (e.g., arm extended), set stage to "up"
# - If the angle drops below the lower threshold (e.g., arm contracted) 
#   and the previous stage was "up", set stage to "down" and increment the rep counter
"""
    if degrees > 160:
        stage = "up"
    if degrees < 50 and stage == "up":
        stage = "down"
        counter += 1
    return counter, stage

def count_reps(counter,degrees,stage):
    """Counts repetitions based on angle thresholds:
    - If angle > 160, set stage to "down" 
    - If angle < 50 and stage is "down", set stage to "up" and increment counter
    """  
    if degrees > 160:
        stage = "down"
    if degrees < 50 and stage == "down":
        stage = "up"
        counter += 1
    return counter, stage 


      
                       