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
    void reorderList(ListNode* head) {
        
        ListNode* half = head;
        int count = 0;

        ListNode* end = head;

        while(end and end->next){
            half = half->next;
            end = end->next->next;
            count++;
        }

        //reverse 2nd half
        ListNode* reverse = half;
        half = half->next;
        reverse->next = NULL;
        
        while(half){
            ListNode* temp = half->next;
            half->next = reverse;
            reverse = half;
            half = temp;
        }


        //adding 2 lists
        ListNode* start = head;

        ListNode* curr = new ListNode(0);

        while(count){
            
            curr->next = start;
            start = start->next;
            curr = curr->next;

            curr->next = reverse;
            reverse = reverse->next;
            curr = curr->next;

            count--;
        }

        return;
    }
};
