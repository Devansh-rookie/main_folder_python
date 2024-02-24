#include<stdio.h>
#include<math.h>
int reverse(int);
int main()
{
	int a,b,r,s,t,w;
	printf("enter a");
	scanf("%d",&a);
	printf("enter b");
	scanf("%d",&b);
	r=reverse(a);
	s=reverse(b);
	t=r+s;
	w=reverse(t);
	printf("%d",w);
	return 0;
}
int reverse(int x)
{
	int i=0,j,z,num=0,op_num;
    op_num= x;
	while(op_num>0)
	{
        op_num/=10;
		i++;
	}
	for(j=0;j<i;j++)
	{
		z=x%10;
		x=x/10;
		num=num+z*pow(10,i-j);
	}
	return num;
}