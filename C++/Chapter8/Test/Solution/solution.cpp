#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <limits>
#include <chrono>
#include <vector>

#include "../Vector3D/Vector3D.h"

using namespace std;
using namespace std::chrono;

struct Sphere {
    Point3D center;
    double radius;
    Color albedo;
    string material;
};

struct Ray {
    Point3D origin;
    Vector3D direction;
    Sphere closestSphere;
    double distanceToClosestSphere = std::numeric_limits<double>::max();
};

double hitSphere(const Ray &ray, const Sphere &sphere) {
    const Vector3D aMinusC = ray.origin - sphere.center;
    const auto a = ray.direction.dot(ray.direction);
    const auto b = 2.0 * aMinusC.dot(ray.direction);
    const auto c = aMinusC.dot(aMinusC) - sphere.radius * sphere.radius;
    const auto discriminant = b * b - 4 * a * c;
    const auto t = (-b - sqrt(discriminant)) / (2 * a);
    if (discriminant > 0 && t > 0) {
        return t;
    } else {
        throw "Ray Missed Sphere!"s;
    }
}

Ray determineBounceRay(const Ray &ray, const Sphere &sphere) {
    const double t = hitSphere(ray, sphere);
    const Vector3D P = ray.origin + t * ray.direction;
    const Vector3D N = (P - sphere.center) / sphere.radius;
    Vector3D bounce;
    if (sphere.material == "diffuse") {
        bounce = N + makeRandomUnitVector();
    } else if (sphere.material == "metal") {
        bounce = ray.direction - 2 * ray.direction.dot(N) * N;
    } else if (sphere.material == "glass") {
        const auto perpedicularBounce = 1.5 * (ray.direction + -ray.direction.dot(N) * N);
        bounce = perpedicularBounce + -sqrt(abs(1 - perpedicularBounce.length() * perpedicularBounce.length())) * N;
    } else if(sphere.material == "light") {
        throw "Light"s;
    } else {
        throw "Unrecognized Material"s;
    }
    return {P + bounce.normalize() * 0.01, bounce.normalize()};
}

Color calculatePixelColor(Ray ray, const vector<Sphere> &spheres, int depth=10) {
    Ray bounce;
    bool hitOnThisBounce = false;
    for (const auto &sphere : spheres) {
        try {
            Ray possibleBounce = determineBounceRay(ray, sphere);
            const double distanceToHit = (possibleBounce.origin - ray.origin).length();
            if (distanceToHit < ray.distanceToClosestSphere) {
                ray.closestSphere = sphere;
                ray.distanceToClosestSphere = distanceToHit;
                bounce = possibleBounce;
            }
            hitOnThisBounce = true;
        } catch(const string &s) {
            if (s == "Light") {
                return sphere.albedo / 255;
            } else {
                continue;
            }
        } 
    }
    if (depth >= 0 && hitOnThisBounce) {
        return ray.closestSphere.albedo / 255 * calculatePixelColor(bounce, spheres, depth - 1);
    } 
    return { 0, 0, 0 };
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
    double samples;
    vector<Sphere> spheres;

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
        } else if (token == "samples") {
            getline(lineReader, token, ' '); 
            samples = stod(token);
        } else if (token == "sphere") {
            getline(lineReader, token, ' '); const double x = stod(token);
            getline(lineReader, token, ' '); const double y = stod(token);
            getline(lineReader, token, ' '); const double z = stod(token);
            getline(lineReader, token, ' '); const double radius = stod(token);
            getline(lineReader, token, ' '); const double r = stod(token);
            getline(lineReader, token, ' '); const double g = stod(token);
            getline(lineReader, token, ' '); const double b = stod(token);
            getline(lineReader, token, ' '); const string material = token;
            spheres.push_back({{x, y, z}, radius, {r, g, b}, material});
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

    auto start = high_resolution_clock::now();
    double currentPercentCompleted = 0;

    for(double i = 0; i < imageHeight; i++) {
        for(double j = 0; j < imageWidth; j++) {
            
            // Calculate Ray
            const auto u = j / imageWidth;
            const auto v = i / imageHeight;

            const Point3D rayOrigin = eye;
            const Point3D spotOnVirtualViewport = topLeftCorner + u * horizontal - v * vertical;
            const Vector3D rayDirection = spotOnVirtualViewport - eye;
            Ray ray = { spotOnVirtualViewport, rayDirection.normalize() };
            
            // Calculate Color
            Color color = {0, 0, 0};
            for (int k = 0; k < samples; k++) {
                color += calculatePixelColor(ray, spheres);
            }
            color /= samples;
            color *= 255;

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

        auto percentComplete = (static_cast<double>(i) / imageHeight) * 100;

        if (percentComplete > currentPercentCompleted)
        {
            currentPercentCompleted = percentComplete;

            auto currentTime = high_resolution_clock::now();
            auto durationInSeconds = duration_cast<seconds>(currentTime - start).count();
            auto timeRemaining = (durationInSeconds / percentComplete) * (100 - percentComplete);

            cout << '\r' << static_cast<int>(floor(percentComplete)) << "% complete.";
            cout << " Estimated Time Remaining: " << timeRemaining << " seconds. " << flush;
        }
    }

    cout << '\r' << "\t\t\t\t\t\t\t\t" << '\r';

    auto stop = high_resolution_clock::now();
    auto durationInSeconds = duration_cast<seconds>(stop - start).count();

    cout << "100% Complete. Ray Tracer ran in " << durationInSeconds << " seconds." << '\n';
    
    return 0;
}

