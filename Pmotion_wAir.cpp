#include <iostream>
#include <cmath>
#include <fstream>

float g = 9.8; //acceleration due to gravity

//!!!VERY USEFUL!!!
//using the <datatype&> syntax to pass new value by reference 
//define function for calculating instantaneous acceleration with drag
void acceleration(float v_x, float v_y, float C, float m, float& a_x, float& a_y) {
    a_x = -C * v_x * std::hypot(v_x, v_y) / m;
    a_y = -g - C * v_y * std::hypot(v_x, v_y) / m;
}

//define function for updating position, velocity and time
void update(float& x, float& y, float& v_x, float& v_y, float a_x, float a_y, float& t, float dt) {
    v_x += a_x * dt;
    v_y += a_y * dt;
    x += v_x * dt;
    y += v_y * dt;
    t += dt;
}

int main() {
    //take initial input from user
    float v_0, theta, dt, m, C;
    std::cout << "Enter initial velocity: ";
    std::cin >> v_0;
    std::cout << "Enter launch angle (in degrees): ";
    std::cin >> theta;
    float theta_radians = theta * M_PI / 180.0;//convert angle to radians for sin and cos functions
    std::cout << "Enter time step: ";
    std::cin >> dt;
    std::cout << "Enter mass: ";
    std::cin >> m;
    std::cout << "Enter drag coefficient: ";
    std::cin >> C;

    //initial value for position, time and maximum height
    float x = 0.0;
    float y = 0.0;
    float t = 0.0;
    float y_max = y;

    //boolean activation condition
    bool inflight = true;

    //break initial velocity into horizontal and vertical components
    float v_x = v_0 * std::cos(theta_radians);
    float v_y = v_0 * std::sin(theta_radians);

    //open output file
    std::ofstream output_file("Pmotion_wAir_cpp_output.txt");

    //run a loop as long as the projectile is in flight
    while (inflight) {
        float a_x, a_y;

        //find instantaneous acceleration
        acceleration(v_x, v_y, C, m, a_x, a_y);
        //update position, velocity and time
        update(x, y, v_x, v_y, a_x, a_y, t, dt);

        //run a loop as long as the projectile is in flight
        if (y >= 0) {
            // Output x, y, v_x, v_y, a_x, a_y to file
            output_file << t << ", " << x << ", " << y << ", " << v_x << ", " << v_y << ", " << a_x << ", " << a_y << "\n";
        
            if (y > y_max) {
            //update maximum height
            y_max = y;
            }
        }
        else {
            inflight = false;
        }
    }


    //close output file
    output_file.close();

    //output summary
    std::cout<<"The maximum height was "<<y_max<<"\n";
    std::cout<<"The horizontal range was "<<x<<"\n";

    return 0;
}
