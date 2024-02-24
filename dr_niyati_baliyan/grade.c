#include<stdio.h>

int main(){
    float a;
    scanf("%f",&a);
    if(a>=85){
        printf("Grade A+");
    } 
    else if(a>=75){
        printf("Grade A");
    } 
    else if(a>=65){
        printf("Grade B");
    } 
    else if(a>=55){
        printf("Grade C");
    }
      
    else{
        printf("Grade F");
    }
    return 0;
}