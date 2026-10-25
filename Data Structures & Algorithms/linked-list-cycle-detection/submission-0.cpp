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
    bool hasCycle(ListNode* head) {
        
        if(head->next == NULL or head->next->next == NULL)return false;

        ListNode* once = head->next;
        ListNode* twice = head->next->next;

        while(twice != NULL and twice->next != NULL){

            if(once == twice)return true;

            once = once->next;
            twice = twice->next->next;
        }

        return false;
    }
};
