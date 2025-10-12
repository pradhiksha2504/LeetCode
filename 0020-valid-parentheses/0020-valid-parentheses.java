class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0;i<s.length();i++){
            char c = s.charAt(i);
            if(c == ')'){
                if(stack.isEmpty() || stack.pop() != '('){
                    return false;
                }
            }else if(c == '}'){
                if(stack.isEmpty() || stack.pop() != '{'){
                    return false;
                }
            }else if(c == ']'){
                if(stack.isEmpty() || stack.pop() != '['){
                    return false;
                }
            }else{
                stack.add(c);
            }
        }
        return stack.isEmpty();
        
    }
}