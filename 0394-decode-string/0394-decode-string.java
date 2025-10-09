class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        for(int i = 0;i<s.length();i++) {
			Character c = s.charAt(i);
			String current = "";
			if(c == ']') {
				StringBuilder word = new StringBuilder();
				while(!stack.isEmpty() && stack.peek().charAt(0) != '[') 
				{
					String curr = stack.pop();
					if(!curr.equals(current) && Character.isAlphabetic(curr.charAt(0))) 
					{
						word.insert(0,curr);
					}
				}
			
				if(!stack.isEmpty() && stack.peek().charAt(0) == '[') {
					stack.pop();
				}
				
				StringBuilder num = new StringBuilder();
				while(!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) 
				{
					num.append(stack.pop());
				}
				num.reverse();
				
				System.out.println(word + " " + num);
				int count = Integer.parseInt(num.toString());
				String x = word.toString();
				for(int j = 0; j < count-1;j++) {
					word.append(x);
				}
				System.out.println("after repeat: "+word);
				stack.add(word.toString());
				System.out.println("Stack: "+stack);
				current = word.toString();
				System.out.println("current: "+current);
				
			}
			else {
				stack.add(c.toString());
			}
		}
		System.out.println("final stack: "+stack);

		StringBuilder result = new StringBuilder();;
		while(!stack.isEmpty()) {
			result.insert(0,stack.pop());
		}
		return result.toString();
    }
}