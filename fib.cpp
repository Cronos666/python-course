#include <iostream>

using namespace std;

int fib(int x)
{
	if(x<=1) return 1;
	else return fib(x-1)+fib(x-2);
}
int main()
{
	int a;
	cin>>a;
	cout<<fib(a)<<endl;
	return 0;
}
