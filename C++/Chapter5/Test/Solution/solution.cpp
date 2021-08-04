#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

#include "../Vector3D/Vector3D.h"

using namespace std;

Color calculatePixelColor(const Point3D &rayOrigin, const Vector3D &rayDirection) {
    double r = abs(rayDirection[0]) * 255 - 50;
    double g = abs(rayDirection[1]) * 255 - 50;
    double b = abs(rayDirection[2]) * 255 - 50;

    return { r, g, b };
}

int main(int argc, char** argv) {
    
    if(argc != 3) {
        cerr << "Usage: ./a.out" << " " << "[Driver File]" << " " << "[Output File]" << '\n';
        return 1;
    }

    // Read Driver File

    ifstream driverReader(argv[1]);

    if (!driverReader) {
        string err = strerror(errno);
        cerr << "Failure to open Driver File - " << argv[1] << ": " << err << '\n';
        return 1;
    }
    
    int imageWidth;
    double aspectRatio;
    Vector3D eye;
    int viewportWidth;
    double focalLength;

    for (string driverLine, token; getline(driverReader, driverLine);) {
        driverLine.erase(remove(driverLine.begin(), driverLine.end(), '\r'), driverLine.end());
        if(driverLine.empty()) continue;
        
        stringstream lineReader(driverLine);
        getline(lineReader, token, ' ');

        if (token == "imageWidth") {
            getline(lineReader, token, ' ');
            imageWidth = stoi(token);
        } else if (token == "aspectRatio") {
            getline(lineReader, token, ' '); const double widthRatio = stod(token);
            getline(lineReader, token, ' '); const double heightRatio = stod(token);
            aspectRatio = heightRatio / widthRatio;
        } else if (token == "eye") {
            getline(lineReader, token, ' '); const double x = stod(token);
            getline(lineReader, token, ' '); const double y = stod(token);
            getline(lineReader, token, ' '); const double z = stod(token);
            eye = { x, y, z };
        } else if (token == "viewportWidth") {
            getline(lineReader, token, ' ');
            viewportWidth = stoi(token);
        } else if (token == "focalLength") {
            getline(lineReader, token, ' ');
            focalLength = stod(token);
        } else if (token == "#" || token[0] == '#') {
            continue;
        }
    }

    // Output Image

    ofstream outWriter(argv[2]);

    if (!outWriter) {
        string err = strerror(errno);
        cerr << "Failure to open Output File - " << argv[2] << ": " << err << '\n';
        return 1;
    }
    
    const int imageHeight = imageWidth * aspectRatio;
    const double viewportHeight = viewportWidth * aspectRatio;

    const Vector3D horizontal = { static_cast<double>(viewportWidth), 0, 0 };
    const Vector3D vertical = { 0, viewportHeight, 0 };
    const Vector3D distance = { 0, 0, focalLength };
    const Point3D topLeftCorner = eye - horizontal / 2 + vertical / 2 - distance;
    
    outWriter << "P3" << '\n';
    outWriter << imageWidth << " " << imageHeight << " " << 255 << '\n';

    for(double i = 0; i < imageHeight; i++) {
        for(double j = 0; j < imageWidth; j++) {
            // Calculate Ray
            const auto u = j / imageWidth;
            const auto v = i / imageHeight;

            const Point3D rayOrigin = eye;
            const Vector3D rayDirection = (topLeftCorner + u * horizontal - v * vertical - eye).normalize();

            // Calculate Color
            Color color = calculatePixelColor(rayOrigin, rayDirection);
            
            // Write Color
            if (color[0] < 0) color[0] = 0;
            if (color[1] < 0) color[1] = 0;
            if (color[2] < 0) color[2] = 0;
    
            if (color[0] > 255) color[0] = 255;
            if (color[1] > 255) color[1] = 255;
            if (color[2] > 255) color[2] = 255;

            outWriter << static_cast<int>(color[0]) << " " 
                      << static_cast<int>(color[1]) << " " 
                      << static_cast<int>(color[2]);

            if(j < imageWidth - 1) {
                outWriter << " ";
            } else {
                outWriter << '\n';
            }
        }
    }
    
    return 0;
}
