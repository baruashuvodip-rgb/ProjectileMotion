#include <iostream>
#include <cmath>
#include <fstream>

float g = 9.8; //acceleration due to gravity
float v_angular = 7.2921159e-5;  //angular velocity of the Earth in rad/s

//to calculate coriolis effect, we need to have three components of velocity.
//horizontal and vertical are given by v_x and v_y. v_z will start at 0 but will be updated with coriolis effect.
//v_x = horizontal velocity = v_0 * cos(theta) * cos(phi)
//v_y = vertical velocity = v_0 * sin(theta) * cos(phi)
// v_z = v_0 * sin(phi) where phi is the latitude of the launch site. 


//define function for calculating instantaneous acceleration with drag + coriolis effect
void acceleration(float v_x, float v_y, float v_z, float v_angular_x, float v_angular_y, float C, float m, float& a_x, float& a_y, float& a_z) {
    
    //coriolis modifications
    float a_coriolis_x = -2 * v_angular_y * v_z;
    float a_coriolis_y = 2 * v_angular_x * v_z;
    float a_coriolis_z = -2 * (v_x * v_angular_y - v_y * v_angular_x);

    //modified acceleration components
    float magnitude = std::sqrt(v_x * v_x + v_y * v_y + v_z * v_z);
    float drag_factor = C * magnitude / m; //simplifying drag calculation
    a_x = - drag_factor * v_x + a_coriolis_x;
    a_y = -g - drag_factor * v_y + a_coriolis_y;
    a_z = - drag_factor * v_z + a_coriolis_z; 
}

//quick function to update initial values for each increment
void update(float& x, float& y, float& z, float& v_x, float& v_y, float& v_z, float a_x, float a_y, float a_z, float dt) {
    x += v_x * dt + 0.5 * a_x * dt * dt;
    y += v_y * dt + 0.5 * a_y * dt * dt;
    z += v_z * dt + 0.5 * a_z * dt * dt;
    v_x += a_x * dt;
    v_y += a_y * dt;
    v_z += a_z * dt;
}

int main() {
    //take initial input from user
    float v_0, theta, phi, dt, m, C;
    std::cout << "Enter initial velocity: ";
    std::cin >> v_0;
    std::cout << "Enter launch angle (in degrees): ";
    std::cin >> theta;
    std::cout << "Enter latitude (in degrees): ";
    std::cin >> phi;
    std::cout << "Enter time step: ";
    std::cin >> dt;
    std::cout << "Enter mass: ";
    std::cin >> m;
    std::cout << "Enter drag coefficient: ";
    std::cin >> C;

    //initial value for position, time and maximum height
    float x = 0.0;
    float y = 0.0;
    float z = 0.0;
    float t = 0.0;
    float y_max = y;

    //initial value for acceleration components
    float a_x = 0.0;
    float a_y = -g;
    float a_z = 0.0;

    float theta_radians = theta * M_PI / 180.0;//convert launch angle to radians for sin and cos functions
    float phi_radians = phi * M_PI / 180.0; //convert latitude to radians
    
    //calculate angular velocity components - no component in z direction
    float v_angular_x = - v_angular * std::cos(phi_radians);
    float v_angular_y = v_angular * std::sin(phi_radians);

    //boolean activation condition
    bool inflight = true;

    //break initial velocity into x, y, z components
    float v_x = v_0 * std::cos(theta_radians);
    float v_y = v_0 * std::sin(theta_radians);
    float v_z = 0.0; //initial velocity perpendicular to launch velocity is zero
    

    //open output file
    std::ofstream output_file("Pmotion_Coriolis_cpp_output.txt");

    //run a loop as long as the projectile is in flight
    while (inflight) {
        float a_x, a_y, a_z;

        //find instantaneous acceleration with drag and coriolis effect
        acceleration(v_x, v_y, v_z, v_angular_x, v_angular_y, C, m, a_x, a_y, a_z);
        //update position, velocity and time
        update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt);

        //run a loop as long as the projectile is in flight
        if (y >= 0) {
            if (y > y_max) {
            //update maximum height
            y_max = y;
            }
            // Output x, y, z, v_x, v_y, v_z, a_x, a_y, a_z to file
            output_file <<t<<" "<<x<<" "<<y<<" "<<z<<" "<<v_x<<" "<<v_y<<" "<<v_z<<" "<<a_x<<" "<<a_y<<" "<<a_z<<"\n";
            t +=dt; //update time
        }
        //close file if y<0
        else {
            inflight = false;
        }
        
    }


    //close output file
    output_file.close();

    //output summary
    std::cout<<"The maximum height was "<<y_max<<"\n";
    std::cout<<"The horizontal range was "<<x<<"\n";
    std::cout<<"The final value of z was "<<z<<"\n";
    return 0;
}
