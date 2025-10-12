class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        List<String> index;
        int ind = 0;
        for(int i = 0; i < strs.length; i++){
            char[] word = strs[i].toCharArray();
            Arrays.sort(word);
            String s = new String(word);

            if(map.containsKey(s)){
                index = map.get(s);
                index.add(strs[ind]);
                map.put(s,index);
            }else{
                index = new ArrayList<String>();
                index.add(strs[ind]);
                map.put(s,index);
            }
            ind++;
        }
        List<List<String>> result = new ArrayList<>();
        for(Map.Entry<String, List<String>> entry : map.entrySet()){
            List<String> words = entry.getValue();
            result.add(words);
        }
        return result;
    
    }
}