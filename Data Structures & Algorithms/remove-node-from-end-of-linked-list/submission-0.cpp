/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    pair<ListNode*, int> remover(ListNode* head, int n) {
        
        if(head->next == NULL){
            if(n == 1)return {NULL,1};
            else return {head, 1};
        }

        pair<ListNode*, int> temp = remover(head->next, n);
        temp.second += 1;
        if(temp.second == n){
            return temp;
        }
        else{
            head->next = temp.first;
            temp.first = head;
            return temp;
        }
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        pair<ListNode*, int> temp = remover(head, n);

        return temp.first;
    }
};
