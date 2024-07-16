import re
import sys

def extract_geometry_coordinates(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)  # Debugging: Print the content of the file

            # Use regular expressions to find the geometry coordinates
            pattern = r'Standard orientation:(.*?)--\n'
            matches = re.findall(pattern, content, re.DOTALL)
            print("Matches:")
            print(matches)  # Debugging: Print the matches found

            geometry_coordinates = []

            for match in matches:
                lines = match.strip().split('\n')[5:]  # Skip the header lines
                coordinates = []
                for line in lines:
                    parts = line.split()
                    atom = parts[1]
                    x, y, z = map(float, parts[3:6])
                    coordinates.append((atom, x, y, z))
                geometry_coordinates.append(coordinates)

            return geometry_coordinates

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_geometry.py <Gaussian_output_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    geometry_coordinates = extract_geometry_coordinates(file_path)

    if geometry_coordinates:
        for idx, geometry in enumerate(geometry_coordinates):
            print(f"Geometry {idx + 1}:")
            for atom, x, y, z in geometry:
                print(f"{atom}: ({x}, {y}, {z})")
            print()
