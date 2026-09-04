#include<iostream>
#include<cmath>
#include<fstream>

const double g = 9.81;  // Acceleration due to gravity (m/s^2)

double deg2rad(double degrees) { //converting degree input to radian for calculation
    return degrees * M_PI / 180.0;
}

int main() {
    double v0, theta0;
    int steps;

    std::cout << "Enter initial velocity (m/s): ";
    std::cin >> v0;
    std::cout << "Enter launch angle (degrees): "; //could take radian but nobody measures in radian
    std::cin >> theta0;
    std::cout << "Enter number of steps: ";
    std::cin >> steps;

    double v_x0 = v0 * cos(deg2rad(theta0));  // Initial horizontal velocity
    double v_y0 = v0 * sin(deg2rad(theta0));  // Initial vertical velocity
    double flight_time = (2 * v_y0) / g;  // Total flight time
    double time_step = flight_time / steps;  // Time increment for each step

    std::ofstream output_file("Pmotion_output.txt");

    double x = 0.0;  // Initial horizontal position
    double y = 0.0;  // Initial vertical position
    double v_y = v_y0;  // Current vertical velocity
    double y_max = y; //maximum height at initial position
    double t = 0.0; //time variable

    for(int i = 0; i <= steps; i++) {
        if(y < 0) {
            break;
        }

        x = x + v_x0 * time_step;
        y = y + v_y * time_step - 0.5 * g * time_step * time_step;
        v_y = v_y - g*time_step;
        t += time_step;

        output_file << t << " " << x << " " << y << " " << v_x0 << " " << v_y << "\n";
        if(y > y_max) { //update maximum height if current height is greater
            y_max = y;
        }
    }
    
output_file.close();

std::cout << "Maximum height reached: " << y_max << std::endl;
std::cout << "Horizontal distance traveled: " << x << std::endl;

return 0;
}