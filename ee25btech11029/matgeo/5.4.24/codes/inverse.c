#include <stdio.h>
#include <math.h>
#define MAX 10
void print_matrix(int n,double mat[MAX][MAX]){
    for(int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            printf("%lf",mat[i][j]);
        }
        printf("\n");
    }
}
int inverse_matrix(int n,double mat[MAX][MAX],double inverse[MAX][MAX]){
    double augvec[MAX][MAX*2];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            augvec[i][j]=mat[i][j];
        }
        for(int j=0;j<n;j++){
            augvec[i][j+n]=(i==j)?1:0;
        }
    }
    for(int i=0;i<n;i++){
        double pivot=augvec[i][i];
        if(pivot==0){
int max_row = i;
for (int k = i + 1; k < n; k++) {
    if (fabs(augvec[k][i]) > fabs(augvec[max_row][i])) {
        max_row = k;
    }
}


if (max_row != i) {
    for (int j = 0; j < 2 * n; j++) {
        double temp = augvec[i][j];
        augvec[i][j] = augvec[max_row][j];
        augvec[max_row][j] = temp;
    }
}
        }
        pivot=augvec[i][i];
        
        if(pivot==0)return 0;
        for(int j=0;j<2*n;j++){
            augvec[i][j]/=pivot;
        }
        for (int k=0;k<n;k++){
            if(k!=i){
                double factor=augvec[k][i];
                for(int j=0;j<2*n;j++){
                    augvec[k][j]-=factor*augvec[i][j];
                }
            }
        }
        
    }
    for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                inverse[i][j]=augvec[i][j+n];
            }
        }
    return 1;

}
int main(){
    int n;
    printf("enter the size of the matrix=");
    scanf("%d",&n);
    printf("\n");
    double mat[MAX][MAX];
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%lf",&mat[i][j]);
        }
    }
    double inv[MAX][MAX];
    
    inverse_matrix(n,mat,inv);
    if(inverse_matrix(n,mat,inv)==1){
        print_matrix(n,inv);}
    if(inverse_matrix(n,mat,inv)==0){
        printf("The matrix is singular");
    }
}
