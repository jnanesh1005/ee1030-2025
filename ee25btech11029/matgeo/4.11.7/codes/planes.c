#include <stdlib.h>
#include <math.h>

void free_points(float* points) {
    if (points != NULL) {
        free(points);
    }
}

float* generate_plane_1_points(float y_min, float y_max, float z_min, float z_max, int num_steps) {
    if (num_steps <= 1) {
        return NULL;
    }

    int total_points = num_steps * num_steps;
    float* points = (float*)malloc(total_points * 3 * sizeof(float));
    if (points == NULL) {
        return NULL;
    }

    float y_step_size = (y_max - y_min) / (num_steps - 1);
    float z_step_size = (z_max - z_min) / (num_steps - 1);

    int index = 0;
    for (int i = 0; i < num_steps; i++) {
        float y = y_min + i * y_step_size;
        for (int j = 0; j < num_steps; j++) {
            float z = z_min + j * z_step_size;
            float x = -2.0f * y - 4.0f;

            points[index++] = x;
            points[index++] = y;
            points[index++] = z;
        }
    }
    return points;
}

float* generate_plane_2_points(float x_min, float x_max, float y_min, float y_max, int num_steps) {
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
            float z = (-3.0f * x + y) / 4.0f;

            points[index++] = x;
            points[index++] = y;
            points[index++] = z;
        }
    }
    return points;
}

float* generate_plane_3_points(float x_min, float x_max, float y_min, float y_max, int num_steps) {
    if (num_steps <= 1) {
        return NULL;
    }

    int total_points = num_steps * num_steps;
    float* points = (float*)malloc(total_points * 3 * sizeof(float));
    if (points == NULL) {
        return NULL;
    }
    
    const float sqrt287 = sqrtf(287.0f);
    const float A = 23.0f + 3.0f * sqrt287;
    const float B = 53.0f - sqrt287;
    const float C = 4.0f * sqrt287 - 4.0f;
    const float D = 104.0f;

    float x_step_size = (x_max - x_min) / (num_steps - 1);
    float y_step_size = (y_max - y_min) / (num_steps - 1);

    int index = 0;
    for (int i = 0; i < num_steps; i++) {
        float x = x_min + i * x_step_size;
        for (int j = 0; j < num_steps; j++) {
            float y = y_min + j * y_step_size;
            float z = (-A * x - B * y - D) / C;

            points[index++] = x;
            points[index++] = y;
            points[index++] = z;
        }
    }
    return points;
}

float* generate_plane_4_points(float x_min, float x_max, float y_min, float y_max, int num_steps) {
    if (num_steps <= 1) {
        return NULL;
    }

    int total_points = num_steps * num_steps;
    float* points = (float*)malloc(total_points * 3 * sizeof(float));
    if (points == NULL) {
        return NULL;
    }

    const float sqrt287 = sqrtf(287.0f);
    const float A = 23.0f - 3.0f * sqrt287;
    const float B = 53.0f + sqrt287;
    const float C = -4.0f - 4.0f * sqrt287;
    const float D = 104.0f;

    float x_step_size = (x_max - x_min) / (num_steps - 1);
    float y_step_size = (y_max - y_min) / (num_steps - 1);

    int index = 0;
    for (int i = 0; i < num_steps; i++) {
        float x = x_min + i * x_step_size;
        for (int j = 0; j < num_steps; j++) {
            float y = y_min + j * y_step_size;
            float z = (-A * x - B * y - D) / C;

            points[index++] = x;
            points[index++] = y;
            points[index++] = z;
        }
    }
    return points;
}
