import java.util.*;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        
        List<Integer> result = new ArrayList<>();
        
        if (s == null || s.length() == 0 || words.length == 0) {
            return result;
        }
        
        int wordLen = words[0].length();
        int wordCount = words.length;
        int totalLen = wordLen * wordCount;
        
        HashMap<String, Integer> wordMap = new HashMap<>();
        
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }
        
        for (int i = 0; i <= s.length() - totalLen; i++) {
            
            HashMap<String, Integer> seen = new HashMap<>();
            int j = 0;
            
            while (j < wordCount) {
                
                int start = i + j * wordLen;
                String currentWord = s.substring(start, start + wordLen);
                
                if (!wordMap.containsKey(currentWord)) {
                    break;
                }
                
                seen.put(currentWord,
                         seen.getOrDefault(currentWord, 0) + 1);
                
                if (seen.get(currentWord) > wordMap.get(currentWord)) {
                    break;
                }
                
                j++;
            }
            
            if (j == wordCount) {
                result.add(i);
            }
        }
        
        return result;
    }
}
