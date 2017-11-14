#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

struct Node {
    int val;
    struct Node *next;
    struct Node *last;
};

typedef struct Node Node;

float* range(int ceil) {
    float *r = (float*) malloc(sizeof(float)*ceil);
    float i;
        
    for(i = 0.0; i < ceil; i += 1.0) {
        r[int(i)] = i;
    }
    
    return r;
}

Node* primes(int ceil) {
    float *sieve;
    int i, x;
    Node *head = (Node*) malloc(sizeof(Node));
    
    head->last = NULL;

    sieve = range(ceil);
    sieve[1] = 0;
    
    for(i = 0; i < sqrt(ceil); i++) {
        if(sieve[i] != 0) {
            for(x = i*i; x <= ceil; x += i) {
                sieve[x] = 0;
            }
        }
    }
    
    for(i = 0; i < ceil; i++) {
        if(sieve[i] != 0) {
          head->next = (Node*) malloc(sizeof(Node));
          head->next->last = head;
          head = head->next;
          head->val = sieve[i];
          head->next = NULL;
        }
    }
    free(sieve);
    
    while(head->last != NULL) {
        head = head->last;
    }
    head = head->next;
    free(head->last);
    head->last = NULL;

    return head;
}

float* totient_list(int ceil) {
    float *tlist;
    Node *ps;
    float i, m;
    
    tlist = range(ceil+1);
    ps = primes(ceil+1);
    
    while(1) {
        tlist[ps->val] = ps->val - 1;
        i = ps->val * 2;
        m = float(ps->val-1) / float(ps->val);
        while(i <= ceil) {
            tlist[int(i)] *= m;
            i += ps->val;
        }
        if(ps->next) {
            ps = ps->next;
            free(ps->last);
        } else {
            break;
        }
    }
    free(ps);
    for(i = 0; i <= ceil; i++) {
        tlist[int(i)] = round(tlist[int(i)]);
    }
    
    return tlist;
}

int string_length(char str[]) {
    int i;
    for(i=0; i < 8; i++) {
        if(str[i]=='\0') {
            return(i);
        }
    }
}

void string_sort(char s[]) {
    char tmp;
    int i, j, len;
    len = string_length(s);
    
    for(i = 0; i < len - 1; i++) {
        for(j = i+1; j < len; j++) {
            if(s[i] > s[j]) {
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
            }
        }
    }
}
                           
int is_permute(int n, float *tlist) {
    char s[8];
    char t[8];
    int s_len, t_len;
    
    sprintf(s, "%d", n);
    sprintf(t, "%d", int(tlist[n]));
    
    s_len = string_length(s);
    t_len = string_length(t);
    
    if(s_len != t_len) return 0;

    string_sort(s);
    string_sort(t);
    
    if(strcmp(s,t) == 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    float *tlist;
    int i, winner;
    float min;
    
    tlist = totient_list(10000000);
    min = 10.0;
    
    for(i = 2; i <= 10000000; i++) {
        if(is_permute(i, tlist)) {
            if(i/tlist[i] < min) {
                winner = i;
                min = i/tlist[i];
            }
        }
    }
    
    printf("%d\n", winner);
    
    free(tlist);
    
    return 0;
}
