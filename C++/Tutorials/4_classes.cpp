#include<iostream>
using namespace std;

//classes almost same as struct only difference is we can make private values and we can add functions in it. it is not only a simple datatype.
class money{
    private:                                      //anything in private is inaccessible
        int id=261;
        string name="Awesome";
        
    public:
        int DA;
        int sal(int n){
            cout<<"Salary is: "<<n*12<<endl;
        }
        void pr(){
            cout<<id<<endl;
            cout<<name<<endl;
        }
};
int main(){
    money harsh;
    harsh.sal(26);
    harsh.pr();
  
    
    return 0;
}