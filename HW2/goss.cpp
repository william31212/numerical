#include <bits/stdc++.h>

using namespace std;
double arr[105][105];
double x[105];

double caltime_begin()
{
	clock_t begin = clock();
	return begin;
}

double caltime_end(double begin)
{
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	return time_spent;
}

//-10 ~ 10
int random()
{
	/* 產生亂數 */
	int x = (rand() % 10) - 5;
	if(x == 0)
	{
		x = (rand() % 10) + 1;
	}
	return x;
}

void generate(int n)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n+1; j++)
		{
			arr[i][j] = random();
		}
	}
}

void print_array(int n)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n+1; j++)
		{
			printf("%.lf ", arr[i][j]);
		}
		printf("\n");
	}
	printf("-------------------------\n");
}



int main(int argc, char const *argv[])
{
	
	/* 固定亂數種子 */
	srand(time(NULL));
	memset(arr, 0, sizeof(arr));
	memset(x, 0, sizeof(x));

	int Dimension[10] = {2,3,4,7,10,20,30,50,70,100};

	for (unsigned int a = 0; a < 10; a++)
	{
		unsigned int n = Dimension[a];
		string filename = to_string(n) + ".out";
		#ifdef DBG
		freopen(filename.c_str(), "w", stdout);
		#endif

		cout << "Dimension +" << Dimension[a] << ":" << '\n';

		generate(n);
		print_array(n);

		double begin = caltime_begin();
		//change upper matrix
		for (int k = 1; k <= n - 1; k++)
		{
			for(int i = k+1; i <= n; i++)
			{
				for(int j = 1; j <= n+1; j++)
				{
					arr[i][j] -= ((arr[i][k] / arr[k][k]) * arr[k][j]);
				}
			}
			print_array(n);
		}

		// solve
		double sum = 0;
		for(int i = n; i >= 1; i--)
		{
			sum = 0;
			for(int j = i+1; j <= n; j++)
			{
				sum += arr[i][j] * x[j];
			}
			x[i] = (arr[i][n + 1] - sum) / arr[i][i];
		}
		double solve_total_time = caltime_end(begin);

		//print answer
		for(int i = 1; i <= n; i++)
		{
			cout << "x" << i << ": " << x[i] << '\n';
		}
		cout << "Calculate time: " << solve_total_time << "s" << '\n';
	}


	return 0;
}