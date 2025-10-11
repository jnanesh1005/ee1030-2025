#include <stdio.h>

void print_matrix(float matrix[2][3]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%8.2f ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    float matrix[2][3] = {
        {3.0, -1.0, 3.0},
        {-3.0, 2.0, 6.0}
    };

    printf("Initial Augmented Matrix:\n");
    print_matrix(matrix);

    for (int j = 0; j < 3; j++) {
        matrix[1][j] = matrix[1][j] + matrix[0][j];
    }

    printf("\nMatrix after Row Operation (R2 -> R2 + R1):\n");
    print_matrix(matrix);

    float y = matrix[1][2] / matrix[1][1];
    float x = (matrix[0][2] - (matrix[0][1] * y)) / matrix[0][0];
    int total_students = (int)(x * y);

    printf("\n--- Solution ---\n");
    printf("Number of rows (x): %.0f\n", x);
    printf("Number of students per row (y): %.0f\n", y);
    printf("Total number of students in the class: %d\n", total_students);

    return 0;
}

