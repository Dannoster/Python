#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <string>
 

#define eb emplace_back
#define mp make_pair
 
using namespace std;
 
map<string,set<string>> tree;
map<string,int> treeAmo;
map<string,bool> dp;
 
 
void getChild(string name) {
    for (auto i : tree[name]) {
        if (treeAmo[i] == 0 && !dp[i]) {
            if(tree[i].empty()) {
                dp[i] = true;
                treeAmo[name]++;
                //cout << "ZERO " << name << '(' << treeAmo[name] << ')' << ' ' << i << '(' << treeAmo[i] << ')' << '\n';
            } else {
                getChild(i);
            }
        }
        if (!dp[i]) {
            //cout << name << '(' << treeAmo[name] << ')' << ' ' << i << '(' << treeAmo[i] << ')' << ' ';
            treeAmo[name] += treeAmo[i] + 1;
            dp[i] = true;
            //cout << " TO " << name << '(' << treeAmo[name] << ')' << ' ' << i << '(' << treeAmo[i] << ')' << '\n';
        }
    }
}
 

int main() {
    int n;
    cin >> n;
    n--;
    set<string> names;
    for (int i = 0; i < n; ++i) {
        string child, parent;
        cin >> child >> parent;
        tree[parent].insert(child);
        treeAmo[parent] = 0;
        treeAmo[child] = 0;
        names.insert(parent);
        names.insert(child);
    }
    for (auto i : names) {
        getChild(i);
        cout << i << ' ' << treeAmo[i] << '\n';
    }
    return 0;
}