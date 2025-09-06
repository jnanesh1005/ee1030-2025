#include <stdio.h>
 
double start_points[4][3]={
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0}
};
double end_points[4][3]={
	{3.0,-1.0,0.0},
	{2.0,1.0,-3.0},
	{3/2,-1/2,0.0},
	{1/2,3/2,-3.0}
};
void get_start_points(double *arr){
	for (int i=0;i<4;i++){
		arr[i*3+0]=start_points[i][0];
		arr[i*3+1]=start_points[i][1];
		arr[i*3+2]=start_points[i][2];
	}
}
void get_end_points(double *arr){
	for (int i=0;i<4;i++){
		arr[i*3+0]=end_points[i][0];
		arr[i*3+1]=end_points[i][1];
		arr[i*3+2]=end_points[i][2];
	}
}
