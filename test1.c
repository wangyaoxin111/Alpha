#inlcude<stdio.h>
void main(void)
{
 int x=5;
 if(fork())
{
 x+=30;
 printf("%d\n",x);
}
 else 
   printf("%d\n",x);
   printf("%d\n",x);
}
