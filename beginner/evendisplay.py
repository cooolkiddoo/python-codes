
#include<stdio.h>
int main()
{
 int i,c,d;
 printf("enter the a value");
 scanf("%d",&c);
 printf("enter the b value");
 scanf("%d",&d);
 for(i=c;i<=d;i++)
 {
  if(i%2==0)
   printf("%d",i);
 }
