import math
import matplotlib.pyplot as plt

def vertical_lines_in_circle(radius, center, num_lines, inner_radius=290):
    # Unpack the center coordinates
    x_center, y_center = center
    
    # Calculate the angle step
    angle_step = 2 * math.pi / num_lines
    
    # Initialize the list of lines and angles
    lines = []
    angles = []
    
    # Generate the lines
    for i in range(num_lines):
        angle = i * angle_step
        x1 = x_center + radius * math.cos(angle)
        x2 = x_center + inner_radius * math.cos(angle)
        y1 = y_center + radius * math.sin(angle)
        y2 = y_center + inner_radius * math.sin(angle)
        lines.append((x1, x2, y1, y2))
        angles.append(math.degrees(angle))
        
    # Return the lines and angles,
    return lines, angles

if __name__ == "__main__":
    # Generate the lines and angles
    lines, angles = vertical_lines_in_circle(491, (599.494, 515.964), 500, 290)
    
    # Plot the lines
    for line in lines:
        x1, x2, y1, y2 = line
        plt.plot([x1, x2], [y1, y2], 'k-')
    
    # Set aspect ratio to equal and show the plot
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
    # Print the line angles
    print("Line angles (in degrees):", angles)