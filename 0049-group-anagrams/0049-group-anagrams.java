class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<Integer>> map = new HashMap<>();
        List<Integer> index;
        int ind = 0;
        for(int i = 0; i < strs.length; i++){
            char[] word = strs[i].toCharArray();
            Arrays.sort(word);
            String s = new String(word);

            if(map.containsKey(s)){
                index = map.get(s);
                index.add(ind);
                map.put(s,index);
            }else{
                index = new ArrayList<Integer>();
                index.add(ind);
                map.put(s,index);
            }
            ind++;
        }
        List<List<String>> result = new ArrayList<>();
        for(Map.Entry<String, List<Integer>> entry : map.entrySet()){
            List<String> words = new ArrayList<>();
            List<Integer> indexes = entry.getValue();
            for(Integer i:indexes){
                words.add(strs[i]);
            }
            result.add(words);
        }
        return result;
    
    }
}