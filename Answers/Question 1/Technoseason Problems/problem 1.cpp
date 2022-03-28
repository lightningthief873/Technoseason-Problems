#include<iostream>
#include<math.h>
#include<stdio.h>

using namespace std;
//function to make the first hidden stone
int HideStone1(int x)
{
	int y;
	int e;
	int d;
	e = x % 2;
	d = x % 3;
	if (e == 0)
	{
		if (d == 0)
		{
			y = 1;
		}
		else
		{
			y = 3;
		}
	}

	if (d == 0)
	{
		if (e == 0)
		{
			y = 1;
		}
		else
		{
			y = 2;
		}
	}
	if (e !=  0)
	{
		if (d !=  0)

		{
			y = 1;
		}
	}
	return y;
}

int Hidestone2(int x) //chaos inducer
{
	int y;
	int a;
	int b;
	int c;
	int d;
	int e;
	a = x * 7 * 13 * 17;
	b = a / 73;
	c = b + a;

	e = c % 2;
	d = c % 3;
	if (e == 0)
	{
		if (d == 0)
		{
			y = 1;
		}
		else
		{
			y = 3;
		}
	}

	if (d == 0)
	{
		if (e == 0)
		{
			y = 1;
		}
		else
		{
			y = 2;
		}
	}
	if (e != 0)
	{
		if (d != 0)

		{
			y = 1;
		}
	}
	return y;

}
//to verify harrys answer and the door 
int Verify(int x, int y)
{
	int z;
	if (x == y)
	{
		z = 1;
	}
	else
	{
		z = 0;
	}
	return z;
}
//opening next door
int Hint(int x,int y,int z) //x is the input from Verify function, y is harrys chosen door & z is the door of the stone 
{
	int a;
	if (x == 1)
	{
		if (y == 1)
		{
			a = 3;
		}
		if (y == 2)
		{
			a = 1;
		}
		else
		{
			a = 2;
		}
	}
	else
	{
		if (y == 1 && z == 2)
		{
			a = 3;
		}
		if (y == 1 && z == 3)
		{
			a = 2;
		}
		if (y == 2 && z == 1)
		{
			a = 3;
		}
		if (y == 2 && z == 3)
		{
			a = 1;
		}
		if (y == 3 && z == 1)
		{
			a = 2;
		}
		if(y == 3 && z == 2)
		{
			a = 1;
		}
	
	}
	return a;
}
int Rechoice(int x,int y)//function for harry's choice and his new choice
{
	int a;
	if (x == y)
	{
		a = 1;
	}
	else
	{
		a = 0;
	}
	return a;
}
int loop(int x, int y)//this function in used in determining that the score updates only when harry wins the stone
{
	int a;
	if (x == y)
	{
		a = 0;
	}
	if (x != y)
	{
		a = 1;
	}
	return a;
}

int main()
{
	int HC;
	int CN=1;
	int HSD;
	int a;
	int OD;
	int HNC;
	int b;
	int sw=0;
	int st=0;
	int c;
	int d;
	int n;

	cout << "The winter christmas holidays had just begun. It was quite a pleasant day at Hogwarts. Hermione" << endl;
	cout << "had left hogwarts for holidays and Ron and Harry were just having a match of chess. Thats when" << endl;
	cout << "I met them for the first time. One night I told Harry what fluffy was hiding behind the closed doors " << endl;
	cout << "we took the adventure upon ourselves to find the Philosophers Stone. He went through that door and " << endl;
	cout << " somehow found out a new cave. A strange new light entered the cave. an angle was atanding in front" << endl;
	cout << "of us. She gave us 3 choices of finding the philosophers stone which was behind one of it." << endl;
	cout << "she asked us our choice" << endl;
	d = HideStone1(CN);
	HSD=Hidestone2(d); //the stone is hidden according to the number of the choice number. 
	//but is almost impossible to determine which one due to the 3 body principle of chaos theory
	even:
	cout << "Enter Harrys choice:" << endl; //harry gives his choice
	cin >> HC;
	if (HC > 3)
	{
		cout << "this door doesnt exist... taking u a few minutes earlier" << endl;
		goto even;
	}

	else
		goto odd;
	odd:
	a = Verify(HC, HSD);
	OD = Hint(a, HC, HSD);
	cout << "The angle says...i'll give u a hint...i'll tell u behind which door the stone isnt " << endl;
	cout << "The opened door is:" << OD << endl;
	cout << "Enter Harrys next choice:" << endl;
	cin >> HNC;
	
	if (HNC == OD)
	{
		cout << "This Door is already opened. Choose another door:" << endl;

	}
	else
	{
		b=Rechoice(HNC, HSD); //verifying new choice and earlier hidden door
		if(b==1)
		{
			cout << "Harry got the Philosophers stone" << endl;
		}
		else
		{
			cout << "Harry failed" << endl;
		}
	}
	CN++;

	cout << "how many turns do u want the loop to be" << endl;
	cin>>n

	cout << " The angle says: You have been in a time loop. You will have a 100 tries to free yourself." << endl;
	cout << "choose the wisest strategy to get the Philosophers stone and finally use it in the last one." << endl;

	for (CN = 2; CN < n; CN++) //same code just for n number of times 
	{
		d = HideStone1(CN);
		HSD = HideStone1(d);
		cout << "Enter Harry's choice:" << endl;
		eve:
		cin >> HC;
		if (HC > 3)
		{
			cout << "This door doesnt exist... taking you a few moments earlier..." << endl;
			goto eve;
		}
		else
			goto od;
		od:
		a = Verify(HC, HSD);
		OD = Hint(a, HC, HSD);
		cout << "The opened door is:" << OD << endl;
		cout << "Enter Harrys next choice:" << endl;
		cin >> HNC;
		b = Rechoice(HNC, HSD);
		{
			if (HNC == OD)
			{
				cout << "This Door is already opened. Choose another door:" << endl;

			}
			else
			{
				if (b == 1)
				{
					cout << "Harry got the Philosophers stone" << endl;
				}
				else
				{
					cout << "Harry failed" << endl;
				}
			}
		}
		c = loop(HC, HNC);
		if (b + c == 2)
		{
			sw++;
		}
		if (b + c == 1)
		{
			st++;
		}
		cout << "Switch Strategy score = " << sw << endl;
		cout << "Stay Strategy score = " << st << endl;
	}
	return 0;
}