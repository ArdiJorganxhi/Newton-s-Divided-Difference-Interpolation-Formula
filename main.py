def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;



def tabela(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]));
    return y;



def aplikimiFormules(value, x, y, n):
    sum = y[0][0];

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);

    return sum;



def printimiTabeles(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                  end=" ");

        print("");

    



n = 8;
y = [[0 for i in range(10)]
     for j in range(10)];
x = [20, 21, 23, 24, 25, 27, 29, 30];


y[0][0] = 346;
y[1][0] = 362;
y[2][0] = 343;
y[3][0] = 339;
y[4][0] = 347;
y[5][0] = 346;
y[6][0] = 339;
y[7][0] = 394;


y = tabela(x, y, n);


printimiTabeles(y, n);


vlera = 26;


print("\nNumber of Deaths from COVID19 at", vlera, "April", "is",
      round(aplikimiFormules(vlera, x, y, n), 2))
