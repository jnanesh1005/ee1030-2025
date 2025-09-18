#include <stdlib.h>


float* generate_plane_points(float x_min, float x_max, float y_min, float y_max, int num_steps) {
    if (num_steps <= 1) { 
        return NULL;
    }

    int total_points = num_steps * num_steps;
    float* points = (float*)malloc(total_points * 3 * sizeof(float));
    if (points == NULL) {
        return NULL; 
    }

   
    float x_step_size = (x_max - x_min) / (num_steps - 1);
    float y_step_size = (y_max - y_min) / (num_steps - 1);

    int index = 0;
   
    for (int i = 0; i < num_steps; i++) {
        float x = x_min + i * x_step_size;
        
        for (int j = 0; j < num_steps; j++) {
            float y = y_min + j * y_step_size;

          
            float z = 4.0f - 2.0f * x - (4.0f / 3.0f) * y;

           
            points[index++] = x;
            points[index++] = y;
            points[index++] = z;
        }
    }

    return points;
}


void free_points(float* points) {
    if (points != NULL) {
        free(points);
    }
}
