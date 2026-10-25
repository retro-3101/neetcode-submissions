/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        
        map<Node*, Node*> mapping;

        Node* new_head = new Node(0);
        Node *temp = head, *new_temp = new_head;
        while(temp){
            new_temp->next = new Node(temp->val);
            new_temp = new_temp->next;
            
            mapping[temp] = new_temp;
            temp = temp->next;
        }
        new_head = new_head->next;

        //random pointer allocation
        new_temp = new_head;
        temp = head;

        while(temp){
            new_temp->random = mapping[temp->random];
            temp = temp->next;
            new_temp = new_temp->next;
        }

        return new_head;
    }
};
