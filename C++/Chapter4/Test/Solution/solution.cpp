#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

#include "../Vector3D/Vector3D.h"

using namespace std;

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

    for (string driverLine; getline(driverReader, driverLine);) {
        driverLine.erase(remove(driverLine.begin(), driverLine.end(), '\r'), driverLine.end());
        if(driverLine.empty()) {
            continue;
        }
        stringstream lineReader(driverLine);
        string token;

        getline(lineReader, token, ' ');

        if (token == "imageWidth") {
            getline(lineReader, token, ' ');
            imageWidth = stoi(token);
        } else if (token == "aspectRatio") {
            getline(lineReader, token, ' '); double widthRatio = stod(token);
            getline(lineReader, token, ' '); double heightRatio = stod(token);
            aspectRatio = heightRatio / widthRatio;
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

    outWriter << "P3" << '\n';
    outWriter << imageWidth << " " << imageHeight << " " << 255 << '\n';

    for(double i = 0; i < imageHeight; i++) {
        for(double j = 0; j < imageWidth; j++) {
            outWriter << static_cast<int>(i / imageHeight * 255) << " ";
            outWriter << static_cast<int>(j / imageWidth * 255) << " ";
            outWriter << 64;
            if(j < imageWidth - 1) {
                outWriter << " ";
            } else {
                outWriter << '\n';
            }
        }
    }
    
    return 0;
}
