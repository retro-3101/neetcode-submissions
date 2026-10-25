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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* result = new ListNode(0);
        ListNode* curr = result;
        ListNode* prev = curr;

        while(l1 or l2){
            int a = curr->val;
            
            if(l1){
                a = a + l1->val;
                l1 = l1->next;
            }
            if(l2){
                a = a + l2->val;
                l2 = l2->next;
            }

            curr->val = (a)%10;
            curr->next = new ListNode(a/10);

            prev = curr;
            curr = curr->next;    
        }
        if(curr->val == 0){
            prev->next = NULL;
        }

        return result;
    }
};
