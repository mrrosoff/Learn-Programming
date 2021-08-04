#include <iostream>

#include "../Vector3D/Vector3D.h"

using namespace std;

bool hitSphere(const Point3D &sphereCenter, double radius, const Point3D &rayOrigin, const Vector3D &rayDirection) {
    const Vector3D aMinusC = rayOrigin - sphereCenter;
    const auto a = rayDirection.dot(rayDirection);
    const auto b = 2.0 * aMinusC.dot(rayDirection);
    const auto c = aMinusC.dot(aMinusC) - radius * radius;
    const auto discriminant = b * b - 4 * a * c;
    return discriminant > 0;
}

int main(int argc, char** argv) {
    
    // IO Stream Setup

    cout << boolalpha;
    cout << "Testing hitSphere Function" << '\n';

    const Point3D rayOrigin = {0, 0, 0};
    const Vector3D rayDirection = {0, 0, -1};

    // Test One

    const Point3D testOneSphereCenter = {0, 0, -1};
    const double testOneSphereRadius = 0.5;

    const auto testOne = hitSphere(testOneSphereCenter, testOneSphereRadius, rayOrigin, rayDirection);

    cout << "Test One: " << '\n';
    cout << '\t' << "Expected: " << true << '\n';
    cout << '\t' << "Actual: " << testOne << '\n';

    // Test Two

    const Point3D testTwoSphereCenter = {0, 0.50, -1};
    const double testTwoSphereRadius = 0.50;

    const auto testTwo = hitSphere(testTwoSphereCenter, testTwoSphereRadius, rayOrigin, rayDirection);

    cout << "Test Two: " << '\n';
    cout << '\t' << "Expected: " << false << '\n';
    cout << '\t' << "Actual: " << testTwo << '\n';

    return 0;
}
