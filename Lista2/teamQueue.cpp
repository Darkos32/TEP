#include <iostream>
#include <queue>
#include <map>
#include <array>
#include<cstring>
#include<string>
using namespace std;

class Team{
    public:
        bool inFila;
        queue<string> fila;
        Team(){
            inFila = false;
        }
        void imprimir(){
            for (size_t i = 0; i < fila.size(); i++)
            {
                string tmp;
                tmp = fila.front();
                fila.pop();
                cout <<tmp << endl;
            }
        }

};

int main(int argc, char const *argv[])
{
    int n_filas;
    int *tam_filas = new int[n_filas];
    string linha;
    while (true)
    {
        cin >> n_filas;
        if (n_filas == 0)
        {
            break;
        }
        Team **filas = new Team *[n_filas];
        
        for (size_t i = 0; i < n_filas; i++)
        {
            filas[i] = new Team();
            string x;
            do
            {
                cin >> x;
                linha += x;
            } while (x != "\n");
            cout << linha;
            char linha_array[linha.size()];
            char *token = strtok(linha_array, " ");
            tam_filas[i] = stoi(token);
            string temp;
            while (token != NULL)
            {
                temp = "";
                temp = token;
                filas[i]->fila.push(temp);
            }
            filas[i]->imprimir();
        }
    }
}


