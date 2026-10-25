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
    pair<ListNode*, ListNode*> reverseGroup(ListNode* head, ListNode* tail){

        ListNode* curr = head->next, *prev = head;

        prev->next = NULL;

        ListNode* newtail = prev;

        while(curr != tail){
            ListNode* after = curr->next;
            curr->next = prev;
            prev = curr;
            curr = after;
        }

        return {prev, newtail};
    }

    ListNode* reverseKGroup(ListNode* head, int k) {

        if(k == 1)return head;
        
        ListNode* newhead = head;
        ListNode* curr = new ListNode(0);
        curr->next = head;
        int count = 0;

        while(curr){
            ListNode* end = curr->next;

            while(count < k and end){
                end = end->next;
                count++;
            }

            if(count == k){

                count = 0;

                pair<ListNode*, ListNode*> reversed = reverseGroup(curr->next, end);

                curr->next = reversed.first;
                reversed.second->next = end;
                curr = reversed.second;

                if(newhead == head)newhead = reversed.first;
            }
            else{
                break;
            }
        }

        return newhead;
    }
};
