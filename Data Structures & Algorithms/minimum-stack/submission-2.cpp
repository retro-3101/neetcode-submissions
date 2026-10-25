class MinStack {
public:
    stack<long> nums;
    long min_num;

    MinStack() {
        
    }
    
    void push(int val) {
        if(nums.empty()){
            nums.push(0);
            min_num = val;
        }
        else{
            nums.push(val - min_num);
            if(val < min_num)min_num = val;
        }
    }
    
    void pop() {
        if(nums.empty())return;

        long num = nums.top(); nums.pop();

        if(num < 0)min_num = min_num - num;
    }
    
    int top() {
        long top = nums.top();
        return  (top>0) ? top+min_num : min_num;
    }
    
    int getMin() {
        return (int)min_num;
    }
};
