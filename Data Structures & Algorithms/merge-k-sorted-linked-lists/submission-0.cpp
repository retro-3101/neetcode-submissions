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
    ListNode* Merge2Lists(ListNode* l1, ListNode* l2){

        ListNode* head = new ListNode(0);
        ListNode* curr = head;

        while(l1 or l2){

            if(!l2){
                curr->next = l1;
                l1 = l1->next;
                curr = curr->next;
                curr->next = NULL;
            }

            else if(!l1){
                curr->next = l2;
                l2 = l2->next;
                curr = curr->next;
                curr->next = NULL;
            }

            else if(l1->val > l2->val){
                curr->next = l2;
                l2 = l2->next;
                curr = curr->next;
                curr->next = NULL;
            }
            else{
                curr->next = l1;
                l1 = l1->next;
                curr = curr->next;
                curr->next = NULL;
            }
        }

        return head->next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        int n = lists.size();

        if(n == 0)return NULL; 

        for(int i=1; i<n; i++){

            lists[i] = Merge2Lists(lists[i-1], lists[i]);
        
        }

        return lists[n-1];
    }
};
