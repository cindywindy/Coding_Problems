/*
https://www.interviewcake.com/question/python/stock-price

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

*/

#include <iostream>
using namespace std;

//O(n^2) solution
int get_max_profit(int *stock_prices_pt, int length){
    int max_profit = stock_prices_pt[length-1] - stock_prices_pt[length-2];
    int current_profit=0;

    for(int i=length-1; i >= 0; i--){
        for(int j=i-1; j >= 0 ; j--){
            current_profit = stock_prices_pt[i] - stock_prices_pt[j];
            if (current_profit>max_profit){
                max_profit=current_profit;
            }
        }
    }

    return max_profit;
}

//O(n) solution
int get_max_profit2(int *stock_prices_pt, int length){
    int max_profit = stock_prices_pt[1] - stock_prices_pt[0];
    int min_value = stock_prices_pt[0];
    int current_value = stock_prices_pt[0];

    for(int i=1; i < length; i++){
        max_profit = max(max_profit, (stock_prices_pt[i]-min_value));
        min_value = min(min_value, stock_prices_pt[i]);
    }

    return max_profit;
}


int main(){
    int stock_prices[] = {0,1};

    if(sizeof(stock_prices) >= 8){
        int length_prices = sizeof(stock_prices)/sizeof(stock_prices[0]);
        cout<<get_max_profit(stock_prices, length_prices)<<endl;
        cout<<get_max_profit2(stock_prices, length_prices)<<endl;
    }
    return 0;
}