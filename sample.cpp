#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve(){
      string s; cin>>s;
      bool temp=false;
      for(int i=s.size()-1; i>0; i--){
            if(s[i]==s[i-1]){
                  if(s[i] =='z') {
                        s.insert(i, 1, 'a');
                  }
                  else{
                        char c = s[i]+1;
                        s.insert(i, 1, c);
                  }
                  temp=true;
                  break;
            }
      }
      if(!temp){
            if(s[s.size()-1]=='z') s.insert(s.size(), 1, 'a');
            else s.insert(s.size(), 1, s[s.size()-1]+1);
      }
      cout<<s<<endl;
}

int main(){
      ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

      int t=1;
      cin>>t;
      while(t--){
            solve();
      }
      return 0;
}